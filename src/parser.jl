# =============================================================================
# SGtoRFEM - Parser Module
# =============================================================================
# Parses Space GASS text export format (.txt) into structured data.
# Format: https://spacegass.com/help/export-format/
# =============================================================================

"""
    parse_sg_file(filepath::String) -> SGModel

Main entry point. Reads a Space GASS export file and returns structured data.
"""
function parse_sg_file(filepath::String)
    model = SGModel(
        Dict{Int,SGNode}(),
        Dict{Int,SGMember}(),
        Dict{Int,SGSection}(),
        Dict{Int,SGMaterial}(),
        SGNodalLoad[],
        SGLoadCase[],
        SGConstraint[],
        Dict{Int,NTuple{6,Float64}}(),  # offsets
        "",                              # title
        Dict{Symbol,String}()            # units
    )

    current_section = ""
    cont_buf = String[]
    in_cont = false

    open(filepath, "r") do io
        while !eof(io)
            raw = readline(io)
            line = strip(raw)

            # Continuation handling
            if in_cont
                line = strip(line, '&')
                push!(cont_buf, line)
                if !endswith(raw, '&')
                    combined = join(cont_buf, " ")
                    process_line(model, current_section, combined)
                    in_cont = false; empty!(cont_buf)
                end
                continue
            end

            if endswith(line, '&')
                in_cont = true
                line = strip(line, '&')
                push!(cont_buf, line)
                continue
            end

            # Skip blanks and comments
            isempty(line) || startswith(line, '#') && continue

            # Section header?
            if is_section_header(line)
                current_section = uppercase(line)
                continue
            end

            process_line(model, current_section, line)
        end
    end
    return model
end

"""
    is_section_header(line::String) -> Bool
"""
function is_section_header(line::String)
    occursin(",", line) && return false
    occursin(" ", line) && return false
    all(isuppercase, line) || return false
    return true
end

"""
    process_line(model, section, line)
"""
function process_line(model::SGModel, section::String, line::String)
    case section
        "UNITS"       => parse_units!(model, line)
        "NODES"       => parse_node!(model, line)
        "MEMBERS"     => parse_member!(model, line)
        "SECTIONS"    => parse_section!(model, line)
        "MATERIALS"   => parse_material!(model, line)
        "CONSTRAINTS" => parse_constraint!(model, line)
        "OFFSETS"     => parse_offset!(model, line)
        "NODELOADS"   => parse_nodal_load!(model, line)
        "MEMBCONC"    => parse_member_conn!(model, line)
        "MEMBFORCES"  => parse_member_force!(model, line)
        "SELFWEIGHT"  => parse_selfweight!(model, line)
        "LUMPEDMASS"  => parse_lumped_mass!(model, line)
        "COMBINATIONS"=> parse_combination!(model, line)
        "TITLES"      => (model.title = strip(line, '"'))
        _             => nothing
    end
end

# =============================================================================
# INDIVIDUAL SECTION PARSERS
# =============================================================================

function parse_units!(model::SGModel, line::String)
    for part in split(line)[2:end]
        if occursin(":", part)
            kv = split(part, ":"); length(kv)==2 || continue
            model.units[Symbol(lowercase(strip(kv[1])))] = strip(kv[2])
        end
    end
end

function parse_node!(model::SGModel, line::String)
    f = split(line, ","); length(f) >= 4 || return
    try
        id = parse(Int,   strip(f[1]))
        x  = parse(Float64,strip(f[2]))
        y  = parse(Float64,strip(f[3]))
        z  = parse(Float64,strip(f[4]))
        model.nodes[id] = SGNode(id, x, y, z)
    catch; end
end

function parse_member!(model::SGModel, line::String)
    f = split(line, ","); length(f) < 10 && return
    try
        id     = parse(Int,   strip(f[1]))
        beta   = parse(Float64,strip(f[2]))
        dirfld = strip(f[4])

        if occursin(",", dirfld)
            dp = split(dirfld, ",")
            axis_dir = only(strip(dp[1]))
            endcode  = length(dp) > 1 ? only(strip(dp[2])) : 'N'
        else
            axis_dir = only(dirfld); endcode = 'N'
        end

        startn = parse(Int, strip(f[5]))
        endn   = parse(Int, strip(f[6]))
        sect   = parse(Int, strip(f[7]))
        mat    = parse(Int, strip(f[8]))
        c1 = length(f) > 9  ? strip(f[9])  : "FFFFFF"
        c2 = length(f) > 10 ? strip(f[10]) : "FFFFFF"

        # releases (6 values, default 0)
        rfx_i = length(f) > 10 ? parse(Float64,strip(f[11])) : 0.0
        rfy_i = length(f) > 11 ? parse(Float64,strip(f[12])) : 0.0
        rfz_i = length(f) > 12 ? parse(Float64,strip(f[13])) : 0.0
        rm_i  = length(f) > 13 ? parse(Float64,strip(f[14])) : 0.0
        rfx_j = length(f) > 14 ? parse(Float64,strip(f[15])) : 0.0
        rfy_j = length(f) > 15 ? parse(Float64,strip(f[16])) : 0.0

        fix_i = (rfx_i, rfy_i, rfz_i, rm_i, 0.0, 0.0)
        fix_j = (rfx_j, rfy_j, 0.0,    0.0, 0.0, 0.0)

        model.members[id] = SGMember(
            id, startn, endn, sect, mat,
            beta, axis_dir, endcode,
            c1, c2, fix_i, fix_j,
            (0.0,0.0,0.0)
        )
    catch; end
end

function parse_section!(model::SGModel, line::String)
    f = split(line, ","); length(f) < 6 && return
    try
        sid = parse(Int, strip(f[1]))

        if haskey(model.sections, sid)
            # Row 2 – update dims
            sec = model.sections[sid]
            depth = length(f) > 2 ? parse(Float64,strip(f[3])) : sec.depth
            fw    = length(f) > 4 ? parse(Float64,strip(f[5])) : sec.flange_width
            rr    = length(f) > 5 ? parse(Float64,strip(f[6])) : sec.root_radius
            model.sections[sid] = SGSection(sec.id, sec.description, sec.material,
                sec.profile, sec.area, sec.iy, sec.iz, sec.j, depth, fw, rr)
            return
        end

        # Row 1 – primary props
        desc = strip(f[2], '"')
        mat  = strip(f[3], '"')
        prof = strip(f[4], '"')
        A    = parse(Float64, strip(f[5]))
        Iy   = parse(Float64, strip(f[6]))
        Iz   = parse(Float64, strip(f[7]))
        J    = parse(Float64, strip(f[8]))

        sec = SGSection(sid, desc, mat, prof, A, Iy, Iz, J, 0.0, 0.0, 0.0)
        model.sections[sid] = sec
    catch; end
end

function parse_material!(model::SGModel, line::String)
    f = split(line, ","); length(f) >= 8 || return
    try
        id   = parse(Int,    strip(f[1]))
        name = strip(f[2], '"')
        std  = strip(f[3], '"')
        E    = parse(Float64, strip(f[4]))
        ν    = parse(Float64, strip(f[5]))
        ρ    = parse(Float64, strip(f[6]))
        α    = parse(Float64, strip(f[7]))
        fy   = parse(Float64, strip(f[8]))
        model.materials[id] = SGMaterial(id, name, std, E, ν, ρ, α, fy)
    catch; end
end

function parse_constraint!(model::SGModel, line::String)
    f = split(line, ","); length(f) >= 3 || return
    try
        nid = parse(Int, strip(f[2]))
        code = strip(f[3])
        push!(model.constraints, SGConstraint(nid, code))
    catch; end
end

function parse_offset!(model::SGModel, line::String)
    f = split(line, ","); length(f) >= 8 || return
    try
        mid = parse(Int,    strip(f[1]))
        dx1 = parse(Float64,strip(f[3]))
        dy1 = parse(Float64,strip(f[4]))
        dz1 = parse(Float64,strip(f[5]))
        dx2 = parse(Float64,strip(f[6]))
        dy2 = parse(Float64,strip(f[7]))
        dz2 = parse(Float64,strip(f[8]))
        model.offsets[mid] = (dx1, dy1, dz1, dx2, dy2, dz2)
    catch; end
end

function parse_nodal_load!(model::SGModel, line::String)
    f = split(line, ","); length(f) >= 9 || return
    try
        lc   = parse(Int,    strip(f[1]))
        nid  = parse(Int,    strip(f[2]))
        fx   = parse(Float64,strip(f[3]))
        fy   = parse(Float64,strip(f[4]))
        fz   = parse(Float64,strip(f[5]))
        mx   = parse(Float64,strip(f[6]))
        my   = parse(Float64,strip(f[7]))
        mz   = parse(Float64,strip(f[8]))
        lcat = parse(Int,    strip(f[9]))
        push!(model.nodal_loads, SGNodalLoad(lc, nid, fx, fy, fz, mx, my, mz, lcat))
    catch; end
end

# Placeholder parsers for less-critical sections
parse_member_conn!(_m::SGModel, _l::String) = nothing
parse_member_force!(_m::SGModel, _l::String) = nothing
parse_selfweight!   (_m::SGModel, _l::String) = nothing
parse_lumped_mass!  (_m::SGModel, _l::String) = nothing
parse_combination!  (_m::SGModel, _l::String) = nothing

end # module SGtoRFEM.Parser
