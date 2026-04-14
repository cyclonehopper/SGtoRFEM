module SGtoRFEM

using DataFrames
using LinearAlgebra
using Missings
using ODBC
using SQLite

# Module-level constant for load case counters
const load_case_counters = Dict{Int,Int}()

# BUILD DICTIONARY

export table_exists
# Helper function for Access databases
function table_exists(dbconn, table_name)
    try
        # This will try to get table info - if table doesn't exist, it will throw an error
        DBInterface.execute(dbconn, "SELECT TOP 1 * FROM `$table_name`")
        return true
    catch e
        return false
    end
end

function normalize_sg_dataframe!(df::DataFrame)
    # Map common underscore/abbreviated names to what the code expects
    mapping = Dict(
        "Node_A" => "Node A",
        "Node_B" => "Node B",
        "Dir_Axis" => "Dir Axis",
        "Dir_Angle_deg" => "Dir Angle (deg)",
        "Dir_Node" => "Dir Node",
        "X_m" => "X (m)",
        "Y_m" => "Y (m)",
        "Z_m" => "Z (m)",
        "Fixity_Code_at_A" => "Fixity Code at A",
        "Fixity_Code_at_B" => "Fixity Code at B"
    )
    for (oldname, newname) in mapping
        if hasproperty(df, Symbol(oldname)) && !hasproperty(df, Symbol(newname))
            rename!(df, oldname => newname)
        end
    end
    
    # Handle general space-to-underscore and units in parentheses
    for n in names(df)
        if contains(n, "_")
            new_n = replace(n, "_" => " ")
            new_n = replace(new_n, " m" => " (m)")
            new_n = replace(new_n, " deg" => " (deg)")
            if !hasproperty(df, Symbol(new_n))
                rename!(df, n => new_n)
            end
        end
    end

    # Type conversion for String columns that should be numbers
    for n in names(df)
        col = df[!, n]
        if eltype(col) <: AbstractString
            # Try to convert to Int if it looks like an ID
            if n in ["Node", "Member", "Section", "Material", "Node A", "Node B", "Dir Node", "Case"]
                df[!, n] = passmissing(parse).(Int, col)
            # Try to convert to Float64 if it looks like a coordinate or force
            elseif contains(lowercase(n), "(m)") || contains(lowercase(n), "(deg)") || 
                   contains(lowercase(n), "stiffness") || contains(lowercase(n), "force") ||
                   n in ["X", "Y", "Z"]
                df[!, n] = passmissing(parse).(Float64, col)
            end
        end
    end

    return df
end

export set_global_model_settings
function set_global_model_settings()

    ps = "# Set global model settings:\n"
    ps *= "BaseSettings(global_axes_orientation=GlobalAxesOrientationType.E_GLOBAL_AXES_ORIENTATION_ZUP, " *
          "local_axes_orientation=LocalAxesOrientationType.E_LOCAL_AXES_ORIENTATION_YUP_X)\n\n"

    return ps
end

export create_materials
function create_materials(vMatName::Vector{String})
    ps = "# Create Materials\n"
    for i in eachindex(vMatName)
        ps *= "Material($(i), name=\"$(vMatName[i])\")\n"
    end
    ps *= "\n"
    return ps
end

export create_sections
function create_sections(dfSections::DataFrame, dfMembers::DataFrame)
    vs = ["# Create Sections\n"]

    # Create a dictionary for quick lookup of Material by Section
    material_lookup = Dict(dfMembers.Section .=> dfMembers.Material)

    for i in eachrow(dfSections)
        # Get the corresponding material number using the Section
        matnum = get(material_lookup, i.Section, 0) 
        if matnum == 0
            push!(vs, "CrossSection($(i.Section), name=\"$(i.Name)\")")
        else
            push!(vs, "CrossSection($(i.Section), name=\"$(i.Name)\", material_no=$matnum)")
        end
    end
    push!(vs, "\n")

    return join(vs, "\n")
end

export create_nodes
function create_nodes(dfNodes::DataFrame)
    vs = ["# Create Nodes\n"]  # Initialize with the header line

    for i in eachrow(dfNodes)
        # Access values in the DataFrameRow `i` directly using indexing
        push!(vs, "Node($(i[1]), $(i[2]), $(i[3]), $(i[4]))\n")
    end
    push!(vs, "\n")

    return join(vs, "")  # Join all lines into a single string
end

export parse_hinge
function parse_hinge(row::DataFrameRow, ; isStart::Bool=true)

    # Define the release parameters in order
    release_params = [
        "translational_release_n",
        "translational_release_vy",
        "translational_release_vz",
        "rotational_release_mt",
        "rotational_release_my",
        "rotational_release_mz"
    ]

    if isStart
        # Check that the key is valid
        j = 10
        fixity_key = row[j]

        if length(fixity_key) != 6 || any(c -> !(c in ['F', 'R', 'S']), fixity_key)
            throw(ArgumentError("Invalid fixity key: $fixity_key"))
        end

        # ignore if no hinge
        if fixity_key == "FFFFFF"
            return ""
        end

        # Define the mapping for each character
        fixities = []
        for i in 1:6
            if fixity_key[i] == 'F'
                push!(fixities, " $(release_params[i])=inf")
            elseif fixity_key[i] == 'S'
                # check position
                if i == 1
                    push!(fixities, " $(release_params[i])=$(row[j+2+i]*1000)") #conver kN/m to N/m
                else
                    push!(fixities, " $(release_params[i])=$(row[j+i-1]*1000)")
                end
            end
        end
    else
        j = 11

        fixity_key = row[j]

        if length(fixity_key) != 6 || any(c -> !(c in ['F', 'R', 'S']), fixity_key)
            throw(ArgumentError("Invalid fixity key: $fixity_key"))
        end

        # ignore if no hinge
        if fixity_key == "FFFFFF"
            return ""
        end

        # Define the mapping for each character
        fixities = []
        for i in 1:6
            if fixity_key[i] == 'F'
                push!(fixities, " $(release_params[i])=inf")
            elseif fixity_key[i] == 'S'
                # check position
                if i == 1
                    push!(fixities, " $(release_params[i])=$(row[j+4+i])")
                else
                    push!(fixities, " $(release_params[i])=$(row[j+i+1])")
                end
            end
        end

    end

    # Return the result
    return join(fixities, ",")
end

export get_unique_hinges
function get_unique_hinges(dfMemb::DataFrame)
    # vs = ["# Create Lines\n"]

    # Initialize a Set to track unique combinations
    unique_hinges = []
    # filtered_rows = DataFrame()
    # hinges = []

    # for node A
    for row in eachrow(dfMemb)
        hinge = parse_hinge(row)
        # Check if this fixity combination is already seen
        if !isempty(hinge) & !(hinge in unique_hinges)
            push!(unique_hinges, hinge)  # Add to unique combinations
            # push!(filtered_rows, row)  # Add the row to the filtered DataFrame
        end
    end

    # for node B
    for row in eachrow(dfMemb)
        hinge = parse_hinge(row, isStart=false)
        # Check if this fixity combination is already seen
        if !isempty(hinge) & !(hinge in unique_hinges)
            push!(unique_hinges, hinge)  # Add to unique combinations
            # push!(filtered_rows, row)  # Add the row to the filtered DataFrame
        end
    end
    return unique_hinges
end


export create_hinges
function create_hinges(hinges::Vector{Any})
    _hinges = [" # Create Member Hinges"]
    for i in eachindex(hinges)
        push!(_hinges, "MemberHinge($i," * hinges[i] * ")")
    end

    return join(_hinges, "\n")
end

export parse_dir_angle
function parse_dir_angle(dfMemb::DataFrame, df_nodes::DataFrame)
    rotation_angles = zeros(nrow(dfMemb))

    for (i, row) in enumerate(eachrow(dfMemb))
        # Get beam direction
        node_a = row["Node A"]
        node_b = row["Node B"]

        start_node = filter(r -> r.Node == node_a, df_nodes)
        end_node = filter(r -> r.Node == node_b, df_nodes)

        dx = end_node[1, "X (m)"] - start_node[1, "X (m)"]
        dy = end_node[1, "Y (m)"] - start_node[1, "Y (m)"]
        dz = end_node[1, "Z (m)"] - start_node[1, "Z (m)"]

        is_vertical = abs(dx) < 1e-3 && abs(dy) < 1e-3
        is_up = dz > 0
        # Calculate rotation based on Dir Axis
        if row["Dir Axis"] == "X Axis"
            if !is_vertical
                # Project beam direction onto YZ plane
                beam_yz = normalize([0, dy, dz])
                y_axis = [0.0, 1.0, 0.0]

                # Cross product to determine rotation
                cross_prod = cross(y_axis, beam_yz)
                beam_angle = acos(dot(y_axis, beam_yz))

                if cross_prod[3] > 0
                    if beam_angle ≤ π / 2
                        beam_angle = π / 2
                    else
                        beam_angle = -π / 2
                    end
                else
                    if beam_angle ≤ π / 2
                        beam_angle = π / 2
                    else
                        beam_angle = -π / 2
                    end
                end
            else
                beam_angle = is_up ? π : 0
            end

        elseif row["Dir Axis"] == "-X Axis"
            if !is_vertical
                # Project beam direction onto YZ plane
                beam_yz = normalize([0, dy, dz])
                y_axis = [0.0, 1.0, 0.0]

                # Cross product to determine rotation
                cross_prod = cross(y_axis, beam_yz)
                beam_angle = acos(dot(y_axis, beam_yz))

                if cross_prod[3] > 0
                    if beam_angle ≤ π / 2
                        beam_angle = -π / 2
                    else
                        beam_angle = π / 2
                    end
                else
                    if beam_angle ≤ π / 2
                        beam_angle = -π / 2
                    else
                        beam_angle = π / 2
                    end
                end
            else
                beam_angle = is_up ? 0 : π
            end

        elseif row["Dir Axis"] == "Y Axis"
            if !is_vertical
                # Project beam direction onto YZ plane
                beam_zx = normalize([dx, 0, dz])
                z_axis = [0.0, 0.0, 1.0]

                # Cross product to determine rotation
                cross_prod = cross(z_axis, beam_zx)
                beam_angle = acos(dot(z_axis, beam_zx))

                if cross_prod[3] > 0
                    beam_angle = -π / 2
                else
                    beam_angle = π / 2
                end
            else
                beam_angle = -π / 2
            end
        elseif row["Dir Axis"] == "-Y Axis"
            if !is_vertical
                # Project beam direction onto YZ plane
                beam_zx = normalize([dx, 0, dz])
                z_axis = [0.0, 0.0, 1.0]

                # Cross product to determine rotation
                cross_prod = cross(z_axis, beam_zx)
                beam_angle = acos(dot(z_axis, beam_zx))

                if cross_prod[3] > 0
                    beam_angle = π / 2
                else
                    beam_angle = -π / 2
                end
            else
                beam_angle = π / 2
            end
        elseif row["Dir Axis"] == "Z Axis"
            beam_angle = 0
        elseif row["Dir Axis"] == "-Z Axis"
            beam_angle = π
        elseif row["Dir Node"] != 0
            if !is_vertical
                # Get Dir Node coordinates
                dir_node = filter(r -> r.Node == row["Dir Node"], df_nodes)

                # Get vector from start node to Dir Node
                dir_vector = [
                    dir_node[1, "X (m)"] - start_node[1, "X (m)"],
                    dir_node[1, "Y (m)"] - start_node[1, "Y (m)"],
                    dir_node[1, "Z (m)"] - start_node[1, "Z (m)"]
                ]

                # Get beam direction vector
                beam_vector = [dx, dy, dz]

                # Normalize vectors
                beam_vector = normalize(beam_vector)
                dir_vector = normalize(dir_vector)

                # Create vertical plane normal (cross product of beam vector and vertical)
                vertical = [0.0, 0.0, 1.0]
                vertical_plane_normal = normalize(cross(beam_vector, vertical))

                # Create beam-dir plane normal
                beam_dir_plane_normal = normalize(cross(beam_vector, dir_vector))

                # Calculate angle between planes (angle between their normals)
                beam_angle = acos(dot(vertical_plane_normal, beam_dir_plane_normal))

                # Determine sign based on which side of vertical plane the dir_vector is
                if dot(dir_vector, vertical_plane_normal) < 0
                    beam_angle = -beam_angle
                end
            else
                # Get Dir Node coordinates
                dir_node = filter(r -> r.Node == row["Dir Node"], df_nodes)

                # Get vector from start node to Dir Node
                dir_vector = [
                    dir_node[1, "X (m)"] - start_node[1, "X (m)"],
                    dir_node[1, "Y (m)"] - start_node[1, "Y (m)"],
                    dir_node[1, "Z (m)"] - start_node[1, "Z (m)"]
                ]

                # Get beam direction vector
                beam_vector = [dx, dy, dz]

                # Normalize vectors
                beam_vector = normalize(beam_vector)
                dir_vector = normalize(dir_vector)

                # Create vertical plane normal (cross product of beam vector and vertical)
                vertical = [0.0, 0.0, 1.0]
                # vertical_plane_normal = normalize(cross(beam_vector, vertical))
                vertical_plane_normal = [0.0, 1.0, 0.0]

                # Create beam-dir plane normal
                beam_dir_plane_normal = normalize(cross(beam_vector, dir_vector))

                # Calculate angle between planes (angle between their normals)
                beam_angle = acos(dot(vertical_plane_normal, beam_dir_plane_normal))

                # Determine sign based on which side of vertical plane the dir_vector is
                if dot(dir_vector, vertical_plane_normal) < 0
                    beam_angle = -beam_angle
                end
            end
        else
            beam_angle = row["Dir Angle (deg)"] * π / 180
            beam_angle = -π / 2 + beam_angle
        end

        rotation_angles[i] = beam_angle
    end

    return rotation_angles
end

# Helper function for rotation
function rodrigues_rotation(axis, theta)
    # Rodrigues rotation formula
    K = [0 -axis[3] axis[2];
        axis[3] 0 -axis[1];
        -axis[2] axis[1] 0]
    I3 = Matrix{Float64}(LinearAlgebra.I, 3, 3)
    return I3 + sin(theta) * K + (1 - cos(theta)) * K^2
end

export create_beam
function create_beam(dfMemb::DataFrame, rot_angles::Vector{Float64})
    vs = ["# Create Lines\n"]
    for i in eachrow(dfMemb)
        push!(vs, "Line($(i[Symbol("Member")]), \"$(i[Symbol("Node A")]) $(i[Symbol("Node B")])\")")
    end
    push!(vs, "\n")


    push!(vs, "# Create Members ")
    # check IF THERE ARE ANY HINGES
    hinges = get_unique_hinges(dfMemb)

    for (i, r) in enumerate(eachrow(dfMemb))

        vs_row = ["Member($(r.Member), line_no=$(r.Member), start_section_no=$(r.Section)"]

        # check if r has hinge and match hinge number
        start_hinge = parse_hinge(r)
        i_start = findfirst(x -> x == start_hinge, hinges)
        if i_start !== nothing
            push!(vs_row, " member_hinge_start=$i_start")
        end

        end_hinge = parse_hinge(r, isStart=false)
        i_end = findfirst(x -> x == end_hinge, hinges)
        if i_end !== nothing
            push!(vs_row, " member_hinge_end=$i_end")
        end


        # direciton angle 
        push!(vs_row, " rotation_angle=$(rot_angles[i])")

        # join line string + )
        push!(vs, join(vs_row, ",") * ")")

    end

    return join(vs, "\n") * "\n\n"  # Join all lines into a single string
end

export parse_nodal_support
function parse_nodal_support(r::DataFrameRow)

    if isnothing(r)
        throw(ArgumentError("No Nodal Restrainsts!"))
    end

    # Define the release parameters in order
    # support_params = [
    #     "spring",
    #     "rotational_restraint"
    # ]

    # Check that the key is valid 
    fixity_key = r[2]

    if length(fixity_key) != 6 || any(c -> !(c in ['F', 'P', 'R', 'S', 'V']), fixity_key)
        throw(ArgumentError("Invalid fixity key: $fixity_key"))
    end

    # Define the mapping for each character, spring part
    fixities_spring = [" spring=["]
    for i in 1:3
        if fixity_key[i] == 'F'
            push!(fixities_spring, "inf")
        elseif fixity_key[i] == 'R'
            push!(fixities_spring, "0")
        elseif fixity_key[i] in ['S', 'V']
            # check position 
            push!(fixities_spring, "$(r[4+i] * 1000)")  # convert kN/m (default in SG) to default of N/m in RFEM
        end
    end
    s1 = replace(join(fixities_spring, ",") * "]", "[," => "[")
    # replace!(s1, r"\[,", "[")

    # Define the mapping for each character, rotational restraint part
    fixities_rotational = [" rotational_restraint=["]
    for i in 4:6
        if fixity_key[i] == 'F'
            push!(fixities_rotational, "inf")
        elseif fixity_key[i] == 'R'
            push!(fixities_rotational, "0")
        elseif fixity_key[i] in ['S', 'V', 'P']
            # check position 
            push!(fixities_rotational, "$(r[4+i] * 1000)")  # convert kN/m (default in SG) to default of N/m in RFEM
        end
    end
    r1 = replace(join(fixities_rotational, ",") * "]", "[," => "[")


    # Return the result
    return join([s1, r1], ",")
end

export get_unique_nodal_supports
function get_unique_nodal_supports(dfNodalRestraints::DataFrame)

    # Initialize a Set to track unique combinations
    unique_nodal_supports = []

    for r in eachrow(dfNodalRestraints)
        nodal_support = parse_nodal_support(r)
        # Check if this fixity combination is already seen
        if !isempty(nodal_support) & !(nodal_support in unique_nodal_supports)
            push!(unique_nodal_supports, nodal_support)  # Add to unique combinations
            # push!(filtered_rows, row)  # Add the row to the filtered DataFrame
        end
    end
    return unique_nodal_supports
end

export create_nodal_supports
function create_nodal_supports(dfNodeRestraints::DataFrame)

    vs = ["# Create Nodal Supports"]
    if isempty(dfNodeRestraints)
        return vs
    end


    nodal_supports = get_unique_nodal_supports(dfNodeRestraints)

    # collect nodes cotaining same restriants, assign to a set
    supported_nodes = [String[] for _ in 1:length(nodal_supports)]

    for r in eachrow(dfNodeRestraints)
        # parse eachnode 
        support = parse_nodal_support(r)

        idx = findfirst(s -> s == support, nodal_supports)

        if idx !== nothing
            push!(supported_nodes[idx], "$(r.Node)")
        end
    end

    for (i, s) in enumerate(supported_nodes)
        s_line = "NodalSupport($i, nodes_no=\"" * join(s, " ") * "\", $(nodal_supports[i]))"
        push!(vs, s_line)
    end
push!(vs, "\n")
    return join(vs, "\n")
end


export create_member_load_distributed
function create_member_load_distributed(df_member_loads::DataFrame)
    vs = ["# Create Member Loads - Distributed"]

    if isempty(df_member_loads)
        return ""
    end

    # Group by Case number first
    for case_group in groupby(df_member_loads, :Case)
        case_num = case_group.Case[1]

        # Get existing counter for this case (already initialized by concentrated loads if they exist)
        sub_load = get!(load_case_counters, case_num, 0)

        # Group by load pattern
        for load_group in groupby(case_group, [:Case, :Axes, :Units,
            Symbol("Start Position (m or %)"), Symbol("Finish Position (m or %)"),
            Symbol("Start X Force (kN/m)"), Symbol("Finish X Force (kN/m)"),
            Symbol("Start Y Force (kN/m)"), Symbol("Finish Y Force (kN/m)"),
            Symbol("Start Z Force (kN/m)"), Symbol("Finish Z Force (kN/m)")])

            # Collect members
            members = join(sort(unique(load_group.Member)), ",")

            # Get position and units
            start_pos = load_group[1, Symbol("Start Position (m or %)")]
            end_pos = load_group[1, Symbol("Finish Position (m or %)")]
            units = load_group[1, :Units]

            # Determine if using relative (percentage) or absolute positions
            is_relative = units == "Percent"
            distance_param_a = is_relative ? "distance_a_relative" : "distance_a_absolute"
            distance_param_b = is_relative ? "distance_b_relative" : "distance_b_absolute"

            # Convert percentage to decimal if needed
            if is_relative
                start_pos = start_pos / 100
                end_pos = end_pos / 100
            end

            # Special handling for projected loads with relative positions
            # Force relative positioning for projected loads
            if load_group[1, :Axes] == "G-Proj" && !is_relative
                # Convert absolute positions to relative (assuming member length is known)
                is_relative = true
                distance_param_a = "distance_a_relative"
                distance_param_b = "distance_b_relative"
                # You might need to calculate these based on member length
                # For now, using direct conversion
                start_pos = 0.0
                end_pos = 1.0
            end

            coord_system = ""
            if load_group[1, :Axes] == "Local"
                directions = [
                    ("LOCAL_X", "Start X Force (kN/m)", "Finish X Force (kN/m)"),
                    ("LOCAL_Y", "Start Y Force (kN/m)", "Finish Y Force (kN/m)"),
                    ("LOCAL_Z", "Start Z Force (kN/m)", "Finish Z Force (kN/m)")
                ]
            else
                # Process each direction (X, Y, Z)
                if load_group[1, :Axes] == "G-Proj"
                    directions = [
                        ("GLOBAL_X_OR_USER_DEFINED_U_PROJECTED", "Start X Force (kN/m)", "Finish X Force (kN/m)"),
                        ("GLOBAL_Y_OR_USER_DEFINED_V_PROJECTED", "Start Y Force (kN/m)", "Finish Y Force (kN/m)"),
                        ("GLOBAL_Z_OR_USER_DEFINED_W_PROJECTED", "Start Z Force (kN/m)", "Finish Z Force (kN/m)")
                    ]
                else
                    directions = [
                        ("GLOBAL_X_OR_USER_DEFINED_U_TRUE", "Start X Force (kN/m)", "Finish X Force (kN/m)"),
                        ("GLOBAL_Y_OR_USER_DEFINED_V_TRUE", "Start Y Force (kN/m)", "Finish Y Force (kN/m)"),
                        ("GLOBAL_Z_OR_USER_DEFINED_W_TRUE", "Start Z Force (kN/m)", "Finish Z Force (kN/m)")
                    ]
                end
            end


            for (dir, start_col, end_col) in directions
                start_force = load_group[1, Symbol(start_col)]
                end_force = load_group[1, Symbol(end_col)]


                if start_force != 0 || end_force != 0
                    load_case_counters[case_num] += 1
                    push!(vs, "MemberLoad.Force($(load_case_counters[case_num]), $case_num, \"$members\", " *
                              "load_distribution=MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, " *
                              "load_direction=MemberLoadDirection.LOAD_DIRECTION_$dir" *
                              ", load_parameter=[$(is_relative ? "True" : "False"), $(is_relative ? "True" : "False"), $(start_force * 1000), $(end_force * 1000), $start_pos, $end_pos])")
                end
            end
        end
    end

    push!(vs, "\n")
    return join(vs, "\n")
end


function create_analysis_settings()
    ps = "# Create Analysis Settings\n"
    ps *= "StaticAnalysisSettings(1, \"Linear\", StaticAnalysisSettingsAnalysisType.GEOMETRICALLY_LINEAR)\n\n"
    return ps
end

function create_primary_loadcase_titles(df_lc_titles::DataFrame, df_LC_table::DataFrame)
    vs = ["# Create Load Cases"]
    # Identify combination cases to exclude primary definitions if they overlap
    combo_cases = []
    if hasproperty(df_LC_table, Symbol("Combination Case"))
        combo_cases = unique(df_LC_table[!, Symbol("Combination Case")])
    end
    
    for r in eachrow(df_lc_titles)
        if !(r.Case in combo_cases)
            # Usually Case 1 is self-weight in SpaceGass models
            sw = (r.Case == 1) ? "True" : "False"
            push!(vs, "LoadCase($(r.Case), \"$(r.Title)\", self_weight=[$sw, 0.0, 0.0, 1.0], static_analysis_settings_no=1)")
        end
    end
    push!(vs, "\n")
    return join(vs, "\n")
end

function create_design_situations()
    ps = "# Create Design Situations\n"
    ps *= "DesignSituation(1, \"ULS (STR/GEO)\", design_situation_type=DesignSituationType.DESIGN_SITUATION_TYPE_ULS_STR_GEO)\n"
    ps *= "DesignSituation(2, \"SLS\", design_situation_type=DesignSituationType.DESIGN_SITUATION_TYPE_SLS_CHARACTERISTIC)\n\n"
    return ps
end

function create_load_combinations(df_lc_titles::DataFrame, df_LC_table::DataFrame)
    vs = ["# Create Load Combinations"]
    
    if isempty(df_LC_table)
        return ""
    end

    # Group by Combination Case
    for combo_group in groupby(df_LC_table, Symbol("Combination Case"))
        combo_num = combo_group[1, Symbol("Combination Case")]
        
        # Find title from titles df
        title_row = filter(r -> r.Case == combo_num, df_lc_titles)
        title = isempty(title_row) ? "Combo $combo_num" : title_row[1, :Title]
        
        # Format items: [[multiplier, case_no], ...]
        items = []
        for r in eachrow(combo_group)
            push!(items, "[$(r[Symbol("Multiplying Factor")]), $(r.Case)]")
        end
        items_str = "[" * join(items, ",") * "]"
        
        push!(vs, "LoadCombination($combo_num, \"$title\", static_analysis_settings_no=1, design_situation_no=1, items=$items_str)")
    end
    push!(vs, "\n")
    return join(vs, "\n")
end

function create_nodal_loads(df_nodal_loads::DataFrame)
    vs = ["# Create Nodal Loads"]
    if isempty(df_nodal_loads)
        return ""
    end

    for case_group in groupby(df_nodal_loads, :Case)
        case_num = case_group.Case[1]
        
        # Identify columns for force and moment
        force_cols = [n for n in names(df_nodal_loads) if contains(lowercase(n), "force")]
        moment_cols = [n for n in names(df_nodal_loads) if contains(lowercase(n), "moment")]
        
        # Ensure we have column names to group by
        group_cols = vcat([:Node], force_cols, moment_cols)
        for load_group in groupby(case_group, intersect(group_cols, names(case_group)))
            nodes = join(unique(load_group.Node), " ")
            
            # Map columns to RFEM direction enums
            mapping = [
                ("X Force", "GLOBAL_X_OR_USER_DEFINED_U_TRUE"),
                ("Y Force", "GLOBAL_Y_OR_USER_DEFINED_V_TRUE"),
                ("Z Force", "GLOBAL_Z_OR_USER_DEFINED_W_TRUE"),
                ("X Moment", "GLOBAL_X_OR_USER_DEFINED_U_TRUE"),
                ("Y Moment", "GLOBAL_Y_OR_USER_DEFINED_V_TRUE"),
                ("Z Moment", "GLOBAL_Z_OR_USER_DEFINED_W_TRUE")
            ]
            
            for (prefix, rfem_dir) in mapping
                # Find matching column
                col_name = findfirst(n -> contains(n, prefix), names(df_nodal_loads))
                if col_name !== nothing
                    val = load_group[1, col_name] * 1000
                    if val != 0
                        load_id = get!(load_case_counters, case_num, 0) + 1
                        load_case_counters[case_num] = load_id
                        
                        load_type = contains(prefix, "Force") ? "NodalLoad" : "NodalMoment" # Simplified
                        # Note: NodalLoad in RFEM 6 Python API handles both, usually via load_type parameter
                        # Here we use the simplified NodalLoad constructor
                        push!(vs, "NodalLoad($load_id, $case_num, \"$nodes\", load_direction=NodalLoadDirection.LOAD_DIRECTION_$rfem_dir, load_parameter=[$val])")
                    end
                end
            end
        end
    end
    push!(vs, "\n")
    return join(vs, "\n")
end

function create_member_load_concentrated(df_member_loads::DataFrame)
    vs = ["# Create Member Loads - Concentrated"]
    if isempty(df_member_loads)
        return ""
    end

    for case_group in groupby(df_member_loads, :Case)
        case_num = case_group.Case[1]
        
        # Identify columns
        force_cols = [n for n in names(df_member_loads) if contains(lowercase(n), "force")]
        
        for load_group in groupby(case_group, intersect(vcat([:Axes, :Units, Symbol("Position m or pct")], force_cols), names(case_group)))
            members = join(unique(load_group.Member), ",")
            
            pos = load_group[1, Symbol("Position m or pct")]
            is_relative = load_group[1, :Units] == "Percent"
            if is_relative
                pos /= 100
            end
            
            forces = [("X Force", "GLOBAL_X_OR_USER_DEFINED_U_TRUE"), 
                      ("Y Force", "GLOBAL_Y_OR_USER_DEFINED_V_TRUE"), 
                      ("Z Force", "GLOBAL_Z_OR_USER_DEFINED_W_TRUE")]
            
            for (prefix, dir) in forces
                col_name = findfirst(n -> contains(n, prefix), names(df_member_loads))
                if col_name !== nothing
                    val = load_group[1, col_name] * 1000
                    if val != 0
                        load_id = get!(load_case_counters, case_num, 0) + 1
                        load_case_counters[case_num] = load_id
                        push!(vs, "MemberLoad.Force($load_id, $case_num, \"$members\", " *
                                  "load_distribution=MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1, " *
                                  "load_direction=MemberLoadDirection.LOAD_DIRECTION_$dir" *
                                  ", load_parameter=[$(is_relative ? "True" : "False"), $val, $pos])")
                    end
                end
            end
        end
    end
    push!(vs, "\n")
    return join(vs, "\n")
end

export fWritePyScript
function fWritePyScript(sg_db_source_filepathname)

    if endswith(lowercase(sg_db_source_filepathname), ".mdb") || endswith(lowercase(sg_db_source_filepathname), ".accdb")
        statement = "Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=" * sg_db_source_filepathname
        dbconn = ODBC.Connection(statement)
    elseif endswith(lowercase(sg_db_source_filepathname), ".db") || endswith(lowercase(sg_db_source_filepathname), ".sqlite")
        dbconn = SQLite.DB(sg_db_source_filepathname)
    else
        error("Unsupported database format or file extension: $sg_db_source_filepathname")
    end

    header = "import sys\n"
    header *= "sys.path.append(r'C:\\Users\\j0sua\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages')\n"
    header *= "from RFEM.initModel import Model\n"
    header *= "from RFEM.BasicObjects.material import Material\n"
    header *= "from RFEM.BasicObjects.crossSection import CrossSection\n"
    header *= "from RFEM.BasicObjects.node import Node\n"
    header *= "from RFEM.BasicObjects.line import Line\n"
    header *= "from RFEM.BasicObjects.member import Member\n"
    header *= "from RFEM.TypesForNodes.nodalSupport import NodalSupport\n"
    header *= "from RFEM.TypesForMembers.memberHinge import MemberHinge\n"
    header *= "from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings\n"
    header *= "from RFEM.LoadCasesAndCombinations.loadCase import LoadCase\n"
    header *= "from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation\n"
    header *= "from RFEM.LoadCasesAndCombinations.loadCombination import LoadCombination\n"
    header *= "from RFEM.Loads.nodalLoad import NodalLoad\n"
    header *= "from RFEM.Loads.memberLoad import MemberLoad\n"
    header *= "from RFEM.enums import *\n"
    header *= "from RFEM.dataTypes import inf\n\n"
    header *= "model = Model(new_model=False, model_name=\"\", delete_all=True)\n\n"

    # Set global model settings:
    pyscript = [header, set_global_model_settings()]


    # MATERILS PROPERTIES QUERY
    query_matprop = DBInterface.execute(dbconn, "SELECT * FROM `Material Properties`")
    df_matprop = normalize_sg_dataframe!(DataFrame(query_matprop))
    vMatNames = df_matprop[:, 2]

    push!(pyscript, create_materials(vMatNames))

    # CREATE SECTIONS
    query_secprop = DBInterface.execute(dbconn, "SELECT * FROM `Section Properties`")
    df_secprop = normalize_sg_dataframe!(DataFrame(query_secprop))

    query_members = DBInterface.execute(dbconn, "SELECT * FROM Members")
    df_members = normalize_sg_dataframe!(DataFrame(query_members))


    push!(pyscript, create_sections(df_secprop, df_members))


    # CREATE NODES
    query_nodes = DBInterface.execute(dbconn, "SELECT * FROM Nodes")
    df_nodes = normalize_sg_dataframe!(DataFrame(query_nodes))

    push!(pyscript, create_nodes(df_nodes))


    # CREATE UNIQUE HINGES



    # parse_hinge(df_members[43,:])
    hinges = get_unique_hinges(df_members)
    push!(pyscript, create_hinges(hinges))

    # CREATE MEMBERS
    push!(pyscript, create_beam(df_members, parse_dir_angle(df_members, df_nodes)))


    # CREATE NODAL RESTRAITNS

    # Using the check:
    table_name = "Node Restraints"
    if table_exists(dbconn, table_name)
        query_nodal_restraints = DBInterface.execute(dbconn, "SELECT * FROM `$table_name`")
        df_node_restraints = DataFrame(query_nodal_restraints)
        push!(pyscript, create_nodal_supports(df_node_restraints))

    end


    # CREATE ANALYSIS SETTINGS
    push!(pyscript, create_analysis_settings())

    # CREATE LOAD CASE TITLES
    df_lc_titles = normalize_sg_dataframe!(DataFrame(DBInterface.execute(dbconn, "SELECT * FROM `Load Case Titles`")))
    df_LC_table = normalize_sg_dataframe!(DataFrame(DBInterface.execute(dbconn, "SELECT * FROM `Combination Load Cases`")))

    push!(pyscript, create_primary_loadcase_titles(df_lc_titles, df_LC_table))


    # CREATE DESIGN SITUATIONS
    push!(pyscript, create_design_situations())

    # CAREAT LOAD COMBINATIONS TABLE  
    push!(pyscript, create_load_combinations(df_lc_titles, df_LC_table))


    # CREATE NODAL LOADS
    table_name = "Node Loads"
    if table_exists(dbconn, table_name)
        query_nodal_loads = DBInterface.execute(dbconn, "SELECT * FROM `$table_name`")
        df_nodal_loads = normalize_sg_dataframe!(DataFrame(query_nodal_loads))
        push!(pyscript, create_nodal_loads(df_nodal_loads))
    end



    # CREATE MEMBER LOADS - CONCENTRATED
    table_name = "Member Concentrated Loads"
    if table_exists(dbconn, table_name)
        df_member_loads = normalize_sg_dataframe!(DataFrame(DBInterface.execute(dbconn, "SELECT * FROM `$table_name`")))
        push!(pyscript, create_member_load_concentrated(df_member_loads))
    end


    # CREATE MEMBER LOADS - DISTRIBUTED
    table_name = "Member Distributed Forces"
    if table_exists(dbconn, table_name)
        df_member_forces = normalize_sg_dataframe!(DataFrame(DBInterface.execute(dbconn, "SELECT * FROM `$table_name`")))
        push!(pyscript, create_member_load_distributed(df_member_forces))
    end

# write to file
    write("sg2rfem.py", join(pyscript, ""))
    if dbconn isa ODBC.Connection
        ODBC.disconnect!(dbconn)
    end
    return ""
end

end
