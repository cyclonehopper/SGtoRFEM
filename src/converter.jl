# =============================================================================
# SGtoRFEM - Converter Module
# =============================================================================
# Maps parsed Space GASS data to RFEM intermediate model.
# =============================================================================

using Statistics

# =============================================================================
# SECTION CLASSIFICATION
# =============================================================================
# Classify a SG section description into an RFEM parametric shape and derive
# approximate dimensions (m). Description strings win; parsed row-2 dims
# (depth / flange_width / thickness_web / thickness_flange) fill the gaps.
#
# Returns (shape, h, b, tw, tf, r) all in meters.
# =============================================================================

function _num(s::AbstractString)
    v = tryparse(Float64, strip(s))
    return v === nothing ? 0.0 : v
end

function classify_section(sgs::SGSection)
    desc = uppercase(sgs.description)

    # CHS e.g. "219.1x6.4 CHS" or "219.1*6.4 CHS"
    m = match(r"(\d+(?:\.\d+)?)\s*[x*]\s*(\d+(?:\.\d+)?)\s*(?:CHS|PIPE)"i, desc)
    if m !== nothing
        d = _num(m.captures[1]) / 1000.0
        t = _num(m.captures[2]) / 1000.0
        return ("CHS", d, d, t, t, 0.0)
    end

    # RHS/SHS e.g. "100*50*6 RHS" or square "89*5 SHS"
    m = match(r"(\d+(?:\.\d+)?)\s*[x*]\s*(\d+(?:\.\d+)?)\s*[x*]\s*(\d+(?:\.\d+)?)\s*(RHS|SHS)", desc)
    if m !== nothing
        h = _num(m.captures[1]) / 1000.0
        b = _num(m.captures[2]) / 1000.0
        t = _num(m.captures[3]) / 1000.0
        shape = String(m.captures[4])
        return (shape, h, b, t, t, 0.0)
    end
    m = match(r"(\d+(?:\.\d+)?)\s*[x*]\s*(\d+(?:\.\d+)?)\s*(RHS|SHS)", desc)
    if m !== nothing
        h = _num(m.captures[1]) / 1000.0
        t = _num(m.captures[2]) / 1000.0
        shape = String(m.captures[3])
        return (shape, h, h, t, t, 0.0)
    end

    # Equal angle e.g. "90*10 EA" or "90x90x10 EA"
    m = match(r"(\d+(?:\.\d+)?)\s*(?:[x*]\s*(\d+(?:\.\d+)?))?\s*[x*]?\s*(\d+(?:\.\d+)?)?\s*EA\b", desc)
    if m !== nothing && m.captures[1] !== nothing
        leg = _num(m.captures[1]) / 1000.0
        t   = m.captures[2] !== nothing ? _num(m.captures[2]) / 1000.0 :
              m.captures[3] !== nothing ? _num(m.captures[3]) / 1000.0 : 0.0
        return ("LE", leg, leg, t, t, 0.0)
    end

    # PFC channel e.g. "200 PFC" – use row-2 dims
    if occursin(r"\bPFC\b", desc)
        h = sgs.depth > 0 ? sgs.depth/1000.0 : 0.2
        b = sgs.flange_width > 0 ? sgs.flange_width/1000.0 : max(0.075, h*0.4)
        tw = sgs.thickness_web > 0 ? sgs.thickness_web/1000.0 : 0.006
        tf = sgs.thickness_flange > 0 ? sgs.thickness_flange/1000.0 : 0.01
        return ("U", h, b, tw, tf, 0.0)
    end

    # I-sections: UB/UC/WB/WC/N/I names, or anything with row-2 depth+width
    h = sgs.depth/1000.0
    b = sgs.flange_width/1000.0
    tw = sgs.thickness_web/1000.0
    tf = sgs.thickness_flange/1000.0
    r  = sgs.root_radius/1000.0
    if occursin(r"(UB|UC|WB|WC|\bI\s?SEC|\bW\d)", desc) || (h > 0 && b > 0)
        h > 0 || (h = sqrt(max(sgs.area, 100.0)*1e-6 * 20))   # crude fallback
        b > 0 || (b = 0.5*h)
        tw <= 0 && (tw = 0.006)
        tf > 0 || (tf = 1.6*tw)
        return ("I", h, b, tw, tf, min(max(r, 0.0), 2*tf))
    end

    # Unknown – synthesise an I-section from area alone
    A = max(sgs.area, 100.0) * 1e-6            # m^2
    h = sqrt(A * 15)
    @warn "Section '$(sgs.description)' not recognised; approximating as I-section $(round(h*1000,digits=1))mm deep"
    return ("UNKNOWN", h, 0.5*h, 0.006, 0.010, 0.0)
end

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
    if isempty(materials)
        # No MATERIALS section in the SG export – assume structural steel
        materials[1] = RFEMMaterial(1, "S355", "STEEL", "",
                                    210e9, 0.3, 210e9/(2*0.7), 7.85, 355e6, 1.2e-5)
    else
        # ensure material id 1 exists so unresolved references never break import
        get!(materials, 1) do
            RFEMMaterial(1, "S355", "STEEL", "", 210e9, 0.3,
                         210e9/(2*0.7), 7.85, 355e6, 1.2e-5)
        end
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
            mat_id = 1   # default steel created below / by writer
        end

        # Unit conversion: area mm^2 → m^2 (1e-6), inertia mm^4 → m^4 (1e-12)
        A  = sgs.area * 1e-6
        Iy = sgs.iy   * 1e-12
        Iz = sgs.iz   * 1e-12
        J  = sgs.j    * 1e-12

        # Classify shape and get approximate dimensions (metres)
        shape, d_m, b_m, tw_m, tf_m, r_m = classify_section(sgs)

        # Shear area approximations (rough)
        A_shear = A * 0.6
        xs = RFEMCrossSection(sid, isempty(sgs.description) ? sgs.profile : sgs.description,
                              mat_id, "PARAMETRIC_THIN_WALLED",
                              A, Iy, Iz, J,
                              A_shear, A_shear,
                              d_m, b_m, tw_m, tf_m, r_m, shape, "")
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

        # Create Line (release codes carried through for hinge generation)
        line = RFEMLine(sgm.id, sgm.section_id, sgm.material_id,
                        start_ref, end_ref, sgm.beta_angle,
                        sgm.fix_i, sgm.fix_j,
                        Dict("release_i" => String(sgm.color1),
                             "release_j" => String(sgm.color2)))
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
    # 6. Load Cases -> nodal + member load items
    # -------------------------------------------------------------------------
    # Group nodal loads by case
    loads_by_case = Dict{Int, Vector{SGNodalLoad}}()
    for ld in sg.nodal_loads
        push!(get!(Vector{SGNodalLoad}, loads_by_case, ld.load_case), ld)
    end
    # Group member concentrated / distributed loads by case
    concs_by_case = Dict{Int, Vector{SGMembConc}}()
    for c in sg.member_concs
        push!(get!(Vector{SGMembConc}, concs_by_case, c.lc), c)
    end
    forces_by_case = Dict{Int, Vector{SGMembForce}}()
    for d in sg.member_forces
        push!(get!(Vector{SGMembForce}, forces_by_case, d.lc), d)
    end

    all_cases = sort(union(collect(keys(loads_by_case)),
                           collect(keys(concs_by_case)),
                           collect(keys(forces_by_case))))

    cases = RFEMCase[]
    for cid in all_cases
        lc_name = "LC " * string(cid)
        idx = findfirst(lc -> lc.id == cid, sg.load_cases)
        idx !== nothing && (lc_name = sg.load_cases[idx].name)

        ncomps = RFEMNodalLoadItem[]
        nmoments = RFEMNodalMomentItem[]
        mloads = RFEMMemberLoadItem[]
        load_no = 0

        for ld in get(loads_by_case, cid, SGNodalLoad[])
            for (comp, f) in (('X', ld.fx), ('Y', ld.fy), ('Z', ld.fz))
                if f != 0
                    load_no += 1
                    push!(ncomps, RFEMNodalLoadItem(load_no, ld.node_id, comp, f))
                end
            end
            for (axis, m) in (('X', ld.mx), ('Y', ld.my), ('Z', ld.mz))
                if m != 0
                    load_no += 1
                    push!(nmoments, RFEMNodalMomentItem(load_no, ld.node_id, axis, m))
                end
            end
        end

        # concentrated member loads: separate items per non-zero component
        for c in get(concs_by_case, cid, SGMembConc[])
            for (comp, mag) in (('X', c.fx), ('Y', c.fy), ('Z', c.fz))
                if mag != 0
                    load_no += 1
                    push!(mloads, RFEMMemberLoadItem(load_no, c.member, :conc_force,
                        comp, c.axis, "CONCENTRATED_1", c.relative, c.a, 0.0, mag, 0.0))
                end
            end
            for (comp, mag) in (('X', c.mx), ('Y', c.my), ('Z', c.mz))
                if mag != 0
                    load_no += 1
                    push!(mloads, RFEMMemberLoadItem(load_no, c.member, :conc_moment,
                        comp, c.axis, "CONCENTRATED_1", c.relative, c.a, 0.0, mag, 0.0))
                end
            end
        end

        # distributed member loads: trapezoidal pieces per component
        for d in get(forces_by_case, cid, SGMembForce[])
            for (comp, q1, q2) in (('X', d.fx1, d.fx2), ('Y', d.fy1, d.fy2),
                                   ('Z', d.fz1, d.fz2))
                if q1 != 0 || q2 != 0
                    load_no += 1
                    push!(mloads, RFEMMemberLoadItem(load_no, d.member, :dist,
                        comp, d.axis, "TRAPEZOIDAL", d.relative, d.a, d.b, q1, q2))
                end
            end
        end

        push!(cases, RFEMCase(cid, lc_name, ncomps, nmoments, mloads))
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