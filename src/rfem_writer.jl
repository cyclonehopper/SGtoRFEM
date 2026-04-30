
module SGtoRFEM.Writer

using XML
using Printf

export generate_rfem_xml

# -------------------------------------------------------------------------
# Helper functions
# -------------------------------------------------------------------------

"""
    find_element(parent::XML.Node, name::String) -> XML.Element
Return the first child element whose tag name matches `name`.
"""
function find_element(parent::XML.Node, name::String)
    for child in XML.child_nodes(parent)
        if isa(child, XML.Element) && XML.localname(child) == name
            return child::XML.Element
        end
    end
    error("Element <$name> not found under $(XML.name(parent))")
end

"""
    clear_container!(container::XML.Node)
Remove all child elements (typically <item> entries) from a container.
"""
function clear_container!(container::XML.Node)
    children = XML.child_nodes(container)
    for child in children
        isa(child, XML.Element) && XML.remove_child(container, child)
    end
end

"""
    set_text!(parent::XML.Node, tag::String, value)
Search direct children for element named `tag` and replace its text content
with `string(value)`.
"""
function set_text!(parent::XML.Node, tag::String, value)
    for child in XML.child_nodes(parent)
        if isa(child, XML.Element) && XML.localname(child) == tag
            # Remove any existing children (including text nodes)
            while length(XML.child_nodes(child)) > 0
                old = first(XML.child_nodes(child))
                XML.remove_child(child, old)
            end
            XML.add_child(child, XML.TextNode(string(value)))
            return
        end
    end
    @warn "Tag <$tag> not found in $(XML.name(parent))"
end

"""
    replace_recursive!(parent::XML.Node, tag::String, value)
Replace the text of all child elements named `tag` at any depth.
"""
function replace_recursive!(parent::XML.Node, tag::String, value)
    for child in XML.child_nodes(parent)
        if isa(child, XML.Element)
            if XML.localname(child) == tag
                while length(XML.child_nodes(child)) > 0
                    XML.remove_child(child, first(XML.child_nodes(child)))
                end
                XML.add_child(child, XML.TextNode(string(value)))
            end
            replace_recursive!(child, tag, value)
        end
    end
end

"""
    vector_join(v::Vector{Int}) -> String
Space-separated integer list string (used for assigned_to_members, definition_nodes).
"""
vector_join(v::Vector{Int}) = join(v, ",")

"""
    format_float(x::Float64) -> String
Format a floating-point number without scientific notation, trimmed trailing zeros.
"""
function format_float(x::Float64)
    s = @sprintf("%.6f", x)
    # strip trailing zeros and maybe dot
    s = replace(s, r"0+$" => "")
    if endswith(s, ".")
        s = s[1:end-1]
    end
    return s
end

# -------------------------------------------------------------------------
# Main entry
# -------------------------------------------------------------------------

"""
    generate_rfem_xml(model::RFEMMode output_path::String)

Write a Dlubal RFEM 6 XML project file based on the provided model.
The function uses the sample file  `rfem_sample.xml`  as a structural template
(kept all analysis settings unchanged) and replaces geometry, cross‑sections,
materials and loads with data from `model`.

The template must exist at `./rfem_xml/rfem_sample.xml` relative to the current
working directory or the directory of this file.
"""
function generate_rfem_xml(model::RFEMModel, outpath::String)::Nothing
    # ---- locate template --------------------------------------------------
    here = @__DIR__
    tmpl_path_here = joinpath(here, "..", "..", "rfem_xml", "rfem_sample.xml")
    tmpl_path_cwd  = joinpath(pwd(), "rfem_xml", "rfem_sample.xml")
    tmpl_path = isfile(tmpl_path_here) ? tmpl_path_here : tmpl_path_cwd
    if !isfile(tmpl_path)
        error("""
        RFEM sample template not found.
        Expected at ./rfem_xml/rfem_sample.xml or at $(tmpl_path_here)
        """)
    end

    # ---- load template ----------------------------------------------------
    doc = XML.read(tmpl_path, XML.Document)
    root = doc.root  # <document>

    # ---- navigate to <model> → <basic_objects> ----------------------------
    model_el = find_element(root, "model")
    basic     = find_element(model_el, "basic_objects")
    loadsec   = find_element(model_el, "load_cases_and_combinations")
    load_cases_cont = find_element(loadsec, "load_cases")

    # ---- containers for item lists ----------------------------------------
    mat_cont   = find_element(basic, "material")
    sec_cont   = find_element(basic, "section")
    node_cont  = find_element(basic, "node")
    line_cont  = find_element(basic, "line")
    member_cont= find_element(basic, "member")

    # ---- template items (first item of each list) ------------------------
    mat_tpl   = first(XML.child_nodes(mat_cont))
    sec_tpl   = first(XML.child_nodes(sec_cont))
    node_tpl  = first(XML.child_nodes(node_cont))
    line_tpl  = first(XML.child_nodes(line_cont))
    member_tpl= first(XML.child_nodes(member_cont))

    # load case template: first <item> under <load_cases>
    lc_tpl    = first(XML.child_nodes(load_cases_cont))
    # nodal_loads template inside that item
    nl_parent = find_element(lc_tpl, "nodal_loads")
    nl_tpl    = first(XML.child_nodes(nl_parent))

    # ---- clear existing item lists ----------------------------------------
    clear_container!(mat_cont)
    clear_container!(sec_cont)
    clear_container!(node_cont)
    clear_container!(line_cont)
    clear_container!(member_cont)
    clear_container!(load_cases_cont)

    # -------------------------------------------------------------------------
    # 1. MATERIALS
    # -------------------------------------------------------------------------
    for mat in values(model.materials)
        item = deepcopy(mat_tpl)

        # Basic identifiers
        set_text!(item, "no",          mat.id)
        set_text!(item, "name",        mat.name)

        # Elastic modulus (Pa) – numerous occurrences
        replace_recursive!(item, "elasticity_modulus_global", mat.E)
        replace_recursive!(item, "elasticity_modulus_x",      mat.E)
        replace_recursive!(item, "elasticity_modulus_y",      mat.E)
        replace_recursive!(item, "elasticity_modulus_z",      mat.E)

        # Shear modulus
        G = mat.E / (2*(1 - mat.nu))
        replace_recursive!(item, "shear_modulus_global", G)
        replace_recursive!(item, "shear_modulus_yz",    G)
        replace_recursive!(item, "shear_modulus_xz",    G)
        replace_recursive!(item, "shear_modulus_xy",    G)

        # Poisson ratio
        replace_recursive!(item, "poisson_ratio_global", mat.nu)
        replace_recursive!(item, "poisson_ratio_yz",    mat.nu)
        replace_recursive!(item, "poisson_ratio_xz",    mat.nu)
        replace_recursive!(item, "poisson_ratio_xy",    mat.nu)
        replace_recursive!(item, "poisson_ratio_zy",    mat.nu)
        replace_recursive!(item, "poisson_ratio_zx",    mat.nu)
        replace_recursive!(item, "poisson_ratio_yx",    mat.nu)

        # Density & others
        replace_recursive!(item, "mass_density", mat.density)
        replace_recursive!(item, "specific_weight", mat.density)

        # Thermal expansion
        replace_recursive!(item, "thermal_expansion_coefficient_global", mat.α)
        replace_recursive!(item, "thermal_expansion_coefficient_x", mat.α)
        replace_recursive!(item, "thermal_expansion_coefficient_y", mat.α)
        replace_recursive!(item, "thermal_expansion_coefficient_z", mat.α)

        # Yield strength
        replace_recursive!(item, "yield_strength_for_compression", mat.fy)
        replace_recursive!(item, "yield_strength_for_tension",     mat.fy)

        XML.add_child(mat_cont, item)
    end

    # -------------------------------------------------------------------------
    # 2. SECTIONS
    # -------------------------------------------------------------------------
    # Build mapping section_id → list of member IDs that use it
    sec_members = Dict{Int, Vector{Int}}()
    for (memb_id, line) in model.lines
      push!(get!(Vector{Int}, sec_members, line.sect_id), memb_id)
    end

    for xs in values(model.cross_sections)
        item = deepcopy(sec_tpl)
        sid  = xs.id
        set_text!(item, "no",              sid)
        set_text!(item, "name",            xs.name)
        # assigned members
        member_list = get(sec_members, sid, Int[])
        set_text!(item, "assigned_to_members", vector_join(member_list))

        # Cross-section material reference
        set_text!(item, "material", string(xs.material_id))

        # Basic area / inertia properties (SI units m, m^2, m^4)
        set_text!(item, "area_axial",                     format_float(xs.area))
        set_text!(item, "moment_of_inertia_bending_z",    format_float(xs.iz))
        set_text!(item, "moment_of_inertia_bending_y",    format_float(xs.iy))
        set_text!(item, "moment_of_inertia_torsion",      format_float(xs.j))

        # Shear areas (rough approximation)
        A_shear = xs.area * 0.6
        set_text!(item, "area_shear_z", format_float(A_shear))
        set_text!(item, "area_shear_y", format_float(A_shear))

        # Temperature load dimensions (depth and width in meters)
        set_text!(item, "depth_temperature_load",  format_float(xs.depth))
        set_text!(item, "width_temperature_load",  format_float(xs.flange_width))

        # Some geometry parameters – keep from template if not provided
        if xs.depth > 0
            set_text!(item, "h", format_float(xs.depth))
        end
        if xs.flange_width > 0
            set_text!(item, "b", format_float(xs.flange_width))
        end
        if xs.root_radius > 0
            set_text!(item, "r_1", format_float(xs.root_radius))
            set_text!(item, "r_2", format_float(xs.root_radius))
        end
        if xs.thickness_web > 0
            set_text!(item, "t_w", format_float(xs.thickness_web))
        end
        if xs.thickness_flange > 0
            set_text!(item, "t_f", format_float(xs.thickness_flange))
        end

        XML.add_child(sec_cont, item)
    end

    # -------------------------------------------------------------------------
    # 3. NODES
    # -------------------------------------------------------------------------
    for n in values(model.nodes)
        item = deepcopy(node_tpl)
        set_text!(item, "no", n.id)
        # coordinates – multiple places exist, update both location blocks

        # direct coordinates child
        coords = find_element(item, "coordinates")
        set_text!(coords, "x", n.x)
        set_text!(coords, "y", n.y)
        set_text!(coords, "z", n.z)

        # individual number fields
        set_text!(item, "coordinate_1", n.x)
        set_text!(item, "coordinate_2", n.y)
        set_text!(item, "coordinate_3", n.z)

        XML.add_child(node_cont, item)
    end

    # -------------------------------------------------------------------------
    # 4. LINES (geometry)
    # -------------------------------------------------------------------------
    for (line_id, ln) in model.lines
        item = deepcopy(line_tpl)
        set_text!(item, "no",               ln.id)   # integer to string
        set_text!(item, "definition_nodes", string(ln.start.node_id)*","*string(ln.end.node_id))
        # length
        len = compute_length(model.nodes[ln.start.node_id], model.nodes[ln.end.node_id])
        set_text!(item, "length",           format_float(len))

        # Determine primary direction for position_short
        n1 = model.nodes[ln.start.node_id]
        n2 = model.nodes[ln.end.node_id]
        dx, dy, dz = n2.x - n1.x, n2.y - n1.y, n2.z - n1.z
        amax = max(abs(dx), abs(dy), abs(dz))
        dir_char = abs(dx) == amax ? "X" : (abs(dy)==amax ? "Y" : "Z")
        set_text!(item, "position_short", "|| "*dir_char)

        # rotation angle – take from line beta (already in degrees)
        set_text!(item, "rotation_angle", format_float(ln.β))

        # <member> element: which member uses this line
        # We'll store member_id as same as line_id
        # find the <member> child element and set its text
        memb_el = find_element(item, "member")
        set_text!(memb_el, "", ln.id)   # the <member> tag's text content
        # Note: In template member tag probably contains number like "4".

        XML.add_child(line_cont, item)
    end

    # -------------------------------------------------------------------------
    # 5. MEMBERS (beams)
    # -------------------------------------------------------------------------
    # The member data we stored directly as vector in model.members_data after conversion.
    # We'll prepare that in converter: model.members_data::Vector{RFEMMember}
    # If not present, we can recompute.
    for memb in model.members_data
        item = deepcopy(member_tpl)

        set_text!(item, "no",                       memb.id)
        set_text!(item, "line",                     memb.line_id)

        # cross‑section references
        set_text!(item, "cross_section_start", memb.sect_id)
        set_text!(item, "cross_section_end",   memb.sect_id)
        set_text!(item, "cross_section_internal", memb.sect_id)
        set_text!(item, "cross_section_taper_end",   memb.sect_id)
        set_text!(item, "cross_section_taper_start", memb.sect_id)

        # material
        set_text!(item, "cross_section_material", memb.mat_id)

        # nodes info
        set_text!(item, "nodes",            string(memb.start_node)*","*string(memb.end_node))
        set_text!(item, "node_start",        memb.start_node)
        set_text!(item, "node_end",          memb.end_node)

        # Length / mass / volume
        set_text!(item, "analytical_length",  format_float(memb.length))
        set_text!(item, "length",             format_float(memb.length))
        set_text!(item, "analytical_volume",  format_float(memb.volume))
        set_text!(item, "volume",             format_float(memb.volume))
        set_text!(item, "analytical_mass",    format_float(memb.mass))
        set_text!(item, "mass",               format_float(memb.mass))

        # Position short (orientation)
        set_text!(item, "position_short", memb.position_short)

        # rotation angle (beta)
        set_text!(item, "rotation_angle", format_float(memb.beta))

        # centre of gravity
        cg = find_element(item, "center_of_gravity")
        set_text!(cg, "x", memb.cg_x)
        set_text!(cg, "y", memb.cg_y)
        set_text!(cg, "z", memb.cg_z)
        # also individual CG coordinates elements
        set_text!(item, "center_of_gravity_x", memb.cg_x)
        set_text!(item, "center_of_gravity_y", memb.cg_y)
        set_text!(item, "center_of_gravity_z", memb.cg_z)

        XML.add_child(member_cont, item)
    end

    # -------------------------------------------------------------------------
    # 6. LOAD CASES
    # -------------------------------------------------------------------------
    # The template may contain several <static_analysis_settings> items etc which we leave.
    # We will create new <load_case> items.
    lc_no = 0
    for cas in model.cases
        lc_no += 1
        lc_item = deepcopy(lc_tpl)
        set_text!(lc_item, "no",              lc_no)
        set_text!(lc_item, "name",            cas.name)
        # Keep other fields like analysis_type from template (static) etc.
        # Clear any existing loads
        nodal_parent = find_element(lc_item, "nodal_loads")
        clear_container!(nodal_parent)

        # Create nodal load items for this case
        for load in cas.nodal_loads
            nl_item = deepcopy(nl_tpl)
            set_text!(nl_item, "no",   load.load_no)  # sequential within case?
            set_text!(nl_item, "load_type", "LOAD_TYPE_FORCE")
            set_text!(nl_item, "nodes",  load.node_id)
            set_text!(nl_item, "coordinate_system", "1")
            set_text!(nl_item, "has_specific_direction", "false")
            set_text!(nl_item, "specific_direction_type", "DIRECTION_TYPE_ROTATED_VIA_3_ANGLES")
            set_text!(nl_item, "axes_sequence", "SEQUENCE_XYZ")
            # directions
            set_text!(nl_item, "rotated_about_angle_x","0")
            set_text!(nl_item, "rotated_about_angle_y","0")
            set_text!(nl_item, "rotated_about_angle_z","0")

            # Only one component per item; use appropriate load_direction string
            # We decide based on which component is non-zero; later we create separate items.
            # Here we assume load has .component & .value fields.
            dir_str = load.component == 'X' ? "LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U" :
                      load.component == 'Y' ? "LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V" :
                      "LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE"
            set_text!(nl_item, "load_direction", dir_str)
            set_text!(nl_item, "force_magnitude", load.magnitude)

            XML.add_child(nodal_parent, nl_item)
        end

        XML.add_child(load_cases_cont, lc_item)
    end

    # -------------------------------------------------------------------------
    # 7. WRITE OUT
    # -------------------------------------------------------------------------
    open(outpath, "w") do io
        XML.write(io, doc)
    end
    return nothing
end

# -------------------------------------------------------------------------
# Additional helper: compute length between two nodes
# -------------------------------------------------------------------------
function compute_length(n1::RFEMNode, n2::RFEMNode)
    dx = n2.x - n1.x; dy = n2.y - n1.y; dz = n2.z - n1.z
    return sqrt(dx*dx + dy*dy + dz*dz)
end

end # module SGtoRFEM.Writer
