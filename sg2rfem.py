# Delete default objects:
delete_all()

# Set global model settings:
base_data.current_standard_for_combination_wizard = 6546
base_data.current_standard_for_load_wizard = 6231
base_data.current_standard_for_steel_design = 6679
base_data.activate_load_wizards = False
base_data.member_representatives_active = True
base_data.combination_name_according_to_action_category = True
base_data.global_axes_orientation = "Z upward"
base_data.local_axes_orientation = "y upward | x"
base_data.solids_active = False
base_data.tolerance_for_nodes = 0.000500000023748726
base_data.tolerance_for_lines = 0.000500000023748726
base_data.tolerance_for_surfaces = 0.000500000023748726
base_data.tolerance_for_directions = 0.000500000023748726

# Create Materials
materials.create(1, name="STEEL", definition_type="E | (G) | ν")
materials.create(2, name="dummy", definition_type="E | (G) | ν")

# Create Sections

sections.create_standardized_steel(100, "100*5 SHS")
sections.create_standardized_steel(101, "100 PFC")
sections.create_standardized_steel(125, "125 PFC")
sections.create_standardized_steel(1150, "150*6 SHS")

# Create Nodes
nodes.create_standard( 1, 0.0, 0.0, 0.0)
nodes.create_standard( 2, 0.0, 0.0, 1.525)
nodes.create_standard( 3, -2.26, 1.38380517981929e-16, 0.0)
nodes.create_standard( 4, -2.26, 1.38380517981929e-16, 1.525)
nodes.create_standard( 5, 2.44921270764475e-16, 4.0, 0.0)
nodes.create_standard( 6, 2.44921270764475e-16, 4.0, 1.525)
nodes.create_standard( 7, -2.26, 4.0, 0.0)
nodes.create_standard( 8, -2.26, 4.0, 1.525)
nodes.create_standard( 9, -2.26, 1.383805e-16, 0.7)
nodes.create_standard( 10, 0.0, 0.0, 0.7)
nodes.create_standard( 11, -2.26, 4.0, 0.7)
nodes.create_standard( 12, 2.44921270764475e-16, 4.0, 0.7)
nodes.create_standard( 13, -2.26, 1.383805e-16, 0.775)
nodes.create_standard( 14, 0.0, 0.0, 1.4)
nodes.create_standard( 15, -2.26, 4.0, 0.775)
nodes.create_standard( 16, 2.44921270764475e-16, 4.0, 1.4)
nodes.create_standard( 17, 0.0, 0.0, 1.475)
nodes.create_standard( 18, -2.26, 1.38380517981929e-16, 1.475)
nodes.create_standard( 19, 2.44921270764475e-16, 4.0, 1.475)
nodes.create_standard( 20, -2.26, 4.0, 1.475)
nodes.create_standard( 21, 1.22460635382238e-16, 2.0, 1.05)
nodes.create_standard( 22, -2.26, 2.0, 1.05)
nodes.create_standard( 23, -2.26, 4.0, 1.4)
nodes.create_standard( 24, -2.26, 0.0, 1.4)
nodes.create_standard( 25, 2.449213e-16, 4.0, 0.14)
nodes.create_standard( 26, 2.449213e-16, 4.0, 0.28)
nodes.create_standard( 27, 2.449213e-16, 4.0, 0.42)
nodes.create_standard( 28, 2.449213e-16, 4.0, 0.56)
nodes.create_standard( 29, 2.449213e-16, 4.0, 0.84)
nodes.create_standard( 30, 2.449213e-16, 4.0, 0.98)
nodes.create_standard( 31, 2.449213e-16, 4.0, 1.12)
nodes.create_standard( 32, 2.449213e-16, 4.0, 1.26)
nodes.create_standard( 33, -2.26, 4.0, 0.14)
nodes.create_standard( 34, -2.26, 4.0, 0.28)
nodes.create_standard( 35, -2.26, 4.0, 0.42)
nodes.create_standard( 36, -2.26, 4.0, 0.56)
nodes.create_standard( 37, -2.26, 4.0, 0.9)
nodes.create_standard( 38, -2.26, 4.0, 1.025)
nodes.create_standard( 39, -2.26, 4.0, 1.15)
nodes.create_standard( 40, -2.26, 4.0, 1.275)

 # Create Member Hinges
member_hinges.create(1, axial_release_n=inf, axial_release_vy=inf, axial_release_vz=inf, moment_release_mt=inf)
member_hinges.create(2, axial_release_n=1000.0, axial_release_vy=inf, axial_release_vz=inf, moment_release_my=2000.0, moment_release_mz=3000.0)
member_hinges.create(3, axial_release_n=4.0, axial_release_vy=inf, axial_release_vz=inf, moment_release_mt=inf, moment_release_my=5.0, moment_release_mz=6.0)
member_hinges.create(4, axial_release_n=inf, axial_release_vy=inf, axial_release_vz=inf, moment_release_mt=inf, moment_release_my=0.001, moment_release_mz=0.001)# Create Lines

lines.create_polyline(1, "1,10")
lines.create_polyline(2, "3,9")
lines.create_polyline(3, "5,25")
lines.create_polyline(4, "7,33")
lines.create_polyline(5, "9,13")
lines.create_polyline(6, "10,14")
lines.create_polyline(7, "9,10")
lines.create_polyline(8, "11,15")
lines.create_polyline(9, "17,2")
lines.create_polyline(10, "18,4")
lines.create_polyline(11, "17,18")
lines.create_polyline(12, "19,20")
lines.create_polyline(13, "15,16")
lines.create_polyline(14, "12,29")
lines.create_polyline(15, "19,6")
lines.create_polyline(16, "24,18")
lines.create_polyline(17, "11,12")
lines.create_polyline(18, "23,20")
lines.create_polyline(19, "13,24")
lines.create_polyline(20, "25,26")
lines.create_polyline(21, "26,27")
lines.create_polyline(22, "27,28")
lines.create_polyline(23, "28,12")
lines.create_polyline(24, "29,30")
lines.create_polyline(25, "30,31")
lines.create_polyline(26, "31,32")
lines.create_polyline(27, "32,16")
lines.create_polyline(28, "33,34")
lines.create_polyline(29, "34,35")
lines.create_polyline(30, "35,36")
lines.create_polyline(31, "36,11")
lines.create_polyline(32, "14,17")
lines.create_polyline(33, "13,14")
lines.create_polyline(34, "15,37")
lines.create_polyline(35, "20,8")
lines.create_polyline(36, "16,19")
lines.create_polyline(37, "10,21")
lines.create_polyline(38, "12,21")
lines.create_polyline(39, "21,16")
lines.create_polyline(40, "21,14")
lines.create_polyline(41, "22,9")
lines.create_polyline(42, "23,22")
lines.create_polyline(43, "24,22")
lines.create_polyline(44, "37,38")
lines.create_polyline(45, "38,39")
lines.create_polyline(46, "39,40")
lines.create_polyline(47, "40,23")
lines.create_polyline(48, "22,11")


# Create Members 
members.create_beam(1, "100", line="1")
members.create_beam(2, "100", line="2")
members.create_beam(3, "100", line="3")
members.create_beam(4, "100", line="4")
members.create_beam(5, "100", line="5")
members.create_beam(6, "100", line="6")
members.create_beam(7, "100", line="7")
members.create_beam(8, "100", line="8")
members.create_beam(9, "100", line="9")
members.create_beam(10, "100", line="10")
members.create_beam(11, "100", line="11")
members.create_beam(12, "100", line="12")
members.create_beam(13, "101", line="13", member_hinge_start="1", member_hinge_end="1")
members.create_beam(14, "100", line="14")
members.create_beam(15, "100", line="15")
members.create_beam(16, "100", line="16")
members.create_beam(17, "100", line="17")
members.create_beam(18, "100", line="18")
members.create_beam(19, "100", line="19")
members.create_beam(20, "100", line="20")
members.create_beam(21, "100", line="21")
members.create_beam(22, "100", line="22")
members.create_beam(23, "100", line="23")
members.create_beam(24, "100", line="24")
members.create_beam(25, "100", line="25")
members.create_beam(26, "100", line="26")
members.create_beam(27, "100", line="27")
members.create_beam(28, "100", line="28")
members.create_beam(29, "100", line="29")
members.create_beam(30, "100", line="30")
members.create_beam(31, "100", line="31")
members.create_beam(32, "100", line="32")
members.create_beam(33, "101", line="33", member_hinge_start="2", member_hinge_end="3")
members.create_beam(34, "100", line="34")
members.create_beam(35, "100", line="35")
members.create_beam(36, "100", line="36")
members.create_beam(37, "101", line="37", member_hinge_start="1")
members.create_beam(38, "101", line="38", member_hinge_start="1")
members.create_beam(39, "101", line="39", member_hinge_end="4")
members.create_beam(40, "101", line="40", member_hinge_end="1")
members.create_beam(41, "101", line="41", member_hinge_end="1")
members.create_beam(42, "101", line="42", member_hinge_start="1")
members.create_beam(43, "101", line="43", member_hinge_start="1")
members.create_beam(44, "100", line="44")
members.create_beam(45, "100", line="45")
members.create_beam(46, "100", line="46")
members.create_beam(47, "100", line="47")
members.create_beam(48, "101", line="48", member_hinge_end="1")

# Create Nodal Supports
nodal_supports.create(1, nodes="1,3",  spring=[inf,inf,inf], rotational_restraint=[0,0,inf])
nodal_supports.create(2, nodes="5",  spring=[5.201e6,5.63e6,inf], rotational_restraint=[0,0,inf])
nodal_supports.create(3, nodes="7",  spring=[0,inf,inf], rotational_restraint=[inf,0,inf])

# Create Static Analysis Settings
static_analysis_settings.create(1)
static_analysis_settings.create(2, analysis_type="Second-order (P-Δ)")

# Create Load Cases
load_cases.create(1, name="G(SW) - Structure Self Weight", static_analysis_settings="SA1", to_solve=False)
load_cases.create(2, name="G(SD) - Structural Dead Loads", static_analysis_settings="SA1", to_solve=False)
load_cases.create(3, name="G(EQ) - Equipment Dead Loads", static_analysis_settings="SA1", to_solve=False)
load_cases.create(10, name="Q(rLL) Roof live load", static_analysis_settings="SA1", to_solve=False)
load_cases.create(11, name="Q(L1) - General Floor Loads", static_analysis_settings="SA1", to_solve=False)
load_cases.create(12, name="Q(S) - Pipe and Elec. Services", static_analysis_settings="SA1", to_solve=False)
load_cases.create(13, name="Q(S2) - Pipe and Elec. Services", static_analysis_settings="SA1", to_solve=False)
load_cases.create(14, name="Q(SP) - Material Spillage", static_analysis_settings="SA1", to_solve=False)
load_cases.create(21, name="Q(ML) - Belt Material Load - Operating", static_analysis_settings="SA1", to_solve=False)
load_cases.create(22, name="Q(FL) - Belt Material Load - Flooded", static_analysis_settings="SA1", to_solve=False)
load_cases.create(23, name="Q(BTN) - Belt Tension Not Operating", static_analysis_settings="SA1", to_solve=False)
load_cases.create(24, name="Q(BTO) - Belt Tension Operating", static_analysis_settings="SA1", to_solve=False)
load_cases.create(25, name="Q(MPT) - Belt Tension Motor Peak Torque", static_analysis_settings="SA1", to_solve=False)
load_cases.create(31, name="Q(TO) - Tank and Bin Operating", static_analysis_settings="SA1", to_solve=False)
load_cases.create(32, name="Q(TE) - Tank and Bin Extreme", static_analysis_settings="SA1", to_solve=False)
load_cases.create(33, name="Q(CH) - Chute Extreme (Blocked)", static_analysis_settings="SA1", to_solve=False)
load_cases.create(41, name="Q(EO) - Equipment Operating", static_analysis_settings="SA1", to_solve=False)
load_cases.create(42, name="Q(EE) - Equipment Extreme", static_analysis_settings="SA1", to_solve=False)
load_cases.create(43, name="Q(CR) - Crane MRC", static_analysis_settings="SA1", to_solve=False)
load_cases.create(61, name="Q(TH) - Thermal High", static_analysis_settings="SA1", to_solve=False)
load_cases.create(63, name="Eu(x) Earthquake in +x direction", static_analysis_settings="SA1", to_solve=False)
load_cases.create(64, name="Eu(y) Earthquake in +y direction", static_analysis_settings="SA1", to_solve=False)
load_cases.create(71, name="Wu+xD", static_analysis_settings="SA1", to_solve=False)
load_cases.create(72, name="Wu-xD", static_analysis_settings="SA1", to_solve=False)
load_cases.create(73, name="Wu+xU", static_analysis_settings="SA1", to_solve=False)
load_cases.create(74, name="Wu-xU", static_analysis_settings="SA1", to_solve=False)
load_cases.create(75, name="Wu+yD", static_analysis_settings="SA1", to_solve=False)
load_cases.create(76, name="Wu-yD", static_analysis_settings="SA1", to_solve=False)
load_cases.create(77, name="Wu+yU", static_analysis_settings="SA1", to_solve=False)
load_cases.create(78, name="Wu-yU", static_analysis_settings="SA1", to_solve=False)
load_cases.create(79, name="Wu+xDi", static_analysis_settings="SA1", to_solve=False)
load_cases.create(80, name="Wu-xDi", static_analysis_settings="SA1", to_solve=False)
load_cases.create(81, name="Wu+xUi", static_analysis_settings="SA1", to_solve=False)
load_cases.create(82, name="Wu-xUi", static_analysis_settings="SA1", to_solve=False)
load_cases.create(83, name="Wu+yDi", static_analysis_settings="SA1", to_solve=False)
load_cases.create(84, name="Wu-yDi", static_analysis_settings="SA1", to_solve=False)
load_cases.create(85, name="Wu+yUi", static_analysis_settings="SA1", to_solve=False)
load_cases.create(86, name="Wu-yUi", static_analysis_settings="SA1", to_solve=False)

# Create Design Situations
design_situations.create(1, name="ULS - Strength", design_situation_type="DESIGN_SITUATION_TYPE_ULS_STRENGTH_AS_NZS")
design_situations.create(2, name="SLS - Serviceability", design_situation_type="DESIGN_SITUATION_TYPE_SLS_SERVICEABILITY_NZS")

# Create Load Combinations Titles
load_combinations.create(101, design_situation="DS1", user_defined_name_enabled=True, name="Ult Dead Load Extreme", static_analysis_settings="SA2")
load_combinations[101].items[1].load_case=1
load_combinations[101].items[1].factor=1.35
load_combinations[101].items[2].load_case=2
load_combinations[101].items[2].factor=1.35
load_combinations[101].items[3].load_case=3
load_combinations[101].items[3].factor=1.35
load_combinations[101].items[4].load_case=12
load_combinations[101].items[4].factor=1.35
load_combinations[101].items[5].load_case=21
load_combinations[101].items[5].factor=1.0
load_combinations[101].items[6].load_case=23
load_combinations[101].items[6].factor=1.35
load_combinations[101].items[7].load_case=31
load_combinations[101].items[7].factor=1.35
load_combinations.create(111, design_situation="DS1", user_defined_name_enabled=True, name="Ult Live Load Extreme", static_analysis_settings="SA2")
load_combinations[111].items[1].load_case=1
load_combinations[111].items[1].factor=1.2
load_combinations[111].items[2].load_case=2
load_combinations[111].items[2].factor=1.2
load_combinations[111].items[3].load_case=3
load_combinations[111].items[3].factor=1.2
load_combinations[111].items[4].load_case=11
load_combinations[111].items[4].factor=1.5
load_combinations[111].items[5].load_case=12
load_combinations[111].items[5].factor=0.6
load_combinations[111].items[6].load_case=14
load_combinations[111].items[6].factor=0.4
load_combinations[111].items[7].load_case=21
load_combinations[111].items[7].factor=1.0
load_combinations[111].items[8].load_case=24
load_combinations[111].items[8].factor=1.2
load_combinations[111].items[9].load_case=31
load_combinations[111].items[9].factor=1.2
load_combinations[111].items[10].load_case=33
load_combinations[111].items[10].factor=0.2
load_combinations[111].items[11].load_case=41
load_combinations[111].items[11].factor=1.5
load_combinations[111].items[12].load_case=43
load_combinations[111].items[12].factor=0.4
load_combinations.create(112, design_situation="DS1", user_defined_name_enabled=True, name="Ult Services Extreme", static_analysis_settings="SA2")
load_combinations[112].items[1].load_case=1
load_combinations[112].items[1].factor=1.2
load_combinations[112].items[2].load_case=2
load_combinations[112].items[2].factor=1.2
load_combinations[112].items[3].load_case=3
load_combinations[112].items[3].factor=1.2
load_combinations[112].items[4].load_case=11
load_combinations[112].items[4].factor=0.4
load_combinations[112].items[5].load_case=12
load_combinations[112].items[5].factor=1.5
load_combinations[112].items[6].load_case=14
load_combinations[112].items[6].factor=0.4
load_combinations[112].items[7].load_case=21
load_combinations[112].items[7].factor=1.0
load_combinations[112].items[8].load_case=24
load_combinations[112].items[8].factor=1.2
load_combinations[112].items[9].load_case=31
load_combinations[112].items[9].factor=1.2
load_combinations[112].items[10].load_case=33
load_combinations[112].items[10].factor=0.2
load_combinations[112].items[11].load_case=41
load_combinations[112].items[11].factor=1.2
load_combinations[112].items[12].load_case=43
load_combinations[112].items[12].factor=0.4
load_combinations.create(113, design_situation="DS1", user_defined_name_enabled=True, name="Ult Services Extreme", static_analysis_settings="SA2")
load_combinations[113].items[1].load_case=1
load_combinations[113].items[1].factor=1.2
load_combinations[113].items[2].load_case=2
load_combinations[113].items[2].factor=1.2
load_combinations[113].items[3].load_case=3
load_combinations[113].items[3].factor=1.2
load_combinations[113].items[4].load_case=11
load_combinations[113].items[4].factor=0.4
load_combinations[113].items[5].load_case=13
load_combinations[113].items[5].factor=1.5
load_combinations[113].items[6].load_case=14
load_combinations[113].items[6].factor=0.4
load_combinations[113].items[7].load_case=21
load_combinations[113].items[7].factor=1.0
load_combinations[113].items[8].load_case=24
load_combinations[113].items[8].factor=1.2
load_combinations[113].items[9].load_case=31
load_combinations[113].items[9].factor=1.2
load_combinations[113].items[10].load_case=33
load_combinations[113].items[10].factor=0.2
load_combinations[113].items[11].load_case=41
load_combinations[113].items[11].factor=1.2
load_combinations[113].items[12].load_case=43
load_combinations[113].items[12].factor=0.4
load_combinations.create(114, design_situation="DS1", user_defined_name_enabled=True, name="Ult Roof Live Load Extreme", static_analysis_settings="SA2")
load_combinations[114].items[1].load_case=1
load_combinations[114].items[1].factor=1.2
load_combinations[114].items[2].load_case=2
load_combinations[114].items[2].factor=1.2
load_combinations[114].items[3].load_case=3
load_combinations[114].items[3].factor=1.2
load_combinations[114].items[4].load_case=10
load_combinations[114].items[4].factor=1.5
load_combinations.create(121, design_situation="DS1", user_defined_name_enabled=True, name="Ult Material and Tension Extreme", static_analysis_settings="SA2")
load_combinations[121].items[1].load_case=1
load_combinations[121].items[1].factor=1.2
load_combinations[121].items[2].load_case=2
load_combinations[121].items[2].factor=1.2
load_combinations[121].items[3].load_case=3
load_combinations[121].items[3].factor=1.2
load_combinations[121].items[4].load_case=11
load_combinations[121].items[4].factor=0.4
load_combinations[121].items[5].load_case=12
load_combinations[121].items[5].factor=0.6
load_combinations[121].items[6].load_case=14
load_combinations[121].items[6].factor=1.5
load_combinations[121].items[7].load_case=22
load_combinations[121].items[7].factor=1.2
load_combinations[121].items[8].load_case=25
load_combinations[121].items[8].factor=1.5
load_combinations[121].items[9].load_case=32
load_combinations[121].items[9].factor=1.2
load_combinations[121].items[10].load_case=33
load_combinations[121].items[10].factor=1.2
load_combinations[121].items[11].load_case=41
load_combinations[121].items[11].factor=1.2
load_combinations[121].items[12].load_case=43
load_combinations[121].items[12].factor=0.4
load_combinations.create(122, design_situation="DS1", user_defined_name_enabled=True, name="Ult Material Extreme", static_analysis_settings="SA2")
load_combinations[122].items[1].load_case=1
load_combinations[122].items[1].factor=1.2
load_combinations[122].items[2].load_case=2
load_combinations[122].items[2].factor=1.2
load_combinations[122].items[3].load_case=3
load_combinations[122].items[3].factor=1.2
load_combinations[122].items[4].load_case=11
load_combinations[122].items[4].factor=0.4
load_combinations[122].items[5].load_case=12
load_combinations[122].items[5].factor=0.6
load_combinations[122].items[6].load_case=14
load_combinations[122].items[6].factor=1.5
load_combinations[122].items[7].load_case=22
load_combinations[122].items[7].factor=1.2
load_combinations[122].items[8].load_case=23
load_combinations[122].items[8].factor=0.9
load_combinations[122].items[9].load_case=31
load_combinations[122].items[9].factor=1.2
load_combinations[122].items[10].load_case=33
load_combinations[122].items[10].factor=0.2
load_combinations[122].items[11].load_case=41
load_combinations[122].items[11].factor=1.2
load_combinations[122].items[12].load_case=43
load_combinations[122].items[12].factor=0.4
load_combinations.create(123, design_situation="DS1", user_defined_name_enabled=True, name="Ult Belt Tension Extreme - uplift", static_analysis_settings="SA2")
load_combinations[123].items[1].load_case=1
load_combinations[123].items[1].factor=0.9
load_combinations[123].items[2].load_case=2
load_combinations[123].items[2].factor=0.9
load_combinations[123].items[3].load_case=3
load_combinations[123].items[3].factor=0.9
load_combinations[123].items[4].load_case=25
load_combinations[123].items[4].factor=1.5
load_combinations[123].items[5].load_case=41
load_combinations[123].items[5].factor=1.5
load_combinations.create(131, design_situation="DS1", user_defined_name_enabled=True, name="Ult Equipment Extreme", static_analysis_settings="SA2")
load_combinations[131].items[1].load_case=1
load_combinations[131].items[1].factor=1.2
load_combinations[131].items[2].load_case=2
load_combinations[131].items[2].factor=1.2
load_combinations[131].items[3].load_case=3
load_combinations[131].items[3].factor=1.2
load_combinations[131].items[4].load_case=11
load_combinations[131].items[4].factor=0.4
load_combinations[131].items[5].load_case=12
load_combinations[131].items[5].factor=0.6
load_combinations[131].items[6].load_case=14
load_combinations[131].items[6].factor=1.5
load_combinations[131].items[7].load_case=21
load_combinations[131].items[7].factor=1.0
load_combinations[131].items[8].load_case=23
load_combinations[131].items[8].factor=1.2
load_combinations[131].items[9].load_case=32
load_combinations[131].items[9].factor=1.2
load_combinations[131].items[10].load_case=33
load_combinations[131].items[10].factor=1.2
load_combinations[131].items[11].load_case=42
load_combinations[131].items[11].factor=1.5
load_combinations[131].items[12].load_case=43
load_combinations[131].items[12].factor=0.4
load_combinations.create(132, design_situation="DS1", user_defined_name_enabled=True, name="Ult Equipment Extreme - uplift", static_analysis_settings="SA2")
load_combinations[132].items[1].load_case=1
load_combinations[132].items[1].factor=0.9
load_combinations[132].items[2].load_case=2
load_combinations[132].items[2].factor=0.9
load_combinations[132].items[3].load_case=3
load_combinations[132].items[3].factor=0.9
load_combinations[132].items[4].load_case=23
load_combinations[132].items[4].factor=0.9
load_combinations[132].items[5].load_case=42
load_combinations[132].items[5].factor=-1.5
load_combinations.create(141, design_situation="DS1", user_defined_name_enabled=True, name="Ult Crane - plant not operating  ++WuxD", static_analysis_settings="SA2")
load_combinations[141].items[1].load_case=1
load_combinations[141].items[1].factor=1.2
load_combinations[141].items[2].load_case=2
load_combinations[141].items[2].factor=1.2
load_combinations[141].items[3].load_case=3
load_combinations[141].items[3].factor=1.2
load_combinations[141].items[4].load_case=11
load_combinations[141].items[4].factor=0.4
load_combinations[141].items[5].load_case=12
load_combinations[141].items[5].factor=0.6
load_combinations[141].items[6].load_case=14
load_combinations[141].items[6].factor=0.4
load_combinations[141].items[7].load_case=23
load_combinations[141].items[7].factor=1.2
load_combinations[141].items[8].load_case=31
load_combinations[141].items[8].factor=1.2
load_combinations[141].items[9].load_case=33
load_combinations[141].items[9].factor=0.2
load_combinations[141].items[10].load_case=43
load_combinations[141].items[10].factor=1.5
load_combinations[141].items[11].load_case=71
load_combinations[141].items[11].factor=0.19
load_combinations[141].items[12].load_case=79
load_combinations[141].items[12].factor=0.19
load_combinations.create(142, design_situation="DS1", user_defined_name_enabled=True, name="Ult Crane - plant not operating  +-WuxD", static_analysis_settings="SA2")
load_combinations[142].items[1].load_case=1
load_combinations[142].items[1].factor=1.2
load_combinations[142].items[2].load_case=2
load_combinations[142].items[2].factor=1.2
load_combinations[142].items[3].load_case=3
load_combinations[142].items[3].factor=1.2
load_combinations[142].items[4].load_case=11
load_combinations[142].items[4].factor=0.4
load_combinations[142].items[5].load_case=12
load_combinations[142].items[5].factor=0.6
load_combinations[142].items[6].load_case=14
load_combinations[142].items[6].factor=0.4
load_combinations[142].items[7].load_case=23
load_combinations[142].items[7].factor=1.2
load_combinations[142].items[8].load_case=31
load_combinations[142].items[8].factor=1.2
load_combinations[142].items[9].load_case=33
load_combinations[142].items[9].factor=0.2
load_combinations[142].items[10].load_case=43
load_combinations[142].items[10].factor=1.5
load_combinations[142].items[11].load_case=72
load_combinations[142].items[11].factor=0.19
load_combinations[142].items[12].load_case=80
load_combinations[142].items[12].factor=0.19
load_combinations.create(143, design_situation="DS1", user_defined_name_enabled=True, name="Ult Crane - plant not operating ++WuYD", static_analysis_settings="SA2")
load_combinations[143].items[1].load_case=1
load_combinations[143].items[1].factor=1.2
load_combinations[143].items[2].load_case=2
load_combinations[143].items[2].factor=1.2
load_combinations[143].items[3].load_case=3
load_combinations[143].items[3].factor=1.2
load_combinations[143].items[4].load_case=11
load_combinations[143].items[4].factor=0.4
load_combinations[143].items[5].load_case=12
load_combinations[143].items[5].factor=0.6
load_combinations[143].items[6].load_case=14
load_combinations[143].items[6].factor=0.4
load_combinations[143].items[7].load_case=23
load_combinations[143].items[7].factor=1.2
load_combinations[143].items[8].load_case=31
load_combinations[143].items[8].factor=1.2
load_combinations[143].items[9].load_case=33
load_combinations[143].items[9].factor=0.2
load_combinations[143].items[10].load_case=43
load_combinations[143].items[10].factor=1.5
load_combinations[143].items[11].load_case=75
load_combinations[143].items[11].factor=0.19
load_combinations[143].items[12].load_case=83
load_combinations[143].items[12].factor=0.19
load_combinations.create(144, design_situation="DS1", user_defined_name_enabled=True, name="Ult Crane - plant not operating +-WuyD", static_analysis_settings="SA2")
load_combinations[144].items[1].load_case=1
load_combinations[144].items[1].factor=1.2
load_combinations[144].items[2].load_case=2
load_combinations[144].items[2].factor=1.2
load_combinations[144].items[3].load_case=3
load_combinations[144].items[3].factor=1.2
load_combinations[144].items[4].load_case=11
load_combinations[144].items[4].factor=0.4
load_combinations[144].items[5].load_case=12
load_combinations[144].items[5].factor=0.6
load_combinations[144].items[6].load_case=14
load_combinations[144].items[6].factor=0.4
load_combinations[144].items[7].load_case=23
load_combinations[144].items[7].factor=1.2
load_combinations[144].items[8].load_case=31
load_combinations[144].items[8].factor=1.2
load_combinations[144].items[9].load_case=33
load_combinations[144].items[9].factor=0.2
load_combinations[144].items[10].load_case=43
load_combinations[144].items[10].factor=1.5
load_combinations[144].items[11].load_case=76
load_combinations[144].items[11].factor=0.19
load_combinations[144].items[12].load_case=84
load_combinations[144].items[12].factor=0.19
load_combinations.create(145, design_situation="DS1", user_defined_name_enabled=True, name="Ult Crane - plant not operating, uplift   ++WuxD", static_analysis_settings="SA2")
load_combinations[145].items[1].load_case=1
load_combinations[145].items[1].factor=0.9
load_combinations[145].items[2].load_case=2
load_combinations[145].items[2].factor=0.9
load_combinations[145].items[3].load_case=3
load_combinations[145].items[3].factor=0.9
load_combinations[145].items[4].load_case=23
load_combinations[145].items[4].factor=0.9
load_combinations[145].items[5].load_case=41
load_combinations[145].items[5].factor=1.0
load_combinations[145].items[6].load_case=43
load_combinations[145].items[6].factor=1.5
load_combinations[145].items[7].load_case=73
load_combinations[145].items[7].factor=0.19
load_combinations[145].items[8].load_case=81
load_combinations[145].items[8].factor=0.19
load_combinations.create(146, design_situation="DS1", user_defined_name_enabled=True, name="Ult Crane - plant not operating, uplift   +-WuxD", static_analysis_settings="SA2")
load_combinations[146].items[1].load_case=1
load_combinations[146].items[1].factor=0.9
load_combinations[146].items[2].load_case=2
load_combinations[146].items[2].factor=0.9
load_combinations[146].items[3].load_case=3
load_combinations[146].items[3].factor=0.9
load_combinations[146].items[4].load_case=23
load_combinations[146].items[4].factor=0.9
load_combinations[146].items[5].load_case=41
load_combinations[146].items[5].factor=1.0
load_combinations[146].items[6].load_case=43
load_combinations[146].items[6].factor=1.5
load_combinations[146].items[7].load_case=74
load_combinations[146].items[7].factor=0.19
load_combinations[146].items[8].load_case=82
load_combinations[146].items[8].factor=0.19
load_combinations.create(147, design_situation="DS1", user_defined_name_enabled=True, name="Ult Crane - plant not operating, uplift   ++WuyD", static_analysis_settings="SA2")
load_combinations[147].items[1].load_case=1
load_combinations[147].items[1].factor=0.9
load_combinations[147].items[2].load_case=2
load_combinations[147].items[2].factor=0.9
load_combinations[147].items[3].load_case=3
load_combinations[147].items[3].factor=0.9
load_combinations[147].items[4].load_case=23
load_combinations[147].items[4].factor=0.9
load_combinations[147].items[5].load_case=41
load_combinations[147].items[5].factor=1.0
load_combinations[147].items[6].load_case=43
load_combinations[147].items[6].factor=1.5
load_combinations[147].items[7].load_case=77
load_combinations[147].items[7].factor=0.19
load_combinations[147].items[8].load_case=85
load_combinations[147].items[8].factor=0.19
load_combinations.create(148, design_situation="DS1", user_defined_name_enabled=True, name="Ult Crane - plant not operating, uplift   +-WuyD", static_analysis_settings="SA2")
load_combinations[148].items[1].load_case=1
load_combinations[148].items[1].factor=0.9
load_combinations[148].items[2].load_case=2
load_combinations[148].items[2].factor=0.9
load_combinations[148].items[3].load_case=3
load_combinations[148].items[3].factor=0.9
load_combinations[148].items[4].load_case=23
load_combinations[148].items[4].factor=0.9
load_combinations[148].items[5].load_case=41
load_combinations[148].items[5].factor=1.0
load_combinations[148].items[6].load_case=43
load_combinations[148].items[6].factor=1.5
load_combinations[148].items[7].load_case=78
load_combinations[148].items[7].factor=0.19
load_combinations[148].items[8].load_case=86
load_combinations[148].items[8].factor=0.19
load_combinations.create(151, design_situation="DS1", user_defined_name_enabled=True, name="Ult Operating Plant + 1.25 Thermal", static_analysis_settings="SA2")
load_combinations[151].items[1].load_case=1
load_combinations[151].items[1].factor=1.2
load_combinations[151].items[2].load_case=2
load_combinations[151].items[2].factor=1.2
load_combinations[151].items[3].load_case=3
load_combinations[151].items[3].factor=1.2
load_combinations[151].items[4].load_case=11
load_combinations[151].items[4].factor=0.4
load_combinations[151].items[5].load_case=12
load_combinations[151].items[5].factor=0.6
load_combinations[151].items[6].load_case=14
load_combinations[151].items[6].factor=0.4
load_combinations[151].items[7].load_case=21
load_combinations[151].items[7].factor=1.0
load_combinations[151].items[8].load_case=24
load_combinations[151].items[8].factor=1.2
load_combinations[151].items[9].load_case=31
load_combinations[151].items[9].factor=1.2
load_combinations[151].items[10].load_case=33
load_combinations[151].items[10].factor=0.2
load_combinations[151].items[11].load_case=41
load_combinations[151].items[11].factor=1.2
load_combinations[151].items[12].load_case=43
load_combinations[151].items[12].factor=0.4
load_combinations[151].items[13].load_case=61
load_combinations[151].items[13].factor=1.25
load_combinations.create(152, design_situation="DS1", user_defined_name_enabled=True, name="Ult Operating Plant - 1.25 Thermal", static_analysis_settings="SA2")
load_combinations[152].items[1].load_case=1
load_combinations[152].items[1].factor=1.2
load_combinations[152].items[2].load_case=2
load_combinations[152].items[2].factor=1.2
load_combinations[152].items[3].load_case=3
load_combinations[152].items[3].factor=1.2
load_combinations[152].items[4].load_case=11
load_combinations[152].items[4].factor=0.4
load_combinations[152].items[5].load_case=12
load_combinations[152].items[5].factor=0.6
load_combinations[152].items[6].load_case=14
load_combinations[152].items[6].factor=0.4
load_combinations[152].items[7].load_case=21
load_combinations[152].items[7].factor=1.0
load_combinations[152].items[8].load_case=24
load_combinations[152].items[8].factor=1.2
load_combinations[152].items[9].load_case=31
load_combinations[152].items[9].factor=1.2
load_combinations[152].items[10].load_case=33
load_combinations[152].items[10].factor=0.2
load_combinations[152].items[11].load_case=41
load_combinations[152].items[11].factor=1.2
load_combinations[152].items[12].load_case=43
load_combinations[152].items[12].factor=0.4
load_combinations[152].items[13].load_case=61
load_combinations[152].items[13].factor=-1.25
load_combinations.create(153, design_situation="DS1", user_defined_name_enabled=True, name="Ult Operating Plant + 1.5 * Wind Wop x+", static_analysis_settings="SA2")
load_combinations[153].items[1].load_case=1
load_combinations[153].items[1].factor=1.2
load_combinations[153].items[2].load_case=2
load_combinations[153].items[2].factor=1.2
load_combinations[153].items[3].load_case=3
load_combinations[153].items[3].factor=1.2
load_combinations[153].items[4].load_case=11
load_combinations[153].items[4].factor=0.4
load_combinations[153].items[5].load_case=12
load_combinations[153].items[5].factor=0.6
load_combinations[153].items[6].load_case=14
load_combinations[153].items[6].factor=0.4
load_combinations[153].items[7].load_case=21
load_combinations[153].items[7].factor=1.0
load_combinations[153].items[8].load_case=24
load_combinations[153].items[8].factor=1.2
load_combinations[153].items[9].load_case=31
load_combinations[153].items[9].factor=1.2
load_combinations[153].items[10].load_case=33
load_combinations[153].items[10].factor=0.2
load_combinations[153].items[11].load_case=41
load_combinations[153].items[11].factor=1.2
load_combinations[153].items[12].load_case=43
load_combinations[153].items[12].factor=0.4
load_combinations[153].items[13].load_case=71
load_combinations[153].items[13].factor=0.19
load_combinations[153].items[14].load_case=79
load_combinations[153].items[14].factor=0.19
load_combinations.create(154, design_situation="DS1", user_defined_name_enabled=True, name="Ult Operating Plant + 1.5 * Wind Wop x-", static_analysis_settings="SA2")
load_combinations[154].items[1].load_case=1
load_combinations[154].items[1].factor=1.2
load_combinations[154].items[2].load_case=2
load_combinations[154].items[2].factor=1.2
load_combinations[154].items[3].load_case=3
load_combinations[154].items[3].factor=1.2
load_combinations[154].items[4].load_case=11
load_combinations[154].items[4].factor=0.4
load_combinations[154].items[5].load_case=12
load_combinations[154].items[5].factor=0.6
load_combinations[154].items[6].load_case=14
load_combinations[154].items[6].factor=0.4
load_combinations[154].items[7].load_case=21
load_combinations[154].items[7].factor=1.0
load_combinations[154].items[8].load_case=24
load_combinations[154].items[8].factor=1.2
load_combinations[154].items[9].load_case=31
load_combinations[154].items[9].factor=1.2
load_combinations[154].items[10].load_case=33
load_combinations[154].items[10].factor=0.2
load_combinations[154].items[11].load_case=41
load_combinations[154].items[11].factor=1.2
load_combinations[154].items[12].load_case=43
load_combinations[154].items[12].factor=0.4
load_combinations[154].items[13].load_case=72
load_combinations[154].items[13].factor=0.19
load_combinations[154].items[14].load_case=80
load_combinations[154].items[14].factor=0.19
load_combinations.create(155, design_situation="DS1", user_defined_name_enabled=True, name="Ult Operating Plant + 1.5 * Wind Wop y+", static_analysis_settings="SA2")
load_combinations[155].items[1].load_case=1
load_combinations[155].items[1].factor=1.2
load_combinations[155].items[2].load_case=2
load_combinations[155].items[2].factor=1.2
load_combinations[155].items[3].load_case=3
load_combinations[155].items[3].factor=1.2
load_combinations[155].items[4].load_case=11
load_combinations[155].items[4].factor=0.4
load_combinations[155].items[5].load_case=12
load_combinations[155].items[5].factor=0.6
load_combinations[155].items[6].load_case=14
load_combinations[155].items[6].factor=0.4
load_combinations[155].items[7].load_case=21
load_combinations[155].items[7].factor=1.0
load_combinations[155].items[8].load_case=24
load_combinations[155].items[8].factor=1.2
load_combinations[155].items[9].load_case=31
load_combinations[155].items[9].factor=1.2
load_combinations[155].items[10].load_case=33
load_combinations[155].items[10].factor=0.2
load_combinations[155].items[11].load_case=41
load_combinations[155].items[11].factor=1.2
load_combinations[155].items[12].load_case=43
load_combinations[155].items[12].factor=0.4
load_combinations[155].items[13].load_case=75
load_combinations[155].items[13].factor=0.19
load_combinations[155].items[14].load_case=83
load_combinations[155].items[14].factor=0.19
load_combinations.create(156, design_situation="DS1", user_defined_name_enabled=True, name="Ult Operating Plant + 1.5 * Wind Wop y-", static_analysis_settings="SA2")
load_combinations[156].items[1].load_case=1
load_combinations[156].items[1].factor=1.2
load_combinations[156].items[2].load_case=2
load_combinations[156].items[2].factor=1.2
load_combinations[156].items[3].load_case=3
load_combinations[156].items[3].factor=1.2
load_combinations[156].items[4].load_case=11
load_combinations[156].items[4].factor=0.4
load_combinations[156].items[5].load_case=12
load_combinations[156].items[5].factor=0.6
load_combinations[156].items[6].load_case=14
load_combinations[156].items[6].factor=0.4
load_combinations[156].items[7].load_case=21
load_combinations[156].items[7].factor=1.0
load_combinations[156].items[8].load_case=24
load_combinations[156].items[8].factor=1.2
load_combinations[156].items[9].load_case=31
load_combinations[156].items[9].factor=1.2
load_combinations[156].items[10].load_case=33
load_combinations[156].items[10].factor=0.2
load_combinations[156].items[11].load_case=41
load_combinations[156].items[11].factor=1.2
load_combinations[156].items[12].load_case=43
load_combinations[156].items[12].factor=0.4
load_combinations[156].items[13].load_case=76
load_combinations[156].items[13].factor=0.19
load_combinations[156].items[14].load_case=84
load_combinations[156].items[14].factor=0.19
load_combinations.create(161, design_situation="DS1", user_defined_name_enabled=True, name="Ult Wind x+", static_analysis_settings="SA2")
load_combinations[161].items[1].load_case=1
load_combinations[161].items[1].factor=1.2
load_combinations[161].items[2].load_case=2
load_combinations[161].items[2].factor=1.2
load_combinations[161].items[3].load_case=3
load_combinations[161].items[3].factor=1.2
load_combinations[161].items[4].load_case=11
load_combinations[161].items[4].factor=0.4
load_combinations[161].items[5].load_case=12
load_combinations[161].items[5].factor=0.6
load_combinations[161].items[6].load_case=23
load_combinations[161].items[6].factor=1.2
load_combinations[161].items[7].load_case=31
load_combinations[161].items[7].factor=1.2
load_combinations[161].items[8].load_case=33
load_combinations[161].items[8].factor=0.2
load_combinations[161].items[9].load_case=71
load_combinations[161].items[9].factor=1.0
load_combinations[161].items[10].load_case=79
load_combinations[161].items[10].factor=1.0
load_combinations.create(162, design_situation="DS1", user_defined_name_enabled=True, name="Ult Wind x-", static_analysis_settings="SA2")
load_combinations[162].items[1].load_case=1
load_combinations[162].items[1].factor=1.2
load_combinations[162].items[2].load_case=2
load_combinations[162].items[2].factor=1.2
load_combinations[162].items[3].load_case=3
load_combinations[162].items[3].factor=1.2
load_combinations[162].items[4].load_case=11
load_combinations[162].items[4].factor=0.4
load_combinations[162].items[5].load_case=12
load_combinations[162].items[5].factor=0.6
load_combinations[162].items[6].load_case=23
load_combinations[162].items[6].factor=1.2
load_combinations[162].items[7].load_case=31
load_combinations[162].items[7].factor=1.2
load_combinations[162].items[8].load_case=33
load_combinations[162].items[8].factor=0.2
load_combinations[162].items[9].load_case=72
load_combinations[162].items[9].factor=1.0
load_combinations[162].items[10].load_case=80
load_combinations[162].items[10].factor=1.0
load_combinations.create(163, design_situation="DS1", user_defined_name_enabled=True, name="Ult Wind x+ uplift", static_analysis_settings="SA2")
load_combinations[163].items[1].load_case=1
load_combinations[163].items[1].factor=0.9
load_combinations[163].items[2].load_case=2
load_combinations[163].items[2].factor=0.9
load_combinations[163].items[3].load_case=3
load_combinations[163].items[3].factor=0.9
load_combinations[163].items[4].load_case=23
load_combinations[163].items[4].factor=0.9
load_combinations[163].items[5].load_case=73
load_combinations[163].items[5].factor=1.0
load_combinations[163].items[6].load_case=81
load_combinations[163].items[6].factor=1.0
load_combinations.create(164, design_situation="DS1", user_defined_name_enabled=True, name="Ult Wind x- uplift", static_analysis_settings="SA2")
load_combinations[164].items[1].load_case=1
load_combinations[164].items[1].factor=0.9
load_combinations[164].items[2].load_case=2
load_combinations[164].items[2].factor=0.9
load_combinations[164].items[3].load_case=3
load_combinations[164].items[3].factor=0.9
load_combinations[164].items[4].load_case=23
load_combinations[164].items[4].factor=0.9
load_combinations[164].items[5].load_case=74
load_combinations[164].items[5].factor=1.0
load_combinations[164].items[6].load_case=82
load_combinations[164].items[6].factor=1.0
load_combinations.create(165, design_situation="DS1", user_defined_name_enabled=True, name="Ult Wind y+", static_analysis_settings="SA2")
load_combinations[165].items[1].load_case=1
load_combinations[165].items[1].factor=1.2
load_combinations[165].items[2].load_case=2
load_combinations[165].items[2].factor=1.2
load_combinations[165].items[3].load_case=3
load_combinations[165].items[3].factor=1.2
load_combinations[165].items[4].load_case=11
load_combinations[165].items[4].factor=0.4
load_combinations[165].items[5].load_case=12
load_combinations[165].items[5].factor=0.6
load_combinations[165].items[6].load_case=23
load_combinations[165].items[6].factor=1.2
load_combinations[165].items[7].load_case=31
load_combinations[165].items[7].factor=1.2
load_combinations[165].items[8].load_case=33
load_combinations[165].items[8].factor=0.2
load_combinations[165].items[9].load_case=75
load_combinations[165].items[9].factor=1.0
load_combinations[165].items[10].load_case=83
load_combinations[165].items[10].factor=1.0
load_combinations.create(166, design_situation="DS1", user_defined_name_enabled=True, name="Ult Wind y-", static_analysis_settings="SA2")
load_combinations[166].items[1].load_case=1
load_combinations[166].items[1].factor=1.2
load_combinations[166].items[2].load_case=2
load_combinations[166].items[2].factor=1.2
load_combinations[166].items[3].load_case=3
load_combinations[166].items[3].factor=1.2
load_combinations[166].items[4].load_case=11
load_combinations[166].items[4].factor=0.4
load_combinations[166].items[5].load_case=12
load_combinations[166].items[5].factor=0.6
load_combinations[166].items[6].load_case=23
load_combinations[166].items[6].factor=1.2
load_combinations[166].items[7].load_case=31
load_combinations[166].items[7].factor=1.2
load_combinations[166].items[8].load_case=33
load_combinations[166].items[8].factor=0.2
load_combinations[166].items[9].load_case=76
load_combinations[166].items[9].factor=1.0
load_combinations[166].items[10].load_case=84
load_combinations[166].items[10].factor=1.0
load_combinations.create(167, design_situation="DS1", user_defined_name_enabled=True, name="Ult Wind y+ uplift", static_analysis_settings="SA2")
load_combinations[167].items[1].load_case=1
load_combinations[167].items[1].factor=0.9
load_combinations[167].items[2].load_case=2
load_combinations[167].items[2].factor=0.9
load_combinations[167].items[3].load_case=3
load_combinations[167].items[3].factor=0.9
load_combinations[167].items[4].load_case=23
load_combinations[167].items[4].factor=0.9
load_combinations[167].items[5].load_case=77
load_combinations[167].items[5].factor=1.0
load_combinations[167].items[6].load_case=85
load_combinations[167].items[6].factor=1.0
load_combinations.create(168, design_situation="DS1", user_defined_name_enabled=True, name="Ult Wind y- uplift", static_analysis_settings="SA2")
load_combinations[168].items[1].load_case=1
load_combinations[168].items[1].factor=0.9
load_combinations[168].items[2].load_case=2
load_combinations[168].items[2].factor=0.9
load_combinations[168].items[3].load_case=3
load_combinations[168].items[3].factor=0.9
load_combinations[168].items[4].load_case=23
load_combinations[168].items[4].factor=0.9
load_combinations[168].items[5].load_case=78
load_combinations[168].items[5].factor=1.0
load_combinations[168].items[6].load_case=86
load_combinations[168].items[6].factor=1.0
load_combinations.create(171, design_situation="DS1", user_defined_name_enabled=True, name="Ult EQ x+", static_analysis_settings="SA2")
load_combinations[171].items[1].load_case=1
load_combinations[171].items[1].factor=1.0
load_combinations[171].items[2].load_case=2
load_combinations[171].items[2].factor=1.0
load_combinations[171].items[3].load_case=3
load_combinations[171].items[3].factor=1.0
load_combinations[171].items[4].load_case=11
load_combinations[171].items[4].factor=0.3
load_combinations[171].items[5].load_case=12
load_combinations[171].items[5].factor=0.6
load_combinations[171].items[6].load_case=14
load_combinations[171].items[6].factor=0.3
load_combinations[171].items[7].load_case=21
load_combinations[171].items[7].factor=0.7
load_combinations[171].items[8].load_case=24
load_combinations[171].items[8].factor=1.0
load_combinations[171].items[9].load_case=31
load_combinations[171].items[9].factor=1.0
load_combinations[171].items[10].load_case=33
load_combinations[171].items[10].factor=0.2
load_combinations[171].items[11].load_case=41
load_combinations[171].items[11].factor=1.0
load_combinations[171].items[12].load_case=63
load_combinations[171].items[12].factor=1.0
load_combinations[171].items[13].load_case=64
load_combinations[171].items[13].factor=0.3
load_combinations.create(172, design_situation="DS1", user_defined_name_enabled=True, name="Ult EQ x+", static_analysis_settings="SA2")
load_combinations[172].items[1].load_case=1
load_combinations[172].items[1].factor=1.0
load_combinations[172].items[2].load_case=2
load_combinations[172].items[2].factor=1.0
load_combinations[172].items[3].load_case=3
load_combinations[172].items[3].factor=1.0
load_combinations[172].items[4].load_case=11
load_combinations[172].items[4].factor=0.3
load_combinations[172].items[5].load_case=12
load_combinations[172].items[5].factor=0.6
load_combinations[172].items[6].load_case=14
load_combinations[172].items[6].factor=0.3
load_combinations[172].items[7].load_case=21
load_combinations[172].items[7].factor=0.7
load_combinations[172].items[8].load_case=24
load_combinations[172].items[8].factor=1.0
load_combinations[172].items[9].load_case=31
load_combinations[172].items[9].factor=1.0
load_combinations[172].items[10].load_case=33
load_combinations[172].items[10].factor=0.2
load_combinations[172].items[11].load_case=41
load_combinations[172].items[11].factor=1.0
load_combinations[172].items[12].load_case=63
load_combinations[172].items[12].factor=1.0
load_combinations[172].items[13].load_case=64
load_combinations[172].items[13].factor=-0.3
load_combinations.create(173, design_situation="DS1", user_defined_name_enabled=True, name="Ult EQ x-", static_analysis_settings="SA2")
load_combinations[173].items[1].load_case=1
load_combinations[173].items[1].factor=1.0
load_combinations[173].items[2].load_case=2
load_combinations[173].items[2].factor=1.0
load_combinations[173].items[3].load_case=3
load_combinations[173].items[3].factor=1.0
load_combinations[173].items[4].load_case=11
load_combinations[173].items[4].factor=0.3
load_combinations[173].items[5].load_case=12
load_combinations[173].items[5].factor=0.6
load_combinations[173].items[6].load_case=14
load_combinations[173].items[6].factor=0.3
load_combinations[173].items[7].load_case=21
load_combinations[173].items[7].factor=0.7
load_combinations[173].items[8].load_case=24
load_combinations[173].items[8].factor=1.0
load_combinations[173].items[9].load_case=31
load_combinations[173].items[9].factor=1.0
load_combinations[173].items[10].load_case=33
load_combinations[173].items[10].factor=0.2
load_combinations[173].items[11].load_case=41
load_combinations[173].items[11].factor=1.0
load_combinations[173].items[12].load_case=63
load_combinations[173].items[12].factor=-1.0
load_combinations[173].items[13].load_case=64
load_combinations[173].items[13].factor=0.3
load_combinations.create(174, design_situation="DS1", user_defined_name_enabled=True, name="Ult EQ x-", static_analysis_settings="SA2")
load_combinations[174].items[1].load_case=1
load_combinations[174].items[1].factor=1.0
load_combinations[174].items[2].load_case=2
load_combinations[174].items[2].factor=1.0
load_combinations[174].items[3].load_case=3
load_combinations[174].items[3].factor=1.0
load_combinations[174].items[4].load_case=11
load_combinations[174].items[4].factor=0.3
load_combinations[174].items[5].load_case=12
load_combinations[174].items[5].factor=0.6
load_combinations[174].items[6].load_case=14
load_combinations[174].items[6].factor=0.3
load_combinations[174].items[7].load_case=21
load_combinations[174].items[7].factor=0.7
load_combinations[174].items[8].load_case=24
load_combinations[174].items[8].factor=1.0
load_combinations[174].items[9].load_case=31
load_combinations[174].items[9].factor=1.0
load_combinations[174].items[10].load_case=33
load_combinations[174].items[10].factor=0.2
load_combinations[174].items[11].load_case=41
load_combinations[174].items[11].factor=1.0
load_combinations[174].items[12].load_case=63
load_combinations[174].items[12].factor=-1.0
load_combinations[174].items[13].load_case=64
load_combinations[174].items[13].factor=-0.3
load_combinations.create(175, design_situation="DS1", user_defined_name_enabled=True, name="Ult EQ y+", static_analysis_settings="SA2")
load_combinations[175].items[1].load_case=1
load_combinations[175].items[1].factor=1.0
load_combinations[175].items[2].load_case=2
load_combinations[175].items[2].factor=1.0
load_combinations[175].items[3].load_case=3
load_combinations[175].items[3].factor=1.0
load_combinations[175].items[4].load_case=11
load_combinations[175].items[4].factor=0.3
load_combinations[175].items[5].load_case=12
load_combinations[175].items[5].factor=0.6
load_combinations[175].items[6].load_case=14
load_combinations[175].items[6].factor=0.3
load_combinations[175].items[7].load_case=21
load_combinations[175].items[7].factor=0.7
load_combinations[175].items[8].load_case=24
load_combinations[175].items[8].factor=1.0
load_combinations[175].items[9].load_case=31
load_combinations[175].items[9].factor=1.0
load_combinations[175].items[10].load_case=33
load_combinations[175].items[10].factor=0.2
load_combinations[175].items[11].load_case=41
load_combinations[175].items[11].factor=1.0
load_combinations[175].items[12].load_case=63
load_combinations[175].items[12].factor=0.3
load_combinations[175].items[13].load_case=64
load_combinations[175].items[13].factor=1.0
load_combinations.create(176, design_situation="DS1", user_defined_name_enabled=True, name="Ult EQ y+", static_analysis_settings="SA2")
load_combinations[176].items[1].load_case=1
load_combinations[176].items[1].factor=1.0
load_combinations[176].items[2].load_case=2
load_combinations[176].items[2].factor=1.0
load_combinations[176].items[3].load_case=3
load_combinations[176].items[3].factor=1.0
load_combinations[176].items[4].load_case=11
load_combinations[176].items[4].factor=0.3
load_combinations[176].items[5].load_case=12
load_combinations[176].items[5].factor=0.6
load_combinations[176].items[6].load_case=14
load_combinations[176].items[6].factor=0.3
load_combinations[176].items[7].load_case=21
load_combinations[176].items[7].factor=0.7
load_combinations[176].items[8].load_case=24
load_combinations[176].items[8].factor=1.0
load_combinations[176].items[9].load_case=31
load_combinations[176].items[9].factor=1.0
load_combinations[176].items[10].load_case=33
load_combinations[176].items[10].factor=0.2
load_combinations[176].items[11].load_case=41
load_combinations[176].items[11].factor=1.0
load_combinations[176].items[12].load_case=63
load_combinations[176].items[12].factor=-0.3
load_combinations[176].items[13].load_case=64
load_combinations[176].items[13].factor=1.0
load_combinations.create(177, design_situation="DS1", user_defined_name_enabled=True, name="Ult EQ y-", static_analysis_settings="SA2")
load_combinations[177].items[1].load_case=1
load_combinations[177].items[1].factor=1.0
load_combinations[177].items[2].load_case=2
load_combinations[177].items[2].factor=1.0
load_combinations[177].items[3].load_case=3
load_combinations[177].items[3].factor=1.0
load_combinations[177].items[4].load_case=11
load_combinations[177].items[4].factor=0.3
load_combinations[177].items[5].load_case=12
load_combinations[177].items[5].factor=0.6
load_combinations[177].items[6].load_case=14
load_combinations[177].items[6].factor=0.3
load_combinations[177].items[7].load_case=21
load_combinations[177].items[7].factor=0.7
load_combinations[177].items[8].load_case=24
load_combinations[177].items[8].factor=1.0
load_combinations[177].items[9].load_case=31
load_combinations[177].items[9].factor=1.0
load_combinations[177].items[10].load_case=33
load_combinations[177].items[10].factor=0.2
load_combinations[177].items[11].load_case=41
load_combinations[177].items[11].factor=1.0
load_combinations[177].items[12].load_case=63
load_combinations[177].items[12].factor=0.3
load_combinations[177].items[13].load_case=64
load_combinations[177].items[13].factor=-1.0
load_combinations.create(178, design_situation="DS1", user_defined_name_enabled=True, name="Ult EQ y-", static_analysis_settings="SA2")
load_combinations[178].items[1].load_case=1
load_combinations[178].items[1].factor=1.0
load_combinations[178].items[2].load_case=2
load_combinations[178].items[2].factor=1.0
load_combinations[178].items[3].load_case=3
load_combinations[178].items[3].factor=1.0
load_combinations[178].items[4].load_case=11
load_combinations[178].items[4].factor=0.3
load_combinations[178].items[5].load_case=12
load_combinations[178].items[5].factor=0.6
load_combinations[178].items[6].load_case=14
load_combinations[178].items[6].factor=0.3
load_combinations[178].items[7].load_case=21
load_combinations[178].items[7].factor=0.7
load_combinations[178].items[8].load_case=24
load_combinations[178].items[8].factor=1.0
load_combinations[178].items[9].load_case=31
load_combinations[178].items[9].factor=1.0
load_combinations[178].items[10].load_case=33
load_combinations[178].items[10].factor=0.2
load_combinations[178].items[11].load_case=41
load_combinations[178].items[11].factor=1.0
load_combinations[178].items[12].load_case=63
load_combinations[178].items[12].factor=-0.3
load_combinations[178].items[13].load_case=64
load_combinations[178].items[13].factor=-1.0
load_combinations.create(201, design_situation="DS1", user_defined_name_enabled=True, name="Service - No Crane + Wsx+", static_analysis_settings="SA2")
load_combinations[201].items[1].load_case=1
load_combinations[201].items[1].factor=1.0
load_combinations[201].items[2].load_case=2
load_combinations[201].items[2].factor=1.0
load_combinations[201].items[3].load_case=3
load_combinations[201].items[3].factor=1.0
load_combinations[201].items[4].load_case=11
load_combinations[201].items[4].factor=0.4
load_combinations[201].items[5].load_case=12
load_combinations[201].items[5].factor=0.6
load_combinations[201].items[6].load_case=14
load_combinations[201].items[6].factor=0.4
load_combinations[201].items[7].load_case=21
load_combinations[201].items[7].factor=0.7
load_combinations[201].items[8].load_case=24
load_combinations[201].items[8].factor=1.0
load_combinations[201].items[9].load_case=31
load_combinations[201].items[9].factor=1.0
load_combinations[201].items[10].load_case=33
load_combinations[201].items[10].factor=0.2
load_combinations[201].items[11].load_case=41
load_combinations[201].items[11].factor=1.0
load_combinations[201].items[12].load_case=71
load_combinations[201].items[12].factor=0.48
load_combinations[201].items[13].load_case=79
load_combinations[201].items[13].factor=0.48
load_combinations.create(202, design_situation="DS1", user_defined_name_enabled=True, name="Service - No Crane + Wsx-", static_analysis_settings="SA2")
load_combinations[202].items[1].load_case=1
load_combinations[202].items[1].factor=1.0
load_combinations[202].items[2].load_case=2
load_combinations[202].items[2].factor=1.0
load_combinations[202].items[3].load_case=3
load_combinations[202].items[3].factor=1.0
load_combinations[202].items[4].load_case=11
load_combinations[202].items[4].factor=0.4
load_combinations[202].items[5].load_case=12
load_combinations[202].items[5].factor=0.6
load_combinations[202].items[6].load_case=14
load_combinations[202].items[6].factor=0.4
load_combinations[202].items[7].load_case=21
load_combinations[202].items[7].factor=0.7
load_combinations[202].items[8].load_case=24
load_combinations[202].items[8].factor=1.0
load_combinations[202].items[9].load_case=31
load_combinations[202].items[9].factor=1.0
load_combinations[202].items[10].load_case=33
load_combinations[202].items[10].factor=0.2
load_combinations[202].items[11].load_case=41
load_combinations[202].items[11].factor=1.0
load_combinations[202].items[12].load_case=72
load_combinations[202].items[12].factor=0.48
load_combinations[202].items[13].load_case=80
load_combinations[202].items[13].factor=0.48
load_combinations.create(203, design_situation="DS1", user_defined_name_enabled=True, name="Service - No Crane + Wsy+", static_analysis_settings="SA2")
load_combinations[203].items[1].load_case=1
load_combinations[203].items[1].factor=1.0
load_combinations[203].items[2].load_case=2
load_combinations[203].items[2].factor=1.0
load_combinations[203].items[3].load_case=3
load_combinations[203].items[3].factor=1.0
load_combinations[203].items[4].load_case=11
load_combinations[203].items[4].factor=0.4
load_combinations[203].items[5].load_case=12
load_combinations[203].items[5].factor=0.6
load_combinations[203].items[6].load_case=14
load_combinations[203].items[6].factor=0.4
load_combinations[203].items[7].load_case=21
load_combinations[203].items[7].factor=0.7
load_combinations[203].items[8].load_case=24
load_combinations[203].items[8].factor=1.0
load_combinations[203].items[9].load_case=31
load_combinations[203].items[9].factor=1.0
load_combinations[203].items[10].load_case=33
load_combinations[203].items[10].factor=0.2
load_combinations[203].items[11].load_case=41
load_combinations[203].items[11].factor=1.0
load_combinations[203].items[12].load_case=75
load_combinations[203].items[12].factor=0.48
load_combinations[203].items[13].load_case=83
load_combinations[203].items[13].factor=0.48
load_combinations.create(204, design_situation="DS1", user_defined_name_enabled=True, name="Service - No Crane + Wsy-", static_analysis_settings="SA2")
load_combinations[204].items[1].load_case=1
load_combinations[204].items[1].factor=1.0
load_combinations[204].items[2].load_case=2
load_combinations[204].items[2].factor=1.0
load_combinations[204].items[3].load_case=3
load_combinations[204].items[3].factor=1.0
load_combinations[204].items[4].load_case=11
load_combinations[204].items[4].factor=0.4
load_combinations[204].items[5].load_case=12
load_combinations[204].items[5].factor=0.6
load_combinations[204].items[6].load_case=14
load_combinations[204].items[6].factor=0.4
load_combinations[204].items[7].load_case=21
load_combinations[204].items[7].factor=0.7
load_combinations[204].items[8].load_case=24
load_combinations[204].items[8].factor=1.0
load_combinations[204].items[9].load_case=31
load_combinations[204].items[9].factor=1.0
load_combinations[204].items[10].load_case=33
load_combinations[204].items[10].factor=0.2
load_combinations[204].items[11].load_case=41
load_combinations[204].items[11].factor=1.0
load_combinations[204].items[12].load_case=76
load_combinations[204].items[12].factor=0.48
load_combinations[204].items[13].load_case=84
load_combinations[204].items[13].factor=0.48
load_combinations.create(205, design_situation="DS1", user_defined_name_enabled=True, name="Service - No Crane + Wsx+", static_analysis_settings="SA2")
load_combinations[205].items[1].load_case=1
load_combinations[205].items[1].factor=1.0
load_combinations[205].items[2].load_case=2
load_combinations[205].items[2].factor=1.0
load_combinations[205].items[3].load_case=3
load_combinations[205].items[3].factor=1.0
load_combinations[205].items[4].load_case=11
load_combinations[205].items[4].factor=0.4
load_combinations[205].items[5].load_case=13
load_combinations[205].items[5].factor=0.6
load_combinations[205].items[6].load_case=14
load_combinations[205].items[6].factor=0.4
load_combinations[205].items[7].load_case=21
load_combinations[205].items[7].factor=0.7
load_combinations[205].items[8].load_case=24
load_combinations[205].items[8].factor=1.0
load_combinations[205].items[9].load_case=31
load_combinations[205].items[9].factor=1.0
load_combinations[205].items[10].load_case=33
load_combinations[205].items[10].factor=0.2
load_combinations[205].items[11].load_case=41
load_combinations[205].items[11].factor=1.0
load_combinations[205].items[12].load_case=71
load_combinations[205].items[12].factor=0.48
load_combinations[205].items[13].load_case=79
load_combinations[205].items[13].factor=0.48
load_combinations.create(206, design_situation="DS1", user_defined_name_enabled=True, name="Service - No Crane + Wsx-", static_analysis_settings="SA2")
load_combinations[206].items[1].load_case=1
load_combinations[206].items[1].factor=1.0
load_combinations[206].items[2].load_case=2
load_combinations[206].items[2].factor=1.0
load_combinations[206].items[3].load_case=3
load_combinations[206].items[3].factor=1.0
load_combinations[206].items[4].load_case=11
load_combinations[206].items[4].factor=0.4
load_combinations[206].items[5].load_case=13
load_combinations[206].items[5].factor=0.6
load_combinations[206].items[6].load_case=14
load_combinations[206].items[6].factor=0.4
load_combinations[206].items[7].load_case=21
load_combinations[206].items[7].factor=0.7
load_combinations[206].items[8].load_case=24
load_combinations[206].items[8].factor=1.0
load_combinations[206].items[9].load_case=31
load_combinations[206].items[9].factor=1.0
load_combinations[206].items[10].load_case=33
load_combinations[206].items[10].factor=0.2
load_combinations[206].items[11].load_case=41
load_combinations[206].items[11].factor=1.0
load_combinations[206].items[12].load_case=72
load_combinations[206].items[12].factor=0.48
load_combinations[206].items[13].load_case=80
load_combinations[206].items[13].factor=0.48
load_combinations.create(207, design_situation="DS1", user_defined_name_enabled=True, name="Service - No Crane + Wsy+", static_analysis_settings="SA2")
load_combinations[207].items[1].load_case=1
load_combinations[207].items[1].factor=1.0
load_combinations[207].items[2].load_case=2
load_combinations[207].items[2].factor=1.0
load_combinations[207].items[3].load_case=3
load_combinations[207].items[3].factor=1.0
load_combinations[207].items[4].load_case=11
load_combinations[207].items[4].factor=0.4
load_combinations[207].items[5].load_case=13
load_combinations[207].items[5].factor=0.6
load_combinations[207].items[6].load_case=14
load_combinations[207].items[6].factor=0.4
load_combinations[207].items[7].load_case=21
load_combinations[207].items[7].factor=0.7
load_combinations[207].items[8].load_case=24
load_combinations[207].items[8].factor=1.0
load_combinations[207].items[9].load_case=31
load_combinations[207].items[9].factor=1.0
load_combinations[207].items[10].load_case=33
load_combinations[207].items[10].factor=0.2
load_combinations[207].items[11].load_case=41
load_combinations[207].items[11].factor=1.0
load_combinations[207].items[12].load_case=75
load_combinations[207].items[12].factor=0.48
load_combinations[207].items[13].load_case=83
load_combinations[207].items[13].factor=0.48
load_combinations.create(208, design_situation="DS1", user_defined_name_enabled=True, name="Service - No Crane + Wsy-", static_analysis_settings="SA2")
load_combinations[208].items[1].load_case=1
load_combinations[208].items[1].factor=1.0
load_combinations[208].items[2].load_case=2
load_combinations[208].items[2].factor=1.0
load_combinations[208].items[3].load_case=3
load_combinations[208].items[3].factor=1.0
load_combinations[208].items[4].load_case=11
load_combinations[208].items[4].factor=0.4
load_combinations[208].items[5].load_case=13
load_combinations[208].items[5].factor=0.6
load_combinations[208].items[6].load_case=14
load_combinations[208].items[6].factor=0.4
load_combinations[208].items[7].load_case=21
load_combinations[208].items[7].factor=0.7
load_combinations[208].items[8].load_case=24
load_combinations[208].items[8].factor=1.0
load_combinations[208].items[9].load_case=31
load_combinations[208].items[9].factor=1.0
load_combinations[208].items[10].load_case=33
load_combinations[208].items[10].factor=0.2
load_combinations[208].items[11].load_case=41
load_combinations[208].items[11].factor=1.0
load_combinations[208].items[12].load_case=76
load_combinations[208].items[12].factor=0.48
load_combinations[208].items[13].load_case=84
load_combinations[208].items[13].factor=0.48
load_combinations.create(211, design_situation="DS1", user_defined_name_enabled=True, name="Service - Crane + Wocx+ + thermal", static_analysis_settings="SA2")
load_combinations[211].items[1].load_case=1
load_combinations[211].items[1].factor=1.0
load_combinations[211].items[2].load_case=2
load_combinations[211].items[2].factor=1.0
load_combinations[211].items[3].load_case=3
load_combinations[211].items[3].factor=1.0
load_combinations[211].items[4].load_case=11
load_combinations[211].items[4].factor=0.4
load_combinations[211].items[5].load_case=12
load_combinations[211].items[5].factor=0.6
load_combinations[211].items[6].load_case=14
load_combinations[211].items[6].factor=0.4
load_combinations[211].items[7].load_case=21
load_combinations[211].items[7].factor=0.7
load_combinations[211].items[8].load_case=23
load_combinations[211].items[8].factor=1.0
load_combinations[211].items[9].load_case=31
load_combinations[211].items[9].factor=1.0
load_combinations[211].items[10].load_case=33
load_combinations[211].items[10].factor=0.2
load_combinations[211].items[11].load_case=43
load_combinations[211].items[11].factor=1.0
load_combinations[211].items[12].load_case=61
load_combinations[211].items[12].factor=1.0
load_combinations[211].items[13].load_case=71
load_combinations[211].items[13].factor=0.12
load_combinations[211].items[14].load_case=79
load_combinations[211].items[14].factor=0.12
load_combinations.create(213, design_situation="DS1", user_defined_name_enabled=True, name="Service - Crane + Wocx-  + thermal", static_analysis_settings="SA2")
load_combinations[213].items[1].load_case=1
load_combinations[213].items[1].factor=1.0
load_combinations[213].items[2].load_case=2
load_combinations[213].items[2].factor=1.0
load_combinations[213].items[3].load_case=3
load_combinations[213].items[3].factor=1.0
load_combinations[213].items[4].load_case=11
load_combinations[213].items[4].factor=0.4
load_combinations[213].items[5].load_case=12
load_combinations[213].items[5].factor=0.6
load_combinations[213].items[6].load_case=14
load_combinations[213].items[6].factor=0.4
load_combinations[213].items[7].load_case=21
load_combinations[213].items[7].factor=0.7
load_combinations[213].items[8].load_case=23
load_combinations[213].items[8].factor=1.0
load_combinations[213].items[9].load_case=31
load_combinations[213].items[9].factor=1.0
load_combinations[213].items[10].load_case=33
load_combinations[213].items[10].factor=0.2
load_combinations[213].items[11].load_case=43
load_combinations[213].items[11].factor=1.0
load_combinations[213].items[12].load_case=61
load_combinations[213].items[12].factor=1.0
load_combinations[213].items[13].load_case=72
load_combinations[213].items[13].factor=0.12
load_combinations[213].items[14].load_case=80
load_combinations[213].items[14].factor=0.12
load_combinations.create(215, design_situation="DS1", user_defined_name_enabled=True, name="Service - Crane + Wocy+ + thermal", static_analysis_settings="SA2")
load_combinations[215].items[1].load_case=1
load_combinations[215].items[1].factor=1.0
load_combinations[215].items[2].load_case=2
load_combinations[215].items[2].factor=1.0
load_combinations[215].items[3].load_case=3
load_combinations[215].items[3].factor=1.0
load_combinations[215].items[4].load_case=11
load_combinations[215].items[4].factor=0.4
load_combinations[215].items[5].load_case=12
load_combinations[215].items[5].factor=0.6
load_combinations[215].items[6].load_case=14
load_combinations[215].items[6].factor=0.4
load_combinations[215].items[7].load_case=21
load_combinations[215].items[7].factor=0.7
load_combinations[215].items[8].load_case=23
load_combinations[215].items[8].factor=1.0
load_combinations[215].items[9].load_case=31
load_combinations[215].items[9].factor=1.0
load_combinations[215].items[10].load_case=33
load_combinations[215].items[10].factor=0.2
load_combinations[215].items[11].load_case=43
load_combinations[215].items[11].factor=1.0
load_combinations[215].items[12].load_case=61
load_combinations[215].items[12].factor=1.0
load_combinations[215].items[13].load_case=75
load_combinations[215].items[13].factor=0.12
load_combinations[215].items[14].load_case=83
load_combinations[215].items[14].factor=0.12
load_combinations.create(217, design_situation="DS1", user_defined_name_enabled=True, name="Service - Crane + Wocy- + thermal", static_analysis_settings="SA2")
load_combinations[217].items[1].load_case=1
load_combinations[217].items[1].factor=1.0
load_combinations[217].items[2].load_case=2
load_combinations[217].items[2].factor=1.0
load_combinations[217].items[3].load_case=3
load_combinations[217].items[3].factor=1.0
load_combinations[217].items[4].load_case=11
load_combinations[217].items[4].factor=0.4
load_combinations[217].items[5].load_case=12
load_combinations[217].items[5].factor=0.6
load_combinations[217].items[6].load_case=14
load_combinations[217].items[6].factor=0.4
load_combinations[217].items[7].load_case=21
load_combinations[217].items[7].factor=0.7
load_combinations[217].items[8].load_case=23
load_combinations[217].items[8].factor=1.0
load_combinations[217].items[9].load_case=31
load_combinations[217].items[9].factor=1.0
load_combinations[217].items[10].load_case=33
load_combinations[217].items[10].factor=0.2
load_combinations[217].items[11].load_case=43
load_combinations[217].items[11].factor=1.0
load_combinations[217].items[12].load_case=61
load_combinations[217].items[12].factor=1.0
load_combinations[217].items[13].load_case=76
load_combinations[217].items[13].factor=0.12
load_combinations[217].items[14].load_case=84
load_combinations[217].items[14].factor=0.12
load_combinations.create(991, design_situation="DS1", user_defined_name_enabled=True, name="EQ All G", static_analysis_settings="SA2")
load_combinations[991].items[1].load_case=1
load_combinations[991].items[1].factor=1.0
load_combinations[991].items[2].load_case=2
load_combinations[991].items[2].factor=1.0
load_combinations[991].items[3].load_case=3
load_combinations[991].items[3].factor=1.0
load_combinations.create(992, design_situation="DS1", user_defined_name_enabled=True, name="EQ All Q", static_analysis_settings="SA2")
load_combinations[992].items[1].load_case=1
load_combinations[992].items[1].factor=1.0
load_combinations[992].items[2].load_case=2
load_combinations[992].items[2].factor=1.0
load_combinations[992].items[3].load_case=3
load_combinations[992].items[3].factor=1.0
load_combinations[992].items[4].load_case=11
load_combinations[992].items[4].factor=0.3
load_combinations[992].items[5].load_case=12
load_combinations[992].items[5].factor=0.6
load_combinations[992].items[6].load_case=14
load_combinations[992].items[6].factor=0.3
load_combinations[992].items[7].load_case=21
load_combinations[992].items[7].factor=0.7
load_combinations[992].items[8].load_case=24
load_combinations[992].items[8].factor=1.0
load_combinations[992].items[9].load_case=31
load_combinations[992].items[9].factor=1.0
load_combinations[992].items[10].load_case=33
load_combinations[992].items[10].factor=0.2
load_combinations[992].items[11].load_case=41
load_combinations[992].items[11].factor=1.0
load_combinations.create(993, design_situation="DS1", user_defined_name_enabled=True, name="EQ MASS", static_analysis_settings="SA2")
load_combinations[993].items[1].load_case=1
load_combinations[993].items[1].factor=1.0
load_combinations[993].items[2].load_case=2
load_combinations[993].items[2].factor=1.0
load_combinations[993].items[3].load_case=3
load_combinations[993].items[3].factor=1.0
load_combinations[993].items[4].load_case=11
load_combinations[993].items[4].factor=0.3
load_combinations[993].items[5].load_case=12
load_combinations[993].items[5].factor=0.6
load_combinations[993].items[6].load_case=14
load_combinations[993].items[6].factor=0.3
load_combinations[993].items[7].load_case=21
load_combinations[993].items[7].factor=0.7
load_combinations[993].items[8].load_case=24
load_combinations[993].items[8].factor=1.0
load_combinations[993].items[9].load_case=31
load_combinations[993].items[9].factor=1.0
load_combinations[993].items[10].load_case=41
load_combinations[993].items[10].factor=1.0

