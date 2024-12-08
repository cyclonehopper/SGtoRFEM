module SGtoRFEM

using DataFrames

# BUILD DICTIONA

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

function parse_dir_angle(dfMemb::DataFrame)

end

export create_beam
function create_beam(dfMemb::DataFrame)
    vs = ["# Create Lines\n"]
    for i in eachrow(dfMemb)
        push!(vs, "lines.create_polyline($(i[Symbol("Member")]), \"$(i[Symbol("Node A")]),$(i[Symbol("Node B")])\")")
    end
    push!(vs, "\n")


    push!(vs, "# Create Members ")
    # check IF THERE ARE ANY HINGES
    hinges = get_unique_hinges(dfMemb)

    for r in eachrow(dfMemb)

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


        # check if has direciton angle
        if r[2] > 0.00
            push!(vs_row, " rotation_angle=$(r[2]*π/180)")
        end


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


end # module SGtoRFEM
