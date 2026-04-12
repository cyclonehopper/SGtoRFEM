using ODBC, DataFrames
using Revise
using SGtoRFEM
using Pkg
# Pkg.precompile()

# ACTUAL SOURCE CONVERSION CODE

sourcefile = "\\sg_source.MDB"
current_dir = @__DIR__
filepathname = current_dir * sourcefile
statement = "Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=" * filepathname
dbconn = ODBC.Connection(statement)



 
 

# CREATE NODES
query_nodes = DBInterface.execute(dbconn, "SELECT * FROM Nodes");
df_nodes = DataFrame(query_nodes) 

# # CREATE UNIQUE HINGES
query_members = DBInterface.execute(dbconn, "SELECT * FROM Members");
df_members = DataFrame(query_members)
ODBC.disconnect!(dbconn)

x=2
v=3
x+v 

# # parse_hinge(df_members[43,:])
# hinges = get_unique_hinges(df_members)
# # push!(pyscript, create_hinges(hinges))

# # CREATE MEMBERS
str = create_beam(df_members, parse_dir_angle(df_members, df_nodes))

