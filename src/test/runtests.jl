using ODBC, DataFrames
using Revise
using SGtoRFEM
using Pkg
Pkg.precompile()

# ACTUAL SOURCE CONVERSION CODE

sourcefile = "\\sg_source.MDB"
current_dir = @__DIR__
filepathname = current_dir * sourcefile
statement = "Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=" * filepathname
dbconn = ODBC.Connection(statement)


# Set global model settings:
pyscript = [set_global_model_settings()]


# MATERILS PROPERTIES QUERY
query_matprop = DBInterface.execute(dbconn, "SELECT * FROM `Material Properties`");
df_matprop = DataFrame(query_matprop)
vMatNames = df_matprop[:, 2]

push!(pyscript, create_materials(vMatNames))

# CREATE SECTIONS
query_secprop = DBInterface.execute(dbconn, "SELECT * FROM `Section Properties`");
df_secprop = DataFrame(query_secprop)

push!(pyscript, create_sections(df_secprop))


# CREATE NODES
query_nodes = DBInterface.execute(dbconn, "SELECT * FROM Nodes");
df_nodes = DataFrame(query_nodes)

push!(pyscript, create_nodes(df_nodes))


# CREATE UNIQUE HINGES
query_members = DBInterface.execute(dbconn, "SELECT * FROM Members");
df_members = DataFrame(query_members)


# parse_hinge(df_members[43,:])
hinges = get_unique_hinges(df_members)
push!(pyscript, create_hinges(hinges))

# CREATE MEMBERS
push!(pyscript, create_beam(df_members, parse_dir_angle(df_members, df_nodes)))
write("sg2rfem.py", join(pyscript, ""))


# CREATE NODAL RESTRAITNS
query_nodal_restraints = DBInterface.execute(dbconn, "SELECT * FROM `Node Restraints`");
df_node_restraints = DataFrame(query_nodal_restraints)

push!(pyscript, create_nodal_supports(df_node_restraints))

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
query_nodal_loads = DBInterface.execute(dbconn, "SELECT * FROM `Node Loads`");
df_nodal_loads = DataFrame(query_nodal_loads)
push!(pyscript, create_nodal_loads(df_nodal_loads))



# CREATE MEMBER LOADS - CONCENTRATED
df_member_loads = DataFrame(DBInterface.execute(dbconn, "SELECT * FROM `Member Concentrated Loads`"))
push!(pyscript, create_member_load_concentrated(df_member_loads))


# CREATE MEMBER LOADS - DISTRIBUTED
df_member_forces = DataFrame(DBInterface.execute(dbconn, "SELECT * FROM `Member Distributed Forces`"))
push!(pyscript, create_member_load_distributed(df_member_forces))

# write to file
# write("sg2rfem.py", join(pyscript, ""))
ODBC.disconnect!(dbconn)
