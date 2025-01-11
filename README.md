Convert a space gass model (partial) to a python script that can be imported into rfem software.
See runtest.jl for how to generate the *.py file

# Assumptions
1) sg model is z-up
2) sg model units in default m, kN, kN-m

# whats working
1) beam elements only
2) beam orientationn (by direction axis, angle or node) and end release accounted for
3) nodal loads, forces and moments
4) member loads, concentrated and distributed loads 
5) material number assigned to each section
6) load cases and combinations

# lots of not working:
1) sections can only import the names, but need manual assignment within rfem
2) materials name only, need manual assignment within rfem for actual material properties 
3) does not import plates 
