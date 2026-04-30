# =============================================================================
# SGtoRFEM - Converter Module
# =============================================================================
# Maps parsed Space GASS data to RFEM intermediate model.
# =============================================================================

using ..SGtoRFEM  # for type definitions
using Statistics

"""
    convert_to_rfem(model::SGModel) -> RFEMModel

Transform a Space GASS model into an RFEM intermediate representation,
performing unit conversions (mm→m, MPa→Pa) and assembling all necessary
data for XML export.
"""
function convert_to_rfem(sg::SGModel)::RFEMModel
    # -------------------------------------------------------------------------
    # 1. Materials
    # -------------------------------------------------------------------------
    materials = Dict{Int, RFEMMaterial}()
    for (mid, sgm) in sg.materials
        # E: MPa → Pa, ν: -, density: t/m^3, fy: MPa → Pa, α: per °C (keep)
        E_pa   = sgm.E * 1e6
        fy_pa  = sgm.fy * 1e6
        G_pa   = E_pa / (2 * (1 - sgm.ν))
        mat = RFEMMaterial(mid, sgm.name, "STEEL", sgm.standard,
                           E_pa, sgm.ν, G_pa, sgm.density, fy_pa, sgm.α)
        materials[mid] = mat
    end

    # -------------------------------------------------------------------------
    # 2. Nodes
    # -------------------------------------------------------------------------
    nodes = Dict{Int, RFEMNode}()
    for (nid, sgn) in sg.nodes
        node = RFEMNode(nid, "N"*string(nid), sgn.x, sgn.y, sgn.z)
        nodes[nid] = node
    end

    # -------------------------------------------------------------------------
    # 3. Cross Sections
    # -------------------------------------------------------------------------
    cross_sections = Dict{Int, RFEMCrossSection}()
    for (sid, sgs) in sg.sections
        # Resolve material numeric ID from material_name (SG gives string)
        mat_id = 0
        for (m_id, sgm) in sg.materials
            if sgm.name == sgs.material_name
                mat_id = m_id
                break
            end
        end
        if mat_id == 0
            @warn "Material $(sgs.material_name) not found for section $sid; using 1"
            mat_id = 1
        end

        # Unit conversion: area mm^2 → m^2 (1e-6), inertia mm^4 → m^4 (1e-12)
        A  = sgs.area * 1e-6
        Iy = sgs.iy   * 1e-12
        Iz = sgs.iz   * 1e-12
        J  = sgs.j    * 1e-12

        # Dimensions mm → m
        d_m = sgs.depth      / 1000.0   # depth
        b_m = sgs.flange_width / 1000.0  # flange width
        r_m = sgs.root_radius / 1000.0

        # Try to extract wall/web thickness from description (heuristic)
        t_web  = 0.0
        t_flange = 0.0

        desc = sgs.description
        # RHS e.g. "75*50*6 RHS"
        m = match(r"(\d+(?:\.\d+)?)\*(\d+(?:\.\d+)?)\*(\d+(?:\.\d+)?)\s*RHS", desc)
        if m !== nothing
            # third number is thickness (mm)
            t_val = parse(Float64, m.captures[3]) / 1000.0
            t_web = t_val
            t_flange = t_val
        else
            # CHS e.g. "88.9*5 CHS"  (diameter * thickness)
            m = match(r"(\d+(?:\.\d+)?)\*(\d+(?:\.\d+)?)\s*CHS", desc)
            if m !== nothing
                t_val = parse(Float64, m.captures[2]) / 1000.0
                t_web = t_val   # same for all walls in pipe
                t_flange = t_val
            else
                # EA: "50*6 EA" second is thickness
                m = match(r"(\d+(?:\.\d+)?)\*(\d+(?:\.\d+)?)\s*EA", desc)
                if m !== nothing
                    t_val = parse(Float64, m.captures[2]) / 1000.0
                    t_web = t_val
                    t_flange = t_val
                else
                    # PFC/U/C maybe not explicit thickness; leave 0
                end
            end
        end

        # Shear area approximations (rough)
        A_shear = A * 0.6
        xs = RFEMCrossSection(sid, sgs.profile, mat_id, "USER_DEFINED",
                              A, Iy, Iz, J,
                              A_shear, A_shear,
                              d_m, b_m, t_web, t_flange, r_m, "")
        cross_sections[sid] = xs
    end

    # -------------------------------------------------------------------------
    # 4. Offsets (if any)
    # -------------------------------------------------------------------------
    offsets = sg.offsets  # already Dict{Int, NTuple{6,Float64}}

    # -------------------------------------------------------------------------
    # 5. Lines and Members
    # -------------------------------------------------------------------------
    lines   = Dict{Int, RFEMLine}()
    members = RFEMMember[]

    for (mid, sgm) in sg.members
        # Offsets for this member (start, end)
        dx1 = dy1 = dz1 = dx2 = dy2 = dz2 = 0.0
        if haskey(offsets, sgm.id)
            dx1, dy1, dz1, dx2, dy2, dz2 = offsets[sgm.id]
        end
        start_ref = RFEMNodeRef(sgm.start_node, dx1, dy1, dz1)
        end_ref   = RFEMNodeRef(sgm.end_node,   dx2, dy2, dz2)

        # Compute centre-line length
        n1 = sg.nodes[sgm.start_node]
        n2 = sg.nodes[sgm.end_node]
        x1 = n1.x + dx1; y1 = n1.y + dy1; z1 = n1.z + dz1
        x2 = n2.x + dx2; y2 = n2.y + dy2; z2 = n2.z + dz2
        len = sqrt( (x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2 )

        # Section data (area)
        xs = cross_sections[sgm.section_id]
        vol = len * xs.area   # m^3
        mat = materials[sgm.material_id]
        mass = vol * mat.density   # tonnes (t)

        # Centre of gravity (midpoint of centre-line)
        cgx = (x1 + x2)/2
        cgy = (y1 + y2)/2
        cgz = (z1 + z2)/2

        # Determine primary axis for position_short
        vx = x2 - x1; vy = y2 - y1; vz = z2 - z1
        a = abs(vx); b = abs(vy); c = abs(vz)
        if a >= b && a >= c
            dir_char = 'X'
        elseif b >= a && b >= c
            dir_char = 'Y'
        else
            dir_char = 'Z'
        end
        pos_short = "|| " * string(dir_char)

        # Create Line
        line = RFEMLine(sgm.id, sgm.section_id, sgm.material_id,
                        start_ref, end_ref, sgm.beta_angle,
                        sgm.fix_i, sgm.fix_j, Dict())
        lines[sgm.id] = line

        # Create Member entry
        memb = RFEMMember(sgm.id,          # member ID
                          sgm.id,          # line ID (same)
                          sgm.start_node,  # start node id
                          sgm.end_node,    # end node id
                          sgm.section_id,
                          sgm.material_id,
                          len, vol, mass,
                          cgx, cgy, cgz,
                          sgm.beta_angle,
                          pos_short)
        push!(members, memb)
    end

    # -------------------------------------------------------------------------
    # 6. Load Cases -> nodal component items
    # -------------------------------------------------------------------------
    # Group loads by case
    loads_by_case = Dict{Int, Vector{SGNodalLoad}}()
    for ld in sg.nodal_loads
        push!(get!(Vector{SGNodalLoad}, loads_by_case, ld.load_case), ld)
    end

    cases = RFEMCase[]
    for (cid, ldvec) in loads_by_case
        # Load case name
        lc_name = ""
        idx = findfirst(lc -> lc.id == cid, sg.load_cases)
        if idx !== nothing
            lc_name = sg.load_cases[idx].name
        else
            lc_name = "LC " * string(cid)
        end
        # Build component list
        ncomps = RFEMNodalLoadItem[]
        load_no = 0
        for ld in ldvec
            # produce individual component items for non-zero values
            if ld.fx != 0
                load_no += 1
                push!(ncomps, RFEMNodalLoadItem(load_no, ld.node_id, 'X', ld.fx))
            end
            if ld.fy != 0
                load_no += 1
                push!(ncomps, RFEMNodalLoadItem(load_no, ld.node_id, 'Y', ld.fy))
            end
            if ld.fz != 0
                load_no += 1
                push!(ncomps, RFEMNodalLoadItem(load_no, ld.node_id, 'Z', ld.fz))
            end
            # Moments are ignored for now (could be added as separate item if needed)
        end
        push!(cases, RFEMCase(cid, lc_name, ncomps))
    end

    # -------------------------------------------------------------------------
    # 7. Assemble Model
    # -------------------------------------------------------------------------
    model = RFEMModel(nodes, lines, cross_sections, materials,
                      cases, members, sg.title, Dict{String,String}())
    return model
end

# Helper: length without offsets
function compute_length(n1::SGNode, n2::SGNode)
    dx = n2.x - n1.x; dy = n2.y - n1.y; dz = n2.z - n1.z
    return sqrt(dx^2 + dy^2 + dz^2)
end

end # module SGtoRFEM.Converter
