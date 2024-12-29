Convert a space gass model (partial) to a python script that can be imported into rfem software.
See runtest.jl for how to generate the *.py file

whats working
1) beam elements only
2) beam orientationn (by direction axis, angle or node) and end release accounted for
3) nodal loads, forces and moments
4) member loads, concentrated and distributed loads 

lots of not working:
1) sections can only import the names, but need manual assignment within rfem
2) materials name only
3) will crash if load combinations contains a combination, like if generating cobinations from moving loads
4) does not import plates 
