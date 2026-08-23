module SGtoRFEM

# =============================================================================
# SGtoRFEM -- Space GASS to Dlubal RFEM Converter
# =============================================================================
# Architecture:
#   Parser    – reads SG .TXT and populates an SGModel
#   Converter – maps SG types to RFEM representation (RFEMModel)
#   Writer    – generates RFEM XML project file from RFEMModel (via template)
# =============================================================================

# -------------------------- Public API ---------------------------------
export parse_sg_file, convert_to_rfem, generate_rfem_xml,
       SGModel, SGNode, SGMember, SGSection, SGMaterial, SGNodalLoad,
       SGLoadCase, SGConstraint, SGMembConc, SGMembForce, find_child

# -------------------------- SG Data Structures ----------------------------------
struct SGNode
    id  ::Int
    x   ::Float64
    y   ::Float64
    z   ::Float64
end

struct SGMember
    id            ::Int
    start_node    ::Int
    end_node      ::Int
    section_id    ::Int
    material_id   ::Int
    beta_angle    ::Float64
    axis_dir      ::Char
    endcode       ::Char
    color1        ::String
    color2        ::String
    fix_i         ::NTuple{6,Float64}
    fix_j         ::NTuple{6,Float64}
    e_perp        ::NTuple{3,Float64}
end

struct SGSection
    id            ::Int
    description   ::String
    material_name ::String
    profile       ::String
    area          ::Float64
    iy            ::Float64
    iz            ::Float64
    j             ::Float64
    depth         ::Float64    # from second row (mm)
    flange_width  ::Float64    # from second row (mm)
    root_radius   ::Float64    # from second row (mm)
    thickness_web ::Float64    # from second row (mm)
    thickness_flange ::Float64 # from second row (mm)
end

struct SGMaterial
    id        ::Int
    name      ::String
    standard  ::String
    E        ::Float64      # MPa
    ν        ::Float64
    density  ::Float64      # t/m^3
    α        ::Float64
    fy       ::Float64      # MPa
end

struct SGNodalLoad
    load_case    ::Int
    node_id      ::Int
    fx           ::Float64
    fy           ::Float64
    fz           ::Float64
    mx           ::Float64
    my           ::Float64
    mz           ::Float64
    load_category::Int
end

struct SGLoadCase
    id     ::Int
    name   ::String
    factor ::Float64
end

struct SGConstraint
    node_id ::Int
    code    ::String
end

# Member concentrated load (MEMBCONC):
#   lc, member, axis ('G' global / 'L' local / 'A' projected),
#   spec ('A' absolute metres / '%' relative), distance a,
#   force (fx,fy,fz), moment (mx,my,mz)
struct SGMembConc
    lc       ::Int
    member   ::Int
    axis     ::Char
    relative ::Bool
    a        ::Float64
    fx ::Float64; fy ::Float64; fz ::Float64
    mx ::Float64; my ::Float64; mz ::Float64
end

struct SGMembForce
    lc       ::Int
    member   ::Int
    axis     ::Char
    relative ::Bool
    a        ::Float64
    b        ::Float64
    fx1::Float64; fx2::Float64
    fy1::Float64; fy2::Float64
    fz1::Float64; fz2::Float64
end

# Load combination factor row (COMBINATIONS): combination no, load case, factor
struct SGCombo
    no    ::Int
    lc_no ::Int
    factor::Float64
end

mutable struct SGModel
    nodes          ::Dict{Int,SGNode}
    members        ::Dict{Int,SGMember}
    sections       ::Dict{Int,SGSection}
    materials      ::Dict{Int,SGMaterial}
    nodal_loads    ::Vector{SGNodalLoad}
    load_cases     ::Vector{SGLoadCase}
    constraints    ::Vector{SGConstraint}
    offsets        ::Dict{Int,NTuple{6,Float64}}
    title          ::String
    units          ::Dict{Symbol,String}
    section_state  ::Dict{Symbol,Int}   # parser scratch state
    member_concs   ::Vector{SGMembConc}
    member_forces  ::Vector{SGMembForce}
    load_titles    ::Dict{Int,String}   # TITLES: case/combination no -> name
    combinations   ::Vector{SGCombo}
end

# =============================================================================
# 2  RFEM INTERMEDIATE TYPES
# =============================================================================
struct RFEMNode
    id  ::Int
    name::String
    x   ::Float64
    y   ::Float64
    z   ::Float64
end

struct RFEMNodeRef
    node_id  ::Int
    x_offset ::Float64
    y_offset ::Float64
    z_offset ::Float64
end

struct RFEMLine
    id         ::Int
    sect_id    ::Int
    mat_id     ::Int
    start      ::RFEMNodeRef
    end_ref    ::RFEMNodeRef
    β          ::Float64
    fixed_i    ::NTuple{6,Float64}
    fixed_j    ::NTuple{6,Float64}
    props      ::Dict{String,String}
end

struct RFEMCrossSection
    id                    ::Int
    name                  ::String
    material_id           ::Int          # integer RFEM material number
    shape_type            ::String       # "USER_DEFINED" etc.
    area                  ::Float64      # m^2
    iy                    ::Float64      # m^4
    iz                    ::Float64      # m^4
    j                     ::Float64      # m^4
    asy                   ::Float64      # shear area (y)
    asz                   ::Float64      # shear area (z)
    depth                 ::Float64      # depth dimension (m)
    flange_width          ::Float64      # flange width (m)
    thickness_web         ::Float64      # web thickness (m)
    thickness_flange      ::Float64      # flange thickness (m)
    root_radius           ::Float64      # root radius (m)
    shape                 ::String       # "I","CHS","RHS","SHS","U","LE","UNKNOWN"
    comments              ::String
end

struct RFEMMaterial
    id        ::Int
    name      ::String
    type      ::String
    standard  ::String
    E         ::Float64   # Pa
    nu        ::Float64
    G         ::Float64   # Pa
    density   ::Float64   # t/m^3
    fy        ::Float64   # Pa
    alpha     ::Float64
end

struct RFEMNodalLoadItem
    load_no   ::Int
    node_id   ::Int
    component ::Char      # 'X','Y','Z'
    magnitude ::Float64
end

# Nodal moment: axis 'X','Y','Z' (right-hand rule), magnitude in kNm
struct RFEMNodalMomentItem
    load_no   ::Int
    node_id   ::Int
    axis      ::Char
    magnitude ::Float64
end

# Member load item. kind: :conc_force, :conc_moment or :dist.
# For :conc_* only mag1/a are used; for :dist mag1/mag2 at distances a/b.
# axis: 'G' global axes, 'L' member local axes, 'A' global projected.
struct RFEMMemberLoadItem
    load_no      ::Int
    member       ::Int
    kind         ::Symbol
    component    ::Char        # 'X','Y','Z'
    axis         ::Char        # 'G','L','A'
    distribution ::String      # "CONCENTRATED_1" | "TRAPEZOIDAL"
    relative     ::Bool
    a            ::Float64
    b            ::Float64
    mag1         ::Float64
    mag2         ::Float64
end

struct RFEMCase
    id           ::Int
    name         ::String
    nodal_loads  ::Vector{RFEMNodalLoadItem}
    nodal_moments::Vector{RFEMNodalMomentItem}
    member_loads ::Vector{RFEMMemberLoadItem}
end

# Load combination: ordered (load_case_no, factor) items
struct RFEMCombination
    no    ::Int
    name  ::String
    items ::Vector{Tuple{Int,Float64}}   # (load case no, factor)
end

struct RFEMMember
    id                ::Int
    line_id           ::Int
    start_node        ::Int
    end_node          ::Int
    sect_id           ::Int
    mat_id            ::Int
    length            ::Float64     # m
    volume            ::Float64     # m^3
    mass              ::Float64     # t
    cg_x              ::Float64
    cg_y              ::Float64
    cg_z              ::Float64
    beta              ::Float64
    position_short    ::String   # "|| X", "|| Y", "|| Z"
end

struct RFEMModel
    nodes          ::Dict{Int,RFEMNode}
    lines          ::Dict{Int,RFEMLine}      # geometry lines
    cross_sections ::Dict{Int,RFEMCrossSection}
    materials      ::Dict{Int,RFEMMaterial}
    cases          ::Vector{RFEMCase}
    combinations   ::Vector{RFEMCombination}
    members_data   ::Vector{RFEMMember}      # created after lines
    name           ::String
    units          ::Dict{String,String}
end

# =============================================================================
# 3  SUBMODULES
# =============================================================================

include("parser.jl")
include("converter.jl")
include("rfem_writer.jl")

end # module SGtoRFEM
