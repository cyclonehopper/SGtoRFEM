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
        Dict{Symbol,String}(),           # units
        Dict{Symbol,Int}(),              # section parser state
        SGMembConc[],                    # member concentrated loads
        SGMembForce[]                    # member distributed loads
    )

    current_section = ""
    cont_buf = String[]
    in_cont = false

    open(filepath, "r") do io
        while !Base.eof(io)
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
function is_section_header(line::AbstractString)
    occursin(",", line) && return false
    occursin(" ", line) && return false
    all(isuppercase, line) || return false
    return true
end

"""
    process_line(model, section, line)
"""
function process_line(model::SGModel, section::String, line::AbstractString)
    if     section == "UNITS";        parse_units!(model, line)
    elseif section == "NODES";        parse_node!(model, line)
    elseif section == "MEMBERS";      parse_member!(model, line)
    elseif section == "SECTIONS";     parse_section!(model, line)
    elseif section == "MATERIALS";    parse_material!(model, line)
    elseif section == "CONSTRAINTS";  parse_constraint!(model, line)
    elseif section == "OFFSETS";      parse_offset!(model, line)
    elseif section == "NODELOADS";    parse_nodal_load!(model, line)
    elseif section == "MEMBCONC";     parse_member_conn!(model, line)
    elseif section == "MEMBFORCES";   parse_member_force!(model, line)
    elseif section == "SELFWEIGHT";   parse_selfweight!(model, line)
    elseif section == "LUMPEDMASS";   parse_lumped_mass!(model, line)
    elseif section == "COMBINATIONS"; parse_combination!(model, line)
    elseif section == "TITLES";       model.title = strip(line, '"')
    end # unknown sections are ignored
end

# =============================================================================
# INDIVIDUAL SECTION PARSERS
# =============================================================================

function parse_units!(model::SGModel, line::AbstractString)
    for part in split(line)[2:end]
        if occursin(":", part)
            kv = split(part, ":"); length(kv)==2 || continue
            model.units[Symbol(lowercase(strip(kv[1])))] = strip(kv[2])
        end
    end
end

function parse_node!(model::SGModel, line::AbstractString)
    f = split(line, ","); length(f) >= 4 || return
    try
        id = parse(Int,   strip(f[1]))
        x  = parse(Float64,strip(f[2]))
        y  = parse(Float64,strip(f[3]))
        z  = parse(Float64,strip(f[4]))
        model.nodes[id] = SGNode(id, x, y, z)
    catch; end
end

function parse_member!(model::SGModel, line::AbstractString)
    f = split(line, ","); length(f) < 10 && return
    try
        id     = parse(Int,   strip(f[1]))
        beta   = parse(Float64,strip(f[2]))
        dirfld = strip(f[4])

        # Layout A: "...,<axis>,<endcode>,<start>,..."  (Space GASS native)
        # Layout B: "...,\"<axis,endcode>\",<start>,..." (legacy/combined)
        if occursin(",", dirfld)
            dp = split(dirfld, ",")
            axis_dir = isempty(strip(dp[1])) ? ' ' : only(strip(dp[1]))
            endcode  = length(dp) > 1 ? only(strip(dp[2])) : 'N'
            off = 0
        elseif tryparse(Int, strip(f[5])) !== nothing
            axis_dir = isempty(dirfld) ? ' ' : only(dirfld)
            endcode  = 'N'
            off = 0
        else
            axis_dir = isempty(dirfld) ? ' ' : only(dirfld)
            endcode  = isempty(strip(f[5])) ? 'N' : only(strip(f[5]))
            off = 1
        end

        startn = parse(Int, strip(f[5+off]))
        endn   = parse(Int, strip(f[6+off]))
        sect   = parse(Int, strip(f[7+off]))
        mat    = parse(Int, strip(f[8+off]))
        c1 = length(f) > 9+off  ? strip(f[9+off])  : "FFFFFF"
        c2 = length(f) > 10+off ? strip(f[10+off]) : "FFFFFF"

        # releases (default 0)
        rel(i) = length(f) >= 11+off+i ? tryparse(Float64, strip(f[10+off+i])) : nothing
        rv(i)  = (r = rel(i); r === nothing ? 0.0 : r)

        fix_i = (rv(1), rv(2), rv(3), rv(4), 0.0, 0.0)
        fix_j = (rv(5), rv(6), 0.0, 0.0, 0.0, 0.0)

        model.members[id] = SGMember(
            id, startn, endn, sect, mat,
            beta, axis_dir, endcode,
            c1, c2, fix_i, fix_j,
            (0.0,0.0,0.0)
        )
    catch e
        @debug "member line not parsed" line e
    end
end

function parse_section!(model::SGModel, line::AbstractString)
    f = split(line, ",")

    # Row 1 always carries a quoted description; unquoted rows are the
    # geometry/dimension continuation of the previously seen section.
    if !occursin('"', line)
        length(f) >= 10 || return
        sid = get(model.section_state, :last, 0)
        sec = sid == 0 ? nothing : get(model.sections, sid, nothing)
        sec === nothing && return
        try
            # Layout (verified vs Space GASS export):
            #   f1=shape code (7=I, 4=CHS, 5=SHS, 12=L), f3=depth, f4=width,
            #   f8=tf, f10=tw, f12=root radius
            depth = parse(Float64, strip(f[3]))
            fw    = parse(Float64, strip(f[4]))
            tf    = parse(Float64, strip(f[8]))
            tw    = parse(Float64, strip(f[10]))
            rr    = length(f) >= 12 ? parse(Float64, strip(f[12])) : 0.0
            model.sections[sid] = SGSection(sec.id, sec.description, sec.material_name,
                sec.profile, sec.area, sec.iy, sec.iz, sec.j,
                max(depth, sec.depth), max(fw, sec.flange_width),
                max(rr, sec.root_radius), max(tw, sec.thickness_web),
                max(tf, sec.thickness_flange))
        catch; end
        return
    end

    length(f) < 6 && return
    try
        sid = parse(Int, strip(f[1]))
        sid <= 0 && return   # filler/continuation rows use id 0

        # Row 1 – primary props
        desc = strip(f[2], '"')
        mat  = strip(f[3], '"')
        prof = strip(f[4], '"')
        A    = parse(Float64, strip(f[5]))
        Iy   = parse(Float64, strip(f[6]))
        Iz   = parse(Float64, strip(f[7]))
        J    = parse(Float64, strip(f[8]))

        sec = SGSection(sid, desc, mat, prof, A, Iy, Iz, J, 0.0, 0.0, 0.0, 0.0, 0.0)
        model.sections[sid] = sec
        model.section_state[:last] = sid
    catch; end
end

function parse_material!(model::SGModel, line::AbstractString)
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

function parse_constraint!(model::SGModel, line::AbstractString)
    f = split(line, ","); length(f) >= 3 || return
    try
        nid = parse(Int, strip(f[2]))
        code = strip(f[3])
        push!(model.constraints, SGConstraint(nid, code))
    catch; end
end

function parse_offset!(model::SGModel, line::AbstractString)
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

function parse_nodal_load!(model::SGModel, line::AbstractString)
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
# Member concentrated loads (MEMBCONC)
# Layout: lc, member, loadno, axis(G|L|A), spec(A=absolute | %=relative),
#         a, Fx, Fy, Fz, Mx, My, Mz [, cat]
function parse_member_conn!(model::SGModel, line::AbstractString)
    f = split(line, ","); length(f) < 13 && return
    try
        lc  = parse(Int, strip(f[1]))
        mem = parse(Int, strip(f[2]))
        axis = uppercase(strip(f[4])[1])
        relative = occursin("%", strip(uppercase(f[5])))
        num(i) = (v = tryparse(Float64, strip(f[i])); v === nothing ? 0.0 : v)
        push!(model.member_concs, SGMembConc(lc, mem, axis, relative,
            num(6), num(7), num(8), num(9), num(10), num(11), num(12)))
    catch; end
end

# Member distributed loads (MEMBFORCES) – one trapezoidal piece per row.
# Layout: lc, member, slot, axis(G|L|A), spec(%|A), a, b,
#         fx1, fx2, fy1, fy2, fz1, fz2 [, cat]
function parse_member_force!(model::SGModel, line::AbstractString)
    f = split(line, ","); length(f) < 14 && return
    try
        lc  = parse(Int, strip(f[1]))
        mem = parse(Int, strip(f[2]))
        axis = uppercase(strip(f[4])[1])
        relative = occursin("%", strip(uppercase(f[5])))
        num(i) = (v = tryparse(Float64, strip(f[i])); v === nothing ? 0.0 : v)
        push!(model.member_forces, SGMembForce(lc, mem, axis, relative,
            num(6), num(7),
            num(8), num(9), num(10), num(11), num(12), num(13)))
    catch; end
end
parse_selfweight!(_m::SGModel, _l::AbstractString) = nothing
parse_lumped_mass!(_m::SGModel, _l::AbstractString) = nothing
parse_combination!(_m::SGModel, _l::AbstractString) = nothing
