Convert a space gass model (partial) to a python script that can be imported into rfem software.
See runtest.jl for how to generate the *.py file

# Assumptions
1) sg model is z-up
2) sg model units in default m, kN, kN-m

# whats working
1) beam elements only
2) beam orientation (by direction axis, angle or node) and end release accounted for
   (member local axes: x = length, y = minor axis, z = major axis; Z-up, right-hand rule)
3) nodal loads, forces and moments
4) member loads, concentrated and distributed loads (global / local / projected axes)
5) material number assigned to each section
6) load cases and combinations

# section handling (approximation)
Sections are written to RFEM as **parametric** sections built purely from
dimensions, so the import never fails on missing library entries:

| SG description              | RFEM parametrization                  |
|-----------------------------|---------------------------------------|
| `219.1x6.4 CHS`             | thin-walled CHS (d, t)                |
| `100*50*6 RHS` / `89*5 SHS` | thin-walled RHS / SHS (h, b, t)       |
| `200 UC 46.2`, `310 UB ...`  | thin-walled I (h, b, t_w, t_f, r)     |
| `200 PFC`                   | thin-walled channel U (h, b, t_w,t_f) |
| anything else               | approximated as thin-walled I         |

Dimensions come from the SG description strings and the section continuation
rows. All materials are exported as **steel**; if the SG export has no
MATERIALS block a default S355 steel is created.

# lots of not working:
1) sections are geometric approximations – verify properties before design
2) materials name only, need manual assignment within rfem for actual material properties 
3) does not import plates 
