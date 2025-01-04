using ODBC, DataFrames
using Revise
using SGtoRFEM
using Pkg
Pkg.precompile()

# ACTUAL SOURCE CONVERSION CODE

sourcefile = "\\sg_source.MDB"
current_dir = @__DIR__
sg_source_filepathname = current_dir * sourcefile

fWritePyScript(sg_source_filepathname)
