module SGtoRFEM

using DataFrames
using LinearAlgebra
using ODBC
# BUILD DICTIONA

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

export set_global_model_settings
function set_global_model_settings()

    # Delete default objects:
    ps = "# Delete default objects:\n"
    ps *= "delete_all()\n\n"

    ps *= "# Set global model settings:\n"
    ps *= "base_data.current_standard_for_combination_wizard = 6546\n"
    ps *= "base_data.current_standard_for_load_wizard = 6231\n"
    ps *= "base_data.current_standard_for_steel_design = 6679\n"
    ps *= "base_data.activate_load_wizards = False\n"
    ps *= "base_data.member_representatives_active = True\n"
    ps *= "base_data.combination_name_according_to_action_category = True\n"
    ps *= "base_data.global_axes_orientation = \"Z upward\"\n"
    ps *= "base_data.local_axes_orientation = \"y upward | x\"\n"
    ps *= "base_data.solids_active = False\n"
    ps *= "base_data.tolerance_for_nodes = 0.000500000023748726\n"
    ps *= "base_data.tolerance_for_lines = 0.000500000023748726\n"
    ps *= "base_data.tolerance_for_surfaces = 0.000500000023748726\n"
    ps *= "base_data.tolerance_for_directions = 0.000500000023748726\n\n"


    return ps
end

export create_materials
function create_materials(vMatName::Vector{String})
    ps = "# Create Materials\n"
    for i in eachindex(vMatName)
        ps *= "materials.create($(i), name=\"$(vMatName[i])\", definition_type=\"E | (G) | ν\")\n"
    end
    ps *= "\n"
    return ps
end

export create_sections
function create_sections(dfSections::DataFrame)
    vs = ["# Create Sections\n"]
    for i in eachrow(dfSections)
        push!(vs, "sections.create_standardized_steel($(i.Section), \"$(i.Name)\")")
    end
    push!(vs, "\n")

    return join(vs, "\n")
end

export create_nodes
function create_nodes(dfNodes::DataFrame)
    vs = ["# Create Nodes\n"]  # Initialize with the header line

    for i in eachrow(dfNodes)
        # Access values in the DataFrameRow `i` directly using indexing
        push!(vs, "nodes.create_standard( $(i[1]), $(i[2]), $(i[3]), $(i[4]))\n")
    end
    push!(vs, "\n")

    return join(vs, "")  # Join all lines into a single string
end

export parse_hinge
function parse_hinge(row::DataFrameRow, ; isStart::Bool=true)

    # Define the release parameters in order
    release_params = [
        "axial_release_n",
        "axial_release_vy",
        "axial_release_vz",
        "moment_release_mt",
        "moment_release_my",
        "moment_release_mz"
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
        push!(_hinges, "member_hinges.create($i," * hinges[i] * ")")
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
        push!(vs, "lines.create_polyline($(i[Symbol("Member")]), \"$(i[Symbol("Node A")]),$(i[Symbol("Node B")])\")")
    end
    push!(vs, "\n")


    push!(vs, "# Create Members ")
    # check IF THERE ARE ANY HINGES
    hinges = get_unique_hinges(dfMemb)

    for (i, r) in enumerate(eachrow(dfMemb))

        vs_row = ["members.create_beam($(r.Member), \"$(r.Section)\", line=\"$(r.Member)\""]

        # check if r has hinge and match hinge number
        start_hinge = parse_hinge(r)
        i_start = findfirst(x -> x == start_hinge, hinges)
        if i_start !== nothing
            push!(vs_row, " member_hinge_start=\"$i_start\"")
        end

        end_hinge = parse_hinge(r, isStart=false)
        i_end = findfirst(x -> x == end_hinge, hinges)
        if i_end !== nothing
            # str_hinge_end = ", member_hinge_end=\"$i_end\"" 
            push!(vs_row, " member_hinge_end=\"$i_end\"")
        end


        # direciton angle 
        push!(vs_row, " rotation_angle=$(rot_angles[i])")

        # join line string + )
        push!(vs, join(vs_row, ",") * ")")

    end
    # push!(vs, ")\n")

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
        s_line = "nodal_supports.create($i, nodes=\"" * join(s, ",") * "\", $(nodal_supports[i]))"
        push!(vs, s_line)
    end
    push!(vs, "\n")
    return join(vs, "\n")
end

export create_analysis_settings
function create_analysis_settings()
    vs = ["# Create Static Analysis Settings", "static_analysis_settings.create(1)", "static_analysis_settings.create(2, analysis_type=\"Second-order (P-Δ)\")"]
    push!(vs, "\n")
    return join(vs, "\n")
end

export create_primary_loadcase_titles
function create_primary_loadcase_titles(df_lc_titles::DataFrame, df_LC_table::DataFrame)
    vs = ["# Create Load Cases"]

    loadcomb_cases = unique(df_LC_table[:, 1])
    filtered_df_lc_titles = filter(row -> !(row.Case in loadcomb_cases), df_lc_titles)

    for r in eachrow(filtered_df_lc_titles)

        push!(vs, "load_cases.create($(r[1]), name=\"$(r[2])\", static_analysis_settings=\"SA1\", to_solve=False)")
    end
    push!(vs, "\n")

    return join(vs, "\n")
end

export create_design_situations
function create_design_situations()
    vs = ["# Create Design Situations"]
    push!(vs, "design_situations.create(1, name=\"ULS - Strength\", design_situation_type=\"DESIGN_SITUATION_TYPE_ULS_STRENGTH_AS_NZS\")")
    push!(vs, "design_situations.create(2, name=\"SLS - Serviceability\", design_situation_type=\"DESIGN_SITUATION_TYPE_SLS_SERVICEABILITY_NZS\")")
    push!(vs, "\n")

    return join(vs, "\n")
end


export create_load_combinations
function create_load_combinations(df_lc_titles::DataFrame, df_LC_table::DataFrame)
    vs = ["# Create Load Combinations Titles"]

    # Iterate over each unique value in the first column
    unique_LC = unique(df_LC_table[:, 1])

    for LComb in unique_LC
        # Filter rows for the current LComb
        subset = filter(x -> x[1] == LComb, df_LC_table)

        # print name
        comb_name = filter(t -> t[1] == LComb, df_lc_titles).Title[1]
        push!(vs, "load_combinations.create($LComb, design_situation=\"DS1\", user_defined_name_enabled=True, name=\"$comb_name\", static_analysis_settings=\"SA2\")")


        # print combination factors
        for (i, row) in enumerate(eachrow(subset))
            # println("Row: Combination=$(row.Combination), Case=$(row.Case), MultiplyingFactor=$(row.MultiplyingFactor)")

            push!(vs, "load_combinations[$LComb].items[$i].load_case=$(row[2])")
            push!(vs, "load_combinations[$LComb].items[$i].factor=$(row[3])")

        end
    end

    push!(vs, "\n")
    return join(vs, "\n")

end

export create_nodal_loads
function create_nodal_loads(df_nodal_loads::DataFrame)
    vs = ["# Create Nodal Loads"]

    if isempty(df_nodal_loads)
        return ""
    end

    # Group by Case number
    for case_group in groupby(df_nodal_loads, :Case)
        case_num = case_group.Case[1]

        # node load item i
        i = 1

        # For each force direction, group nodes with same force value
        # Handle X forces
        x_forces = filter(row -> row[3] != 0.0, case_group)
        if !isempty(x_forces)
            for x_group in groupby(x_forces, Symbol("X Force (kN)"))
                nodes = join(x_group.Node, ",")
                fx = x_group[1, "X Force (kN)"] * 1000  # Convert to N
                push!(vs, "load_cases[$case_num].nodal_loads.create_force($i, \"$nodes\", $fx, load_case=$case_num)")
                i += 1
            end
        end

        # Handle Y forces
        y_forces = filter(row -> row[4] != 0.0, case_group)
        if !isempty(y_forces)
            for y_group in groupby(y_forces, Symbol("Y Force (kN)"))
                nodes = join(y_group.Node, ",")
                fy = y_group[1, "Y Force (kN)"] * 1000  # Convert to N
                push!(vs, "load_cases[$case_num].nodal_loads.create_force($i, \"$nodes\", $fy, load_direction=\"V\", load_case=$case_num)")
                i += 1
            end
        end

        # Handle Z forces
        z_forces = filter(row -> row[5] != 0.0, case_group)
        if !isempty(z_forces)
            for z_group in groupby(z_forces, Symbol("Z Force (kN)"))
                nodes = join(z_group.Node, ",")
                fz = z_group[1, "Z Force (kN)"] * 1000  # Convert to N
                push!(vs, "load_cases[$case_num].nodal_loads.create_force($i, \"$nodes\", $fz, load_direction=\"W\", load_case=$case_num)")
                i += 1
            end
        end
    end

    push!(vs, "\n")
    return join(vs, "\n")
end

# Add this at module level
const load_case_counters = Dict{Int,Int}()

export create_member_load_concentrated
function create_member_load_concentrated(df_member_loads::DataFrame)
    vs = ["# Create Member Loads - Concentrated"]

    if isempty(df_member_loads)
        return ""
    end

    # Group by Case number first
    for case_group in groupby(df_member_loads, :Case)
        case_num = case_group.Case[1]

        # Initialize or get existing counter for this case
        sub_load = get!(load_case_counters, case_num, 0)

        # Group by load pattern (all relevant columns except Member)
        for load_group in groupby(case_group, [:Case, :Axes, :Units, Symbol("Position (m or %)"),
            Symbol("X Force (kN)"), Symbol("Y Force (kN)"), Symbol("Z Force (kN)"),
            Symbol("X Moment (kNm)"), Symbol("Y Moment (kNm)"), Symbol("Z Moment (kNm)")])

            # Collect and join all member numbers for this load pattern
            members = join(sort(unique(load_group.Member)), ",")
            # sub_load = load_group[1, Symbol("Sub Load")]

            # Get force components
            fx = load_group[1, Symbol("X Force (kN)")]
            fy = load_group[1, Symbol("Y Force (kN)")]
            fz = load_group[1, Symbol("Z Force (kN)")]

            # Get moment components
            mx = load_group[1, Symbol("X Moment (kNm)")]
            my = load_group[1, Symbol("Y Moment (kNm)")]
            mz = load_group[1, Symbol("Z Moment (kNm)")]

            # Skip if all loads are zero
            if fx == 0 && fy == 0 && fz == 0 && mx == 0 && my == 0 && mz == 0
                continue
            end

            # Get position and units
            position = load_group[1, Symbol("Position (m or %)")]
            units = load_group[1, :Units]

            # Convert position to decimal if percentage
            is_relative = units == "Percent"
            if is_relative
                position = position / 100
            end

            # Set parameter name based on units
            distance_param = is_relative ? "distance_a_relative" : "distance_a_absolute"

            # Define direction based on coordinate system
            is_local = load_group[1, :Axes] == "Local"
            x_dir = is_local ? "x" : "X_L (U_L )"
            y_dir = is_local ? "y" : "Y_L (V_L )"

            # Create coordinate system parameter
            coord_system = is_local ? ", coordinate_system=\"Local\"" : ""

            # Create force components
            if fx != 0
                load_case_counters[case_num] += 1
                push!(vs, "load_cases[$case_num].member_loads.create_force($(load_case_counters[case_num]), \"$members\", " *
                          "\"Concentrated - 1\", load_case=$case_num" *
                          coord_system *
                          ", load_direction=\"$x_dir\"" *
                          ", magnitude=$(fx * 1000)" *
                          ", distance_a_is_defined_as_relative=$(is_relative ? "True" : "False")" *
                          ", $distance_param=$position" *
                          ")")
            end

            if fy != 0
                load_case_counters[case_num] += 1
                push!(vs, "load_cases[$case_num].member_loads.create_force($(load_case_counters[case_num]), \"$members\", " *
                          "\"Concentrated - 1\", load_case=$case_num" *
                          coord_system *
                          ", load_direction=\"$y_dir\"" *
                          ", magnitude=$(fy * 1000)" *
                          ", distance_a_is_defined_as_relative=$(is_relative ? "True" : "False")" *
                          ", $distance_param=$position" *
                          ")")
            end

            if fz != 0
                load_case_counters[case_num] += 1
                push!(vs, "load_cases[$case_num].member_loads.create_force($(load_case_counters[case_num]), \"$members\", " *
                          "\"Concentrated - 1\", load_case=$case_num, " *
                          "magnitude=$(fz * 1000), " *
                          "distance_a_is_defined_as_relative=$(is_relative ? "True" : "False"), " *
                          "$distance_param=$position" * ")")
            end

            # Create moment components
            if mx != 0
                load_case_counters[case_num] += 1
                push!(vs, "load_cases[$case_num].member_loads.create_moment($(load_case_counters[case_num]), \"$members\", " *
                          "\"Concentrated - 1\", load_case=$case_num" *
                          coord_system *
                          ", load_direction=\"$x_dir\"" *
                          ", magnitude=$(mx * 1000)" *
                          ", distance_a_is_defined_as_relative=$(is_relative ? "True" : "False")" *
                          ", $distance_param=$position" *
                          ")")
            end

            if my != 0
                load_case_counters[case_num] += 1
                push!(vs, "load_cases[$case_num].member_loads.create_moment($(load_case_counters[case_num]), \"$members\", " *
                          "\"Concentrated - 1\", load_case=$case_num" *
                          coord_system *
                          ", load_direction=\"$y_dir\"" *
                          ", magnitude=$(my * 1000)" *
                          ", distance_a_is_defined_as_relative=$(is_relative ? "True" : "False")" *
                          ", $distance_param=$position" *
                          ")")
            end

            if mz != 0
                load_case_counters[case_num] += 1
                push!(vs, "load_cases[$case_num].member_loads.create_moment($(load_case_counters[case_num]), \"$members\", " *
                          "\"Concentrated - 1\", load_case=$case_num, " *
                          "magnitude=$(mz * 1000), " *
                          "distance_a_is_defined_as_relative=$(is_relative ? "True" : "False"), " *
                          "$distance_param=$position)")
            end
        end
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

            # Set coordinate system based on Axes
            coord_system = ""
            if load_group[1, :Axes] == "Local"
                coord_system = ", coordinate_system=\"Local\""

                directions = [
                    ("x", "Start X Force (kN/m)", "Finish X Force (kN/m)"),
                    ("y", "Start Y Force (kN/m)", "Finish Y Force (kN/m)"),
                    ("z", "Start Z Force (kN/m)", "Finish Z Force (kN/m)")
                ]
            else
                # Process each direction (X, Y, Z)
                if load_group[1, :Axes] == "G-Proj"
                    directions = [
                        ("X_P (U_P )", "Start X Force (kN/m)", "Finish X Force (kN/m)"),
                        ("Y_P (V_P )", "Start Y Force (kN/m)", "Finish Y Force (kN/m)"),
                        ("Z_P (W_P )", "Start Z Force (kN/m)", "Finish Z Force (kN/m)")
                    ]
                else
                    directions = [
                        ("X_L (U_L )", "Start X Force (kN/m)", "Finish X Force (kN/m)"),
                        ("Y_L (V_L )", "Start Y Force (kN/m)", "Finish Y Force (kN/m)"),
                        ("Z_L (W_L )", "Start Z Force (kN/m)", "Finish Z Force (kN/m)")
                    ]
                end
            end



            for (dir, start_col, end_col) in directions
                start_force = load_group[1, Symbol(start_col)]
                end_force = load_group[1, Symbol(end_col)]


                if start_force != 0 || end_force != 0
                    load_case_counters[case_num] += 1
                    push!(vs, "load_cases[$case_num].member_loads.create_force($(load_case_counters[case_num]), \"$members\", " *
                              "\"Trapezoidal\", " *
                              "load_case=$case_num" *
                              coord_system *
                              ", load_direction=\"$dir\"" *
                              ", magnitude_1=$(start_force * 1000)" *
                              ", magnitude_2=$(end_force * 1000)" *
                              ", distance_a_is_defined_as_relative=$(is_relative ? "True" : "False")" *
                              ", $distance_param_a=$start_pos" *
                              ", distance_b_is_defined_as_relative=$(is_relative ? "True" : "False")" *
                              ", $distance_param_b=$end_pos" *
                              ")")
                end
            end
        end
    end

    push!(vs, "\n")
    return join(vs, "\n")
end


export fWritePyScript
function fWritePyScript(sg_db_source_filepathname)

    statement = "Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=" * sg_db_source_filepathname
    dbconn = ODBC.Connection(statement)

    # Set global model settings:
    pyscript = [set_global_model_settings()]


    # MATERILS PROPERTIES QUERY
    query_matprop = DBInterface.execute(dbconn, "SELECT * FROM `Material Properties`")
    df_matprop = DataFrame(query_matprop)
    vMatNames = df_matprop[:, 2]

    push!(pyscript, create_materials(vMatNames))

    # CREATE SECTIONS
    query_secprop = DBInterface.execute(dbconn, "SELECT * FROM `Section Properties`")
    df_secprop = DataFrame(query_secprop)

    push!(pyscript, create_sections(df_secprop))


    # CREATE NODES
    query_nodes = DBInterface.execute(dbconn, "SELECT * FROM Nodes")
    df_nodes = DataFrame(query_nodes)

    push!(pyscript, create_nodes(df_nodes))


    # CREATE UNIQUE HINGES
    query_members = DBInterface.execute(dbconn, "SELECT * FROM Members")
    df_members = DataFrame(query_members)


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
    df_lc_titles = DataFrame(DBInterface.execute(dbconn, "SELECT * FROM `Load Case Titles`"))
    df_LC_table = DataFrame(DBInterface.execute(dbconn, "SELECT * FROM `Combination Load Cases`"))

    push!(pyscript, create_primary_loadcase_titles(df_lc_titles, df_LC_table))


    # CREATE DESIGN SITUATIONS
    push!(pyscript, create_design_situations())

    # CAREAT LOAD COMBINATIONS TABLE  
    push!(pyscript, create_load_combinations(df_lc_titles, df_LC_table))


    # CREATE NODAL LOADS
    table_name = "Node Loads"
    if table_exists(dbconn, table_name)
        query_nodal_loads = DBInterface.execute(dbconn, "SELECT * FROM `$table_name`")
        df_nodal_loads = DataFrame(query_nodal_loads)
        push!(pyscript, create_nodal_loads(df_nodal_loads))
    end



    # CREATE MEMBER LOADS - CONCENTRATED
    table_name = "Member Concentrated Loads"
    if table_exists(dbconn, table_name)
        df_member_loads = DataFrame(DBInterface.execute(dbconn, "SELECT * FROM `$table_name`"))
        push!(pyscript, create_member_load_concentrated(df_member_loads))
    end


    # CREATE MEMBER LOADS - DISTRIBUTED
    table_name = "Member Distributed Forces"
    if table_exists(dbconn, table_name)
        df_member_forces = DataFrame(DBInterface.execute(dbconn, "SELECT * FROM `$table_name`"))
        push!(pyscript, create_member_load_distributed(df_member_forces))
    end

    # write to file

    write("sg2rfem.py", join(pyscript, ""))
    ODBC.disconnect!(dbconn)
    return ""
end



end # module SGtoRFEM
