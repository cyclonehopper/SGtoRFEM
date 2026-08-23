
# Included into SGtoRFEM – shares all RFEM* struct definitions directly.
using XML
using Printf
using Printf

export generate_rfem_xml

# =============================================================================
# XML helpers (XML.jl v0.4.x API – Node{String} trees)
# =============================================================================

"""Text node with string content."""
txt(v) = Node{String}(XML.Text, nothing, nothing, string(v), nothing)

"""Element with a single text value."""
el(tag::String, v) = Node{String}(XML.Element, tag, nothing, nothing, Node[txt(v)])

"""Element with child elements (e.g. <coordinates><x>..</x>..)."""
elc(tag::String, children::Vector{<:Node}) = Node{String}(XML.Element, tag, nothing, nothing, children)

"""First direct child element with the given tag name (or nothing)."""
function find_child(parent::Node, tag::String)
    for c in something(parent.children, Node[])
        c.nodetype === XML.Element && c.tag == tag && return c
    end
    return nothing
end

"""Replace text of a direct child element; creates it if missing."""
function set_text!(parent::Node, tag::String, v)
    c = find_child(parent, tag)
    c === nothing && (push!(parent.children, el(tag, v)); return)
    empty!(c.children)
    push!(c.children, txt(v))
end

"""Remove all children of an element."""
clear_children!(parent::Node) = !isnothing(parent.children) && empty!(parent.children)

"""Format a float without scientific notation."""
function format_float(x::Real)
    s = @sprintf("%.8f", x)
    s = replace(s, r"0+$" => "")
    endswith(s, ".") && (s = s[1:end-1])
    isempty(s) && (s = "0")
    return s
end

# =============================================================================
# Parametric section definitions (verified against Dlubal gRPC schema)
# =============================================================================

"""
Map a classified shape to (section_type, parametrization_type,
manufacturing_type, dimension tags).
Dimension tags are limited to fields that exist in the RFEM cross-section
schema so the import never fails on unknown parameters.
"""
function parametric_spec(shape::String)
    if shape == "CHS"
        return ("TYPE_PARAMETRIC_THIN_WALLED",
                "PARAMETRIC_THIN_WALLED__CIRCULAR_HOLLOW_SECTION__CHS",
                "MANUFACTURING_TYPE_COLD_FORMED",
                ["d", "t"])
    elseif shape == "RHS"
        return ("TYPE_PARAMETRIC_THIN_WALLED",
                "PARAMETRIC_THIN_WALLED__RECTANGULAR_HOLLOW_SECTION__RHS",
                "MANUFACTURING_TYPE_COLD_FORMED",
                ["h", "b", "t"])
    elseif shape == "SHS"
        return ("TYPE_PARAMETRIC_THIN_WALLED",
                "PARAMETRIC_THIN_WALLED__SQUARE_HOLLOW_SECTION__SHS",
                "MANUFACTURING_TYPE_COLD_FORMED",
                ["h", "b", "t"])
    elseif shape == "U"
        return ("TYPE_PARAMETRIC_THIN_WALLED",
                "PARAMETRIC_THIN_WALLED__CHANNEL__U",
                "MANUFACTURING_TYPE_HOT_ROLLED",
                ["h", "b", "t_w", "t_f"])
    else
        # I-sections and anything unrecognised: thin-walled I is always valid.
        return ("TYPE_PARAMETRIC_THIN_WALLED",
                "PARAMETRIC_THIN_WALLED__I_SECTION__I",
                "MANUFACTURING_TYPE_HOT_ROLLED",
                ["h", "b", "t_w", "t_f", "r_1", "r_2"])
    end
end

"""Dimension values in schema field order for a classified shape."""
function section_dims(xs)
    if xs.shape == "CHS"
        return [xs.depth, xs.thickness_web]           # d, t
    elseif xs.shape == "RHS" || xs.shape == "SHS"
        return [xs.depth, xs.flange_width, xs.thickness_web]   # h, b, t
    elseif xs.shape == "U"
        return [xs.depth, xs.flange_width, xs.thickness_web, xs.thickness_flange]
    else
        # Thin-walled I: root radius r1 ≈ t_w, inner radius r2 taken as 0
        return [xs.depth, xs.flange_width, xs.thickness_web,
                xs.thickness_flange, xs.thickness_web, 0.0]
    end
end

"""
RFEM builds parametric sections by parsing the *name*, which encodes the
dimensions. Formats follow RFEM's own conventions:

    I   300/200/10/14/12/8/H          (mm: h/b/t_w/t_f/r_1/r_2, H = hot rolled)
    CHS 0.2191/0.0064/C               (m: d/t, C = cold formed – as exported by RFEM)
    RHS 0.3/0.2/0.006/C               (m: h/b/t)
    SHS 0.089/0.005/C                 (m: b/t)
    U   0.3/0.1/0.006/0.01/H          (m: h/b/t_w/t_f)
"""
function section_name(xs)
    mm(x) = string(round(x*1000, digits=1))
    m_(x) = string(round(x,     digits=4))
    if xs.shape == "CHS"
        return "CHS $(m_(xs.depth))/$(m_(xs.thickness_web))/C"
    elseif xs.shape == "RHS"
        return "RHS $(m_(xs.depth))/$(m_(xs.flange_width))/$(m_(xs.thickness_web))/C"
    elseif xs.shape == "SHS"
        return "SHS $(m_(xs.depth))/$(m_(xs.thickness_web))/C"
    elseif xs.shape == "U"
        return "U $(m_(xs.depth))/$(m_(xs.flange_width))/$(m_(xs.thickness_web))/$(m_(xs.thickness_flange))/H"
    else
        # I h/b/t_w/t_f/r_1/r_2/H with r_1 = t_w, r_2 = 0 (thin-walled)
        return "I $(mm(xs.depth))/$(mm(xs.flange_width))/$(mm(xs.thickness_web))/$(mm(xs.thickness_flange))/$(mm(xs.thickness_web))/0/H"
    end
end

# =============================================================================
# Item builders
# =============================================================================

function material_item(mat)
    G = mat.G
    item = Node{String}(XML.Element, "item", nothing, nothing, Node[])
    set_text!(item, "no", mat.id)
    set_text!(item, "material_type", "TYPE_STEEL")                       # assume all steel
    set_text!(item, "material_model", "MATERIAL_MODEL_ISOTROPIC_LINEAR_ELASTIC")
    set_text!(item, "application_context", "STEEL_DESIGN")
    set_text!(item, "user_defined_name_enabled", "true")
    set_text!(item, "name", isempty(mat.name) ? "Steel" : mat.name)
    set_text!(item, "user_defined", "true")
    set_text!(item, "definition_type", "DERIVED_NU")
    set_text!(item, "stress_failure_hypothesis", "STRESS_FAILURE_HYPOTHESIS_VON_MISES")
    set_text!(item, "is_temperature_dependent", "false")
    set_text!(item, "is_dynamic_increase_factor", "false")
    set_text!(item, "has_cost_estimation", "false")
    set_text!(item, "has_emissions_estimation", "false")

    temp_item = Node{String}(XML.Element, "item", nothing, nothing, Node[])
    set_text!(temp_item, "elasticity_modulus_global", format_float(mat.E))
    set_text!(temp_item, "elasticity_modulus_x",      format_float(mat.E))
    set_text!(temp_item, "elasticity_modulus_y",      format_float(mat.E))
    set_text!(temp_item, "elasticity_modulus_z",      format_float(mat.E))
    set_text!(temp_item, "shear_modulus_global",      format_float(G))
    set_text!(temp_item, "shear_modulus_yz",          format_float(G))
    set_text!(temp_item, "shear_modulus_xz",          format_float(G))
    set_text!(temp_item, "shear_modulus_xy",          format_float(G))
    for suffix in ("global", "yz", "xz", "xy", "zy", "zx", "yx")
        set_text!(temp_item, "poisson_ratio_"*suffix, format_float(mat.nu))
    end
    set_text!(temp_item, "mass_density", format_float(mat.density))       # t/m^3
    set_text!(temp_item, "specific_weight", format_float(mat.density*9.81)) # kN/m^3
    for suffix in ("global", "x", "y", "z")
        set_text!(temp_item, "thermal_expansion_coefficient_"*suffix, format_float(mat.alpha))
    end
    set_text!(temp_item, "division_multiplication_factor", "1")
    set_text!(temp_item, "yield_strength_for_compression", format_float(mat.fy))
    set_text!(temp_item, "yield_strength_for_tension",     format_float(mat.fy))
    set_text!(item, "temperature", elc("temperature", [temp_item]))

    set_text!(item, "stiffness_matrix_editable", "false")
    set_text!(item, "stiffness_modification", "false")
    set_text!(item, "has_linear_elastic_with_nonlinear_criteria", "false")
    set_text!(item, "is_generated", "false")
    return item
end

function section_item(xs, member_list::Vector{Int})
    sec_type, param_type, manuf, dim_tags = parametric_spec(xs.shape)
    dims = section_dims(xs)

    item = Node{String}(XML.Element, "item", nothing, nothing, Node[])
    set_text!(item, "no", xs.id)
    set_text!(item, "type", sec_type)
    if sec_type != "TYPE_PARAMETRIC_MASSIVE_I"
        set_text!(item, "manufacturing_type", manuf)
    end
    set_text!(item, "name", section_name(xs))
    set_text!(item, "assigned_to_members", join(member_list, ","))
    set_text!(item, "shear_stiffness_deactivated", "false")
    set_text!(item, "warping_stiffness_deactivated", "true")
    set_text!(item, "deactivate_shear_weld_elements", "false")
    set_text!(item, "thin_walled_model", sec_type == "TYPE_PARAMETRIC_THIN_WALLED" ? "true" : "false")
    set_text!(item, "us_spelling_of_properties", "false")
    set_text!(item, "has_cost_estimation", "false")
    set_text!(item, "has_emissions_estimation", "false")
    set_text!(item, "stress_smoothing_to_avoid_singularities", "false")

    # driving dimensions – all tags verified to exist in the RFEM schema
    for (tag, val) in zip(dim_tags, dims)
        val > 0 && set_text!(item, tag, format_float(val))
    end

    # gross properties (RFEM recomputes these for parametric sections)
    set_text!(item, "area_axial",                  format_float(xs.area))
    set_text!(item, "area_shear_z",                format_float(xs.asz))
    set_text!(item, "area_shear_y",                format_float(xs.asy))
    set_text!(item, "inclination_principal_axes", "0")
    set_text!(item, "rotation_angle", "0")
    set_text!(item, "depth_temperature_load", format_float(xs.depth))
    set_text!(item, "width_temperature_load", format_float(max(xs.flange_width, xs.depth)))
    set_text!(item, "material", xs.material_id)
    set_text!(item, "parametrization_type", param_type)
    set_text!(item, "linear_analysis_mesh_refinement_factor", "1")
    set_text!(item, "nonlinear_analysis_mesh_refinement_factor", "1")
    set_text!(item, "is_generated", "false")
    return item
end

function node_item(n)
    coords = elc("coordinates", [el("x", format_float(n.x)),
                                 el("y", format_float(n.y)),
                                 el("z", format_float(n.z))])
    item = Node{String}(XML.Element, "item", nothing, nothing, Node[])
    set_text!(item, "no", n.id)
    set_text!(item, "type", "TYPE_STANDARD")
    set_text!(item, "coordinate_system", "1")
    set_text!(item, "coordinate_system_type", "COORDINATE_SYSTEM_CARTESIAN")
    push!(item.children, coords)
    set_text!(item, "coordinate_1", format_float(n.x))
    set_text!(item, "coordinate_2", format_float(n.y))
    set_text!(item, "coordinate_3", format_float(n.z))
    set_text!(item, "is_generated", "false")
    return item
end

function line_item(ln, nodes::Dict{Int,RFEMNode})
    n1 = ln.start.node_id
    n2 = ln.end_ref.node_id
    n1d = get(nodes, n1, nothing)
    n2d = get(nodes, n2, nothing)
    if n1d !== nothing && n2d !== nothing
        len = sqrt((n2d.x-n1d.x)^2 + (n2d.y-n1d.y)^2 + (n2d.z-n1d.z)^2)
        dx, dy, dz = abs(n2d.x-n1d.x), abs(n2d.y-n1d.y), abs(n2d.z-n1d.z)
        amax = max(dx, dy, dz)
        dir_char = dx == amax ? "X" : (dy == amax ? "Y" : "Z")
    else
        len = 0.0; dir_char = "X"
    end
    β = ln.β
    item = Node{String}(XML.Element, "item", nothing, nothing, Node[])
    set_text!(item, "no", ln.id)
    set_text!(item, "definition_nodes", "$n1,$n2")
    set_text!(item, "type", "TYPE_POLYLINE")
    set_text!(item, "length", format_float(len))
    set_text!(item, "position_short", "|| "*dir_char)
    set_text!(item, "rotation_specification_type", "COORDINATE_SYSTEM_ROTATION_VIA_ANGLE")
    set_text!(item, "rotation_angle", format_float(β))
    set_text!(item, "is_rotated", abs(β) > 1e-12 ? "true" : "false")
    set_text!(item, "parent_layer", "1")
    set_text!(item, "member", ln.id)
    set_text!(item, "is_generated", "false")
    return item
end

function member_item(m; hinge_start::Int=0, hinge_end::Int=0)
    item = Node{String}(XML.Element, "item", nothing, nothing, Node[])
    set_text!(item, "no", m.id)
    set_text!(item, "type", "TYPE_BEAM")
    set_text!(item, "activate_load_transfer", "false")
    set_text!(item, "line", m.line_id)
    set_text!(item, "cross_section_distribution_type", "SECTION_DISTRIBUTION_TYPE_UNIFORM")
    set_text!(item, "nodes", "$(m.start_node),$(m.end_node)")
    set_text!(item, "node_start", m.start_node)
    set_text!(item, "node_end", m.end_node)
    set_text!(item, "analytical_length", format_float(m.length))
    set_text!(item, "length", format_float(m.length))
    set_text!(item, "position_short", m.position_short)
    set_text!(item, "load_transfer_type", "STRIPE")
    set_text!(item, "projected_length", format_float(m.length))
    set_text!(item, "is_curved", "false")
    set_text!(item, "rotation_specification_type", "COORDINATE_SYSTEM_ROTATION_VIA_ANGLE")
    set_text!(item, "rotation_angle", format_float(m.beta))
    set_text!(item, "is_rotated", abs(m.beta) > 1e-12 ? "true" : "false")
    set_text!(item, "cross_section_start", m.sect_id)
    set_text!(item, "cross_section_end", m.sect_id)
    set_text!(item, "cross_section_internal", m.sect_id)
    set_text!(item, "cross_section_taper_end", m.sect_id)
    set_text!(item, "cross_section_taper_start", m.sect_id)
    set_text!(item, "cross_section_material", m.mat_id)
    # end releases – only written when a hinge is actually needed
    hinge_start > 0 && set_text!(item, "member_hinge_start", hinge_start)
    hinge_end   > 0 && set_text!(item, "member_hinge_end",   hinge_end)
    set_text!(item, "has_any_end_modifications", "false")
    set_text!(item, "parent_layer", "1")
    set_text!(item, "is_generated", "false")
    return item
end

"""
SG end-release code (6 chars, one per DOF: x, y, z, rx, ry, rz).
'R' = released, anything else = fixed.

Member local axes (SG and RFEM identical): x = member length,
y = section minor axis, z = section major axis; right-hand rule.
So: rx = torsion (mt), ry = bending about minor axis (my),
rz = bending about major axis (mz).
"""
released_dofs(code::AbstractString) =
    Tuple(c == 'R' || c == 'r' for c in code)

function member_hinge_item(no::Int, released::NTuple{6,Bool})
    item = Node{String}(XML.Element, "item", nothing, nothing, Node[])
    set_text!(item, "no", no)
    set_text!(item, "user_defined_name_enabled", "true")
    set_text!(item, "name", "MH$no")
    # released DOFs: n=ux, vy=uy, vz=uz, mt=rx, my=ry, mz=rz
    set_text!(item, "axial_release_n",   string(released[1]))
    set_text!(item, "axial_release_vy",  string(released[2]))
    set_text!(item, "axial_release_vz",  string(released[3]))
    set_text!(item, "moment_release_mt", string(released[4]))
    set_text!(item, "moment_release_my", string(released[5]))
    set_text!(item, "moment_release_mz", string(released[6]))
    return item
end

"""Get or create a hinge id for a release pattern; returns 0 when fully fixed."""
function hinge_id!(hinges::Dict{NTuple{6,Bool},Int}, container::Node,
                   code::AbstractString)
    released = released_dofs(code)
    any(released) || return 0
    get!(hinges, released) do
        no = length(hinges) + 1
        push!(container.children, member_hinge_item(no, released))
        return no
    end
end

function load_case_item(cid, lc_name, loads::Vector{RFEMNodalLoadItem},
                        moments::Vector{RFEMNodalMomentItem},
                        mloads::Vector{RFEMMemberLoadItem})
    item = Node{String}(XML.Element, "item", nothing, nothing, Node[])
    set_text!(item, "no", cid)
    set_text!(item, "analysis_type", "ANALYSIS_TYPE_STATIC")
    set_text!(item, "name", lc_name)
    set_text!(item, "static_analysis_settings", "SA1")
    set_text!(item, "consider_imperfection", "false")
    set_text!(item, "consider_initial_state", "false")
    set_text!(item, "to_solve", "false")
    set_text!(item, "action_category", "ACTION_CATEGORY_NONE_NONE")
    set_text!(item, "self_weight_active", "false")

    nl_container = Node{String}(XML.Element, "nodal_loads", nothing, nothing, Node[])
    for ld in loads
        nl = Node{String}(XML.Element, "item", nothing, nothing, Node[])
        set_text!(nl, "no", ld.load_no)
        set_text!(nl, "load_type", "LOAD_TYPE_FORCE")
        set_text!(nl, "nodes", ld.node_id)
        set_text!(nl, "has_force_eccentricity", "false")
        set_text!(nl, "coordinate_system", "1")
        set_text!(nl, "has_specific_direction", "false")
        set_text!(nl, "specific_direction_type", "DIRECTION_TYPE_ROTATED_VIA_3_ANGLES")
        set_text!(nl, "axes_sequence", "SEQUENCE_XYZ")
        set_text!(nl, "rotated_about_angle_x", "0")
        set_text!(nl, "rotated_about_angle_y", "0")
        set_text!(nl, "rotated_about_angle_z", "0")
        set_text!(nl, "force_magnitude", format_float(ld.magnitude))
        dir_str = ld.component == 'X' ? "LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U" :
                  ld.component == 'Y' ? "LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V" :
                  "LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE"
        set_text!(nl, "load_direction", dir_str)
        set_text!(nl, "load_case", "LC"*string(cid))
        set_text!(nl, "is_generated", "false")
        push!(nl_container.children, nl)
    end
    push!(item.children, nl_container)

    # nodal moments – same container, LOAD_TYPE_MOMENT per axis component
    for mo in moments
        nl = Node{String}(XML.Element, "item", nothing, nothing, Node[])
        set_text!(nl, "no", mo.load_no)
        set_text!(nl, "load_type", "LOAD_TYPE_MOMENT")
        set_text!(nl, "nodes", mo.node_id)
        set_text!(nl, "has_force_eccentricity", "false")
        set_text!(nl, "coordinate_system", "1")
        set_text!(nl, "has_specific_direction", "false")
        set_text!(nl, "specific_direction_type", "DIRECTION_TYPE_ROTATED_VIA_3_ANGLES")
        set_text!(nl, "axes_sequence", "SEQUENCE_XYZ")
        set_text!(nl, "force_magnitude", format_float(mo.magnitude))
        dir_str = mo.axis == 'X' ? "LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U" :
                  mo.axis == 'Y' ? "LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V" :
                  "LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE"
        set_text!(nl, "load_direction", dir_str)
        set_text!(nl, "load_case", "LC"*string(cid))
        set_text!(nl, "is_generated", "false")
        push!(nl_container.children, nl)
    end

    # member loads (concentrated + trapezoidal)
    if !isempty(mloads)
        ml_container = Node{String}(XML.Element, "member_loads", nothing, nothing, Node[])
        for ml in mloads
            nl = Node{String}(XML.Element, "item", nothing, nothing, Node[])
            set_text!(nl, "no", ml.load_no)
            lt = ml.kind == :conc_moment ? "LOAD_TYPE_MOMENT" : "LOAD_TYPE_FORCE"
            set_text!(nl, "load_type", lt)
            set_text!(nl, "members", ml.member)
            set_text!(nl, "load_case", "LC"*string(cid))
            set_text!(nl, "coordinate_system", "1")
            set_text!(nl, "load_distribution",
                      ml.distribution == "TRAPEZOIDAL" ?
                      "LOAD_DISTRIBUTION_TRAPEZOIDAL" : "LOAD_DISTRIBUTION_CONCENTRATED_1")
            # axis mapping (SG model is Z-up, right-hand rule).
            # Member local axes: x = length, y = section minor axis,
            # z = section major axis – identical in SG and RFEM, so local
            # Y/Z loads pass through 1:1.
            #   'G' -> global axes (true length)   'A' -> global projected
            #   'L' -> member local axes
            dir_str =
                ml.axis == 'L' ?
                    (ml.component == 'X' ? "LOAD_DIRECTION_LOCAL_X" :
                     ml.component == 'Y' ? "LOAD_DIRECTION_LOCAL_Y" :
                                           "LOAD_DIRECTION_LOCAL_Z") :
                ml.axis == 'A' ?
                    (ml.component == 'X' ? "LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_PROJECTED_LENGTH" :
                     ml.component == 'Y' ? "LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_PROJECTED_LENGTH" :
                                           "LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_PROJECTED_LENGTH") :
                    (ml.component == 'X' ? "LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE_LENGTH" :
                     ml.component == 'Y' ? "LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE_LENGTH" :
                                           "LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE_LENGTH")
            set_text!(nl, "load_direction", dir_str)
            # magnitude: force components are forces; moment kind uses magnitude too
            set_text!(nl, "magnitude", format_float(ml.mag1))
            if ml.distribution == "TRAPEZOIDAL"
                set_text!(nl, "magnitude_1", format_float(ml.mag1))
                set_text!(nl, "magnitude_2", format_float(ml.mag2))
                set_text!(nl, "distance_b_is_defined_as_relative", string(ml.relative))
                set_text!(nl, "distance_b_relative", format_float(ml.b))
            end
            set_text!(nl, "distance_a_is_defined_as_relative", string(ml.relative))
            if ml.relative
                set_text!(nl, "distance_a_relative", format_float(ml.a))
            else
                set_text!(nl, "distance_a_absolute", format_float(ml.a))
            end
            set_text!(nl, "reference_to_list_of_members", "false")
            set_text!(nl, "is_generated", "false")
            push!(ml_container.children, nl)
        end
        push!(item.children, ml_container)
    end

    set_text!(item, "is_generated", "false")
    return item
end

# =============================================================================
# Main entry
# =============================================================================

"""
    generate_rfem_xml(model::RFEMModel, outpath::String)

Write a Dlubal RFEM 6 XML project file. Uses `rfem_xml/rfem_sample.xml`
as a template for overall document structure/analysis settings and replaces
materials, sections, nodes, lines, members and load cases.

All sections are written as **parametric** sections (dimensions only), so no
RFEM library lookup can fail: sections not found in the library are simply
approximated by their geometric parameters. All materials are written as steel.
"""
function generate_rfem_xml(model::RFEMModel, outpath::String)::Nothing
    here = @__DIR__
    tmpl_path_here = normpath(joinpath(here, "..", "rfem_xml", "rfem_sample.xml"))
    tmpl_path_cwd  = joinpath(pwd(), "rfem_xml", "rfem_sample.xml")
    tmpl_path = isfile(tmpl_path_here) ? tmpl_path_here : tmpl_path_cwd
    isfile(tmpl_path) || error("RFEM sample template not found at $tmpl_path")

    doc = open(f -> read(f, XML.Node), tmpl_path)

    # document → model
    root = nothing
    for c in doc.children
        c isa Node && c.nodetype === XML.Element && c.tag == "document" && (root = c)
    end
    root === nothing && error("Template has no <document> root")
    model_el = find_child(root, "model")
    model_el === nothing && error("Template has no <model>")
    basic = find_child(model_el, "basic_objects")
    basic === nothing && error("Template has no <basic_objects>")
    loadsec = find_child(model_el, "load_cases_and_combinations")
    loadsec === nothing && error("Template has no <load_cases_and_combinations>")
    lc_container = find_child(loadsec, "load_case")
    lc_container === nothing && error("Template has no <load_case>")

    containers = Dict{String,Node}()
    for tag in ("material", "section", "node", "line", "member")
        c = find_child(basic, tag)
        c === nothing && error("Template has no <$tag> container")
        containers[tag] = c
    end

    # ---- 1. MATERIALS (all steel) -----------------------------------------
    clear_children!(containers["material"])
    for (_, mat) in model.materials
        push!(containers["material"].children, material_item(mat))
    end

    # ---- 2. SECTIONS (parametric approximations) --------------------------
    clear_children!(containers["section"])
    sec_members = Dict{Int,Vector{Int}}()
    for memb in model.members_data
        push!(get!(Vector{Int}, sec_members, memb.sect_id), memb.id)
    end
    for (_, xs) in model.cross_sections
        push!(containers["section"].children,
              section_item(xs, get(sec_members, xs.id, Int[])))
    end

    # ---- 3. NODES ----------------------------------------------------------
    clear_children!(containers["node"])
    for (_, n) in model.nodes
        push!(containers["node"].children, node_item(n))
    end

    # ---- 4. LINES ----------------------------------------------------------
    clear_children!(containers["line"])
    for (_, ln) in model.lines
        push!(containers["line"].children, line_item(ln, model.nodes))
    end

    # ---- 5. MEMBERS (with end-release hinges) -----------------------------
    # create the <member_hinge> container if the template lacks one
    hinge_container = find_child(basic, "member_hinge")
    if hinge_container === nothing
        hinge_container = Node{String}(XML.Element, "member_hinge", nothing, nothing, Node[])
        push!(basic.children, hinge_container)
    end
    clear_children!(hinge_container)
    hinges = Dict{NTuple{6,Bool},Int}()

    clear_children!(containers["member"])
    for memb in model.members_data
        ln = get(model.lines, memb.id, nothing)
        hs = he = 0
        if ln !== nothing
            hs = hinge_id!(hinges, hinge_container, get(ln.props, "release_i", "FFFFFF"))
            he = hinge_id!(hinges, hinge_container, get(ln.props, "release_j", "FFFFFF"))
        end
        push!(containers["member"].children,
              member_item(memb; hinge_start=hs, hinge_end=he))
    end

    # ---- 6. LOAD CASES -----------------------------------------------------
    clear_children!(lc_container)
    for cas in model.cases
        push!(lc_container.children,
              load_case_item(cas.id, cas.name, cas.nodal_loads,
                             cas.nodal_moments, cas.member_loads))
    end

    open(outpath, "w") do io
        XML.write(io, doc)
    end
    return nothing
end
