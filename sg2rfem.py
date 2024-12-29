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
materials.create(2, name="dummy_steel", definition_type="E | (G) | ν")

# Create Sections

sections.create_standardized_steel(1, "150 UB 14.0")
sections.create_standardized_steel(40, "40diaRod")
sections.create_standardized_steel(65, "65*5 EA")
sections.create_standardized_steel(75, "75*6 EA")
sections.create_standardized_steel(90, "90*8 EA")
sections.create_standardized_steel(100, "100*10 EA")
sections.create_standardized_steel(102, "101.6*5 CHS")
sections.create_standardized_steel(114, "114.3*4.5 CHS")
sections.create_standardized_steel(125, "125*10 EA")
sections.create_standardized_steel(140, "139.7*5.4 CHS")
sections.create_standardized_steel(150, "150 PFC")
sections.create_standardized_steel(151, "150 UC 30.0")
sections.create_standardized_steel(152, "150*90*8 UA")
sections.create_standardized_steel(168, "168.3x6.4 CHS")
sections.create_standardized_steel(201, "200 UC 46.2")
sections.create_standardized_steel(202, "200 UB 25.4")
sections.create_standardized_steel(203, "200 PFC")
sections.create_standardized_steel(219, "219.1x6.4 CHS")
sections.create_standardized_steel(250, "250 UB 31.4")
sections.create_standardized_steel(251, "250 PFC")
sections.create_standardized_steel(252, "250 UC 72.9")
sections.create_standardized_steel(301, "310 UB 40.4")
sections.create_standardized_steel(350, "360 UB 44.7")
sections.create_standardized_steel(401, "410 UB 53.7")
sections.create_standardized_steel(460, "460 UB 67.1")
sections.create_standardized_steel(530, "530 UB 92.4")
sections.create_standardized_steel(531, "530 UB 82.0")
sections.create_standardized_steel(680, "PullyDum")
sections.create_standardized_steel(700, "700 WB 130")
sections.create_standardized_steel(701, "700 WB 115")
sections.create_standardized_steel(1001, "610ub125_300PFC")
sections.create_standardized_steel(1002, "250*6shs_dum")

# Create Nodes
nodes.create_standard( 1, 0.0, 0.0, 0.0)
nodes.create_standard( 2, 3.17062643365463, 0.0, -0.883746256094687)
nodes.create_standard( 3, 3.17062643365463, 0.0, 3.77278140300982)
nodes.create_standard( 4, 3.08936348356984, 0.713235759181138, -0.883746256094687)
nodes.create_standard( 5, 3.08936348356984, 0.713235759181138, 3.77278140300982)
nodes.create_standard( 6, 2.84974016160754, 1.38991114576094, -0.883746256094687)
nodes.create_standard( 7, 2.84974016160754, 1.38991114576094, 3.77278140300982)
nodes.create_standard( 8, 2.46403952820341, 1.99533986710048, -0.883746256094687)
nodes.create_standard( 9, 2.46403952820341, 1.99533986710048, 3.77278140300982)
nodes.create_standard( 10, 1.95203254785034, 2.49848772538958, -0.883746256094687)
nodes.create_standard( 11, 1.95203254785034, 2.49848772538958, 3.77278140300982)
nodes.create_standard( 12, 1.33996463202023, 2.87356342660543, -0.883746256094687)
nodes.create_standard( 13, 1.33996463202023, 2.87356342660543, 3.77278140300982)
nodes.create_standard( 14, 0.659210302772616, 3.10134063890246, -0.883746256094687)
nodes.create_standard( 15, 0.659210302772616, 3.10134063890246, 3.77278140300982)
nodes.create_standard( 16, -0.0553350611809352, 3.17014353189151, -0.883746256094687)
nodes.create_standard( 17, -0.0553350611809352, 3.17014353189151, 3.77278140300982)
nodes.create_standard( 18, -0.767043957068143, 3.07644527819279, -0.883746256094687)
nodes.create_standard( 19, -0.767043957068143, 3.07644527819279, 3.77278140300982)
nodes.create_standard( 20, -1.43943427910228, 2.82504883815037, -0.883746256094687)
nodes.create_standard( 21, -1.43943427910228, 2.82504883815037, 3.77278140300982)
nodes.create_standard( 22, -2.03803938649782, 2.42884076070727, -0.883746256094687)
nodes.create_standard( 23, -2.03803938649782, 2.42884076070727, 3.77278140300982)
nodes.create_standard( 24, -2.5321748590112, 1.90813062057636, -0.883746256094687)
nodes.create_standard( 25, -2.5321748590112, 1.90813062057636, 3.77278140300982)
nodes.create_standard( 26, -2.89651137634675, 1.28960995207208, -0.883746256094687)
nodes.create_standard( 27, -2.89651137634675, 1.28960995207208, 3.77278140300982)
nodes.create_standard( 28, -3.11237309583311, 0.604984044519956, -0.883746256094687)
nodes.create_standard( 29, -3.11237309583311, 0.604984044519956, 3.77278140300982)
nodes.create_standard( 30, -3.16869497369871, -0.110653266766192, -0.883746256094687)
nodes.create_standard( 31, -3.16869497369871, -0.110653266766192, 3.77278140300982)
nodes.create_standard( 32, -3.06258995778181, -0.820618505935303, -0.883746256094687)
nodes.create_standard( 33, -3.06258995778181, -0.820618505935303, 3.77278140300982)
nodes.create_standard( 34, -2.79949697745024, -1.4885189468181, -0.883746256094687)
nodes.create_standard( 35, -2.79949697745024, -1.4885189468181, 3.77278140300982)
nodes.create_standard( 36, -2.39290214478671, -2.08011809935509, -0.883746256094687)
nodes.create_standard( 37, -2.39290214478671, -2.08011809935509, 3.77278140300982)
nodes.create_standard( 38, -1.86364745823087, -2.56509066764103, -0.883746256094687)
nodes.create_standard( 39, -1.86364745823087, -2.56509066764103, 3.77278140300982)
nodes.create_standard( 40, -1.2388624444398, -2.91857702066369, -0.883746256094687)
nodes.create_standard( 41, -1.2388624444398, -2.91857702066369, 3.77278140300982)
nodes.create_standard( 42, -0.550573502266725, -3.12245749376853, -0.883746256094687)
nodes.create_standard( 43, -0.550573502266725, -3.12245749376853, 3.77278140300982)
nodes.create_standard( 44, 0.16593776629447, -3.16628120032108, -0.883746256094687)
nodes.create_standard( 45, 0.16593776629447, -3.16628120032108, 3.77278140300982)
nodes.create_standard( 46, 0.873943086456045, -3.04780174280171, -0.883746256094687)
nodes.create_standard( 47, 0.873943086456045, -3.04780174280171, 3.77278140300982)
nodes.create_standard( 48, 1.5371501972431, -2.77309236285144, -0.883746256094687)
nodes.create_standard( 49, 1.5371501972431, -2.77309236285144, 3.77278140300982)

 # Create Member Hinges# Create Lines

lines.create_polyline(1, "1,2")
lines.create_polyline(2, "2,3")
lines.create_polyline(3, "4,5")
lines.create_polyline(4, "6,7")
lines.create_polyline(5, "8,9")
lines.create_polyline(6, "10,11")
lines.create_polyline(7, "12,13")
lines.create_polyline(8, "14,15")
lines.create_polyline(9, "16,17")
lines.create_polyline(10, "18,19")
lines.create_polyline(11, "20,21")
lines.create_polyline(12, "22,23")
lines.create_polyline(13, "24,25")
lines.create_polyline(14, "26,27")
lines.create_polyline(15, "28,29")
lines.create_polyline(16, "30,31")
lines.create_polyline(17, "32,33")
lines.create_polyline(18, "34,35")
lines.create_polyline(19, "36,37")
lines.create_polyline(20, "38,39")
lines.create_polyline(21, "40,41")
lines.create_polyline(22, "42,43")
lines.create_polyline(23, "44,45")
lines.create_polyline(24, "46,47")
lines.create_polyline(25, "48,49")


# Create Members 
members.create_beam(1, "1", line="1", rotation_angle=-1.5707963267948966)
members.create_beam(2, "1", line="2", rotation_angle=3.141592653589793)
members.create_beam(3, "1", line="3", rotation_angle=-2.9146998508305306)
members.create_beam(4, "1", line="4", rotation_angle=-2.6878070480712677)
members.create_beam(5, "1", line="5", rotation_angle=-2.4609142453120043)
members.create_beam(6, "1", line="6", rotation_angle=-2.234021442552742)
members.create_beam(7, "1", line="7", rotation_angle=-2.007128639793479)
members.create_beam(8, "1", line="8", rotation_angle=-1.780235837034216)
members.create_beam(9, "1", line="9", rotation_angle=-1.5533430342749535)
members.create_beam(10, "1", line="10", rotation_angle=-1.32645023151569)
members.create_beam(11, "1", line="11", rotation_angle=-1.0995574287564278)
members.create_beam(12, "1", line="12", rotation_angle=-0.8726646259971635)
members.create_beam(13, "1", line="13", rotation_angle=-0.6457718232379018)
members.create_beam(14, "1", line="14", rotation_angle=-0.41887902047863834)
members.create_beam(15, "1", line="15", rotation_angle=-0.1919862177193767)
members.create_beam(16, "1", line="16", rotation_angle=0.03490658503988567)
members.create_beam(17, "1", line="17", rotation_angle=0.26179938779914974)
members.create_beam(18, "1", line="18", rotation_angle=0.48869219055841384)
members.create_beam(19, "1", line="19", rotation_angle=0.7155849933176749)
members.create_beam(20, "1", line="20", rotation_angle=0.9424777960769388)
members.create_beam(21, "1", line="21", rotation_angle=1.1693705988361995)
members.create_beam(22, "1", line="22", rotation_angle=1.3962634015954638)
members.create_beam(23, "1", line="23", rotation_angle=1.6231562043547265)
members.create_beam(24, "1", line="24", rotation_angle=1.8500490071139897)
members.create_beam(25, "1", line="25", rotation_angle=2.0769418098732526)

# Create Static Analysis Settings
static_analysis_settings.create(1)
static_analysis_settings.create(2, analysis_type="Second-order (P-Δ)")

# Create Load Cases
load_cases.create(1, name="G(SW) - Structure Self Weight", static_analysis_settings="SA1", to_solve=False)
load_cases.create(2, name="G(SD) - Structural Dead Loads", static_analysis_settings="SA1", to_solve=False)
load_cases.create(3, name="G(EQ) - Equipment Dead Loads", static_analysis_settings="SA1", to_solve=False)
load_cases.create(10, name="Q(rLL) Roof live load", static_analysis_settings="SA1", to_solve=False)
load_cases.create(11, name="Q(L) - General Floor Loads", static_analysis_settings="SA1", to_solve=False)
load_cases.create(12, name="Q(S) - Pipe and Elec. Services", static_analysis_settings="SA1", to_solve=False)
load_cases.create(13, name="Q(SP) - Material Spillage", static_analysis_settings="SA1", to_solve=False)
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
load_cases.create(64, name="Eu(z) Earthquake in +y direction", static_analysis_settings="SA1", to_solve=False)
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
load_combinations[111].items[6].load_case=21
load_combinations[111].items[6].factor=1.0
load_combinations[111].items[7].load_case=24
load_combinations[111].items[7].factor=1.2
load_combinations[111].items[8].load_case=33
load_combinations[111].items[8].factor=0.2
load_combinations[111].items[9].load_case=41
load_combinations[111].items[9].factor=1.2
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
load_combinations[112].items[6].load_case=21
load_combinations[112].items[6].factor=1.0
load_combinations[112].items[7].load_case=24
load_combinations[112].items[7].factor=1.2
load_combinations[112].items[8].load_case=33
load_combinations[112].items[8].factor=0.2
load_combinations[112].items[9].load_case=41
load_combinations[112].items[9].factor=1.2
load_combinations.create(113, design_situation="DS1", user_defined_name_enabled=True, name="Ult Roof Live Load Extreme", static_analysis_settings="SA2")
load_combinations[113].items[1].load_case=1
load_combinations[113].items[1].factor=1.2
load_combinations[113].items[2].load_case=2
load_combinations[113].items[2].factor=1.2
load_combinations[113].items[3].load_case=3
load_combinations[113].items[3].factor=1.2
load_combinations[113].items[4].load_case=10
load_combinations[113].items[4].factor=1.5
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
load_combinations[121].items[6].load_case=22
load_combinations[121].items[6].factor=1.2
load_combinations[121].items[7].load_case=25
load_combinations[121].items[7].factor=1.5
load_combinations[121].items[8].load_case=33
load_combinations[121].items[8].factor=1.2
load_combinations[121].items[9].load_case=41
load_combinations[121].items[9].factor=1.2
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
load_combinations[122].items[6].load_case=22
load_combinations[122].items[6].factor=1.2
load_combinations[122].items[7].load_case=23
load_combinations[122].items[7].factor=0.9
load_combinations[122].items[8].load_case=33
load_combinations[122].items[8].factor=0.2
load_combinations[122].items[9].load_case=41
load_combinations[122].items[9].factor=1.2
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
load_combinations[131].items[6].load_case=21
load_combinations[131].items[6].factor=1.0
load_combinations[131].items[7].load_case=23
load_combinations[131].items[7].factor=1.2
load_combinations[131].items[8].load_case=33
load_combinations[131].items[8].factor=1.2
load_combinations.create(132, design_situation="DS1", user_defined_name_enabled=True, name="Ult Equipment Extreme - uplift", static_analysis_settings="SA2")
load_combinations[132].items[1].load_case=1
load_combinations[132].items[1].factor=0.9
load_combinations[132].items[2].load_case=2
load_combinations[132].items[2].factor=0.9
load_combinations[132].items[3].load_case=3
load_combinations[132].items[3].factor=0.9
load_combinations[132].items[4].load_case=23
load_combinations[132].items[4].factor=0.9
load_combinations.create(141, design_situation="DS1", user_defined_name_enabled=True, name="Ult Crane - plant not operating", static_analysis_settings="SA2")
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
load_combinations[141].items[6].load_case=23
load_combinations[141].items[6].factor=1.2
load_combinations[141].items[7].load_case=33
load_combinations[141].items[7].factor=0.2
load_combinations[141].items[8].load_case=71
load_combinations[141].items[8].factor=0.17
load_combinations[141].items[9].load_case=79
load_combinations[141].items[9].factor=0.17
load_combinations.create(142, design_situation="DS1", user_defined_name_enabled=True, name="Ult Crane - plant not operating", static_analysis_settings="SA2")
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
load_combinations[142].items[6].load_case=23
load_combinations[142].items[6].factor=1.2
load_combinations[142].items[7].load_case=33
load_combinations[142].items[7].factor=0.2
load_combinations[142].items[8].load_case=72
load_combinations[142].items[8].factor=0.17
load_combinations[142].items[9].load_case=80
load_combinations[142].items[9].factor=0.17
load_combinations.create(143, design_situation="DS1", user_defined_name_enabled=True, name="Ult Crane - plant not operating", static_analysis_settings="SA2")
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
load_combinations[143].items[6].load_case=23
load_combinations[143].items[6].factor=1.2
load_combinations[143].items[7].load_case=33
load_combinations[143].items[7].factor=0.2
load_combinations[143].items[8].load_case=75
load_combinations[143].items[8].factor=0.17
load_combinations[143].items[9].load_case=83
load_combinations[143].items[9].factor=0.17
load_combinations.create(144, design_situation="DS1", user_defined_name_enabled=True, name="Ult Crane - plant not operating", static_analysis_settings="SA2")
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
load_combinations[144].items[6].load_case=23
load_combinations[144].items[6].factor=1.2
load_combinations[144].items[7].load_case=33
load_combinations[144].items[7].factor=0.2
load_combinations[144].items[8].load_case=76
load_combinations[144].items[8].factor=0.17
load_combinations.create(145, design_situation="DS1", user_defined_name_enabled=True, name="Ult Crane - plant not operating, uplift", static_analysis_settings="SA2")
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
load_combinations[145].items[6].load_case=73
load_combinations[145].items[6].factor=0.17
load_combinations.create(146, design_situation="DS1", user_defined_name_enabled=True, name="Ult Crane - plant not operating, uplift", static_analysis_settings="SA2")
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
load_combinations[146].items[6].load_case=74
load_combinations[146].items[6].factor=0.17
load_combinations.create(147, design_situation="DS1", user_defined_name_enabled=True, name="Ult Crane - plant not operating, uplift", static_analysis_settings="SA2")
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
load_combinations[147].items[6].load_case=77
load_combinations[147].items[6].factor=0.17
load_combinations.create(148, design_situation="DS1", user_defined_name_enabled=True, name="Ult Crane - plant not operating, uplift", static_analysis_settings="SA2")
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
load_combinations[148].items[6].load_case=78
load_combinations[148].items[6].factor=0.17
load_combinations[148].items[7].load_case=86
load_combinations[148].items[7].factor=0.17
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
load_combinations[151].items[6].load_case=21
load_combinations[151].items[6].factor=1.0
load_combinations[151].items[7].load_case=24
load_combinations[151].items[7].factor=1.2
load_combinations[151].items[8].load_case=33
load_combinations[151].items[8].factor=0.2
load_combinations[151].items[9].load_case=41
load_combinations[151].items[9].factor=1.2
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
load_combinations[152].items[6].load_case=21
load_combinations[152].items[6].factor=1.0
load_combinations[152].items[7].load_case=24
load_combinations[152].items[7].factor=1.2
load_combinations[152].items[8].load_case=33
load_combinations[152].items[8].factor=0.2
load_combinations[152].items[9].load_case=41
load_combinations[152].items[9].factor=1.2
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
load_combinations[153].items[6].load_case=21
load_combinations[153].items[6].factor=1.0
load_combinations[153].items[7].load_case=24
load_combinations[153].items[7].factor=1.2
load_combinations[153].items[8].load_case=33
load_combinations[153].items[8].factor=0.2
load_combinations[153].items[9].load_case=41
load_combinations[153].items[9].factor=1.2
load_combinations[153].items[10].load_case=71
load_combinations[153].items[10].factor=0.4
load_combinations[153].items[11].load_case=79
load_combinations[153].items[11].factor=0.4
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
load_combinations[154].items[6].load_case=21
load_combinations[154].items[6].factor=1.0
load_combinations[154].items[7].load_case=24
load_combinations[154].items[7].factor=1.2
load_combinations[154].items[8].load_case=33
load_combinations[154].items[8].factor=0.2
load_combinations[154].items[9].load_case=41
load_combinations[154].items[9].factor=1.2
load_combinations[154].items[10].load_case=72
load_combinations[154].items[10].factor=0.4
load_combinations[154].items[11].load_case=80
load_combinations[154].items[11].factor=0.4
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
load_combinations[155].items[6].load_case=21
load_combinations[155].items[6].factor=1.0
load_combinations[155].items[7].load_case=24
load_combinations[155].items[7].factor=1.2
load_combinations[155].items[8].load_case=33
load_combinations[155].items[8].factor=0.2
load_combinations[155].items[9].load_case=41
load_combinations[155].items[9].factor=1.2
load_combinations[155].items[10].load_case=75
load_combinations[155].items[10].factor=0.4
load_combinations[155].items[11].load_case=83
load_combinations[155].items[11].factor=0.4
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
load_combinations[156].items[6].load_case=21
load_combinations[156].items[6].factor=1.0
load_combinations[156].items[7].load_case=24
load_combinations[156].items[7].factor=1.2
load_combinations[156].items[8].load_case=33
load_combinations[156].items[8].factor=0.2
load_combinations[156].items[9].load_case=41
load_combinations[156].items[9].factor=1.2
load_combinations[156].items[10].load_case=76
load_combinations[156].items[10].factor=0.4
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
load_combinations[161].items[7].load_case=33
load_combinations[161].items[7].factor=0.2
load_combinations[161].items[8].load_case=71
load_combinations[161].items[8].factor=1.0
load_combinations[161].items[9].load_case=79
load_combinations[161].items[9].factor=1.0
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
load_combinations[162].items[7].load_case=33
load_combinations[162].items[7].factor=0.2
load_combinations[162].items[8].load_case=72
load_combinations[162].items[8].factor=1.0
load_combinations[162].items[9].load_case=80
load_combinations[162].items[9].factor=1.0
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
load_combinations[165].items[7].load_case=33
load_combinations[165].items[7].factor=0.2
load_combinations[165].items[8].load_case=75
load_combinations[165].items[8].factor=1.0
load_combinations[165].items[9].load_case=83
load_combinations[165].items[9].factor=1.0
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
load_combinations[166].items[7].load_case=33
load_combinations[166].items[7].factor=0.2
load_combinations[166].items[8].load_case=76
load_combinations[166].items[8].factor=1.0
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
load_combinations[171].items[6].load_case=21
load_combinations[171].items[6].factor=0.7
load_combinations[171].items[7].load_case=24
load_combinations[171].items[7].factor=1.0
load_combinations[171].items[8].load_case=33
load_combinations[171].items[8].factor=0.2
load_combinations[171].items[9].load_case=41
load_combinations[171].items[9].factor=1.0
load_combinations[171].items[10].load_case=63
load_combinations[171].items[10].factor=1.0
load_combinations[171].items[11].load_case=64
load_combinations[171].items[11].factor=0.3
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
load_combinations[172].items[6].load_case=21
load_combinations[172].items[6].factor=0.7
load_combinations[172].items[7].load_case=24
load_combinations[172].items[7].factor=1.0
load_combinations[172].items[8].load_case=33
load_combinations[172].items[8].factor=0.2
load_combinations[172].items[9].load_case=41
load_combinations[172].items[9].factor=1.0
load_combinations[172].items[10].load_case=63
load_combinations[172].items[10].factor=1.0
load_combinations[172].items[11].load_case=64
load_combinations[172].items[11].factor=-0.3
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
load_combinations[173].items[6].load_case=21
load_combinations[173].items[6].factor=0.7
load_combinations[173].items[7].load_case=24
load_combinations[173].items[7].factor=1.0
load_combinations[173].items[8].load_case=33
load_combinations[173].items[8].factor=0.2
load_combinations[173].items[9].load_case=41
load_combinations[173].items[9].factor=1.0
load_combinations[173].items[10].load_case=63
load_combinations[173].items[10].factor=-1.0
load_combinations[173].items[11].load_case=64
load_combinations[173].items[11].factor=0.3
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
load_combinations[174].items[6].load_case=21
load_combinations[174].items[6].factor=0.7
load_combinations[174].items[7].load_case=24
load_combinations[174].items[7].factor=1.0
load_combinations[174].items[8].load_case=33
load_combinations[174].items[8].factor=0.2
load_combinations[174].items[9].load_case=41
load_combinations[174].items[9].factor=1.0
load_combinations[174].items[10].load_case=63
load_combinations[174].items[10].factor=-1.0
load_combinations[174].items[11].load_case=64
load_combinations[174].items[11].factor=-0.3
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
load_combinations[175].items[6].load_case=21
load_combinations[175].items[6].factor=0.7
load_combinations[175].items[7].load_case=24
load_combinations[175].items[7].factor=1.0
load_combinations[175].items[8].load_case=33
load_combinations[175].items[8].factor=0.2
load_combinations[175].items[9].load_case=41
load_combinations[175].items[9].factor=1.0
load_combinations[175].items[10].load_case=63
load_combinations[175].items[10].factor=0.3
load_combinations[175].items[11].load_case=64
load_combinations[175].items[11].factor=1.0
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
load_combinations[176].items[6].load_case=21
load_combinations[176].items[6].factor=0.7
load_combinations[176].items[7].load_case=24
load_combinations[176].items[7].factor=1.0
load_combinations[176].items[8].load_case=33
load_combinations[176].items[8].factor=0.2
load_combinations[176].items[9].load_case=41
load_combinations[176].items[9].factor=1.0
load_combinations[176].items[10].load_case=63
load_combinations[176].items[10].factor=-0.3
load_combinations[176].items[11].load_case=64
load_combinations[176].items[11].factor=1.0
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
load_combinations[177].items[6].load_case=21
load_combinations[177].items[6].factor=0.7
load_combinations[177].items[7].load_case=24
load_combinations[177].items[7].factor=1.0
load_combinations[177].items[8].load_case=33
load_combinations[177].items[8].factor=0.2
load_combinations[177].items[9].load_case=41
load_combinations[177].items[9].factor=1.0
load_combinations[177].items[10].load_case=63
load_combinations[177].items[10].factor=0.3
load_combinations[177].items[11].load_case=64
load_combinations[177].items[11].factor=-1.0
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
load_combinations[178].items[6].load_case=21
load_combinations[178].items[6].factor=0.7
load_combinations[178].items[7].load_case=24
load_combinations[178].items[7].factor=1.0
load_combinations[178].items[8].load_case=33
load_combinations[178].items[8].factor=0.2
load_combinations[178].items[9].load_case=41
load_combinations[178].items[9].factor=1.0
load_combinations[178].items[10].load_case=63
load_combinations[178].items[10].factor=-0.3
load_combinations[178].items[11].load_case=64
load_combinations[178].items[11].factor=-1.0
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
load_combinations[201].items[6].load_case=21
load_combinations[201].items[6].factor=0.7
load_combinations[201].items[7].load_case=24
load_combinations[201].items[7].factor=1.0
load_combinations[201].items[8].load_case=33
load_combinations[201].items[8].factor=0.2
load_combinations[201].items[9].load_case=41
load_combinations[201].items[9].factor=1.0
load_combinations[201].items[10].load_case=71
load_combinations[201].items[10].factor=0.69
load_combinations[201].items[11].load_case=79
load_combinations[201].items[11].factor=0.69
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
load_combinations[202].items[6].load_case=21
load_combinations[202].items[6].factor=0.7
load_combinations[202].items[7].load_case=24
load_combinations[202].items[7].factor=1.0
load_combinations[202].items[8].load_case=33
load_combinations[202].items[8].factor=0.2
load_combinations[202].items[9].load_case=41
load_combinations[202].items[9].factor=1.0
load_combinations[202].items[10].load_case=72
load_combinations[202].items[10].factor=0.69
load_combinations[202].items[11].load_case=80
load_combinations[202].items[11].factor=0.69
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
load_combinations[203].items[6].load_case=21
load_combinations[203].items[6].factor=0.7
load_combinations[203].items[7].load_case=24
load_combinations[203].items[7].factor=1.0
load_combinations[203].items[8].load_case=33
load_combinations[203].items[8].factor=0.2
load_combinations[203].items[9].load_case=41
load_combinations[203].items[9].factor=1.0
load_combinations[203].items[10].load_case=75
load_combinations[203].items[10].factor=0.69
load_combinations[203].items[11].load_case=83
load_combinations[203].items[11].factor=0.69
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
load_combinations[204].items[6].load_case=21
load_combinations[204].items[6].factor=0.7
load_combinations[204].items[7].load_case=24
load_combinations[204].items[7].factor=1.0
load_combinations[204].items[8].load_case=33
load_combinations[204].items[8].factor=0.2
load_combinations[204].items[9].load_case=41
load_combinations[204].items[9].factor=1.0
load_combinations[204].items[10].load_case=76
load_combinations[204].items[10].factor=0.69
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
load_combinations[211].items[6].load_case=21
load_combinations[211].items[6].factor=0.7
load_combinations[211].items[7].load_case=23
load_combinations[211].items[7].factor=1.0
load_combinations[211].items[8].load_case=33
load_combinations[211].items[8].factor=0.2
load_combinations[211].items[9].load_case=71
load_combinations[211].items[9].factor=0.17
load_combinations[211].items[10].load_case=79
load_combinations[211].items[10].factor=0.17
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
load_combinations[213].items[6].load_case=21
load_combinations[213].items[6].factor=0.7
load_combinations[213].items[7].load_case=23
load_combinations[213].items[7].factor=1.0
load_combinations[213].items[8].load_case=33
load_combinations[213].items[8].factor=0.2
load_combinations[213].items[9].load_case=72
load_combinations[213].items[9].factor=0.17
load_combinations[213].items[10].load_case=80
load_combinations[213].items[10].factor=0.17
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
load_combinations[215].items[6].load_case=21
load_combinations[215].items[6].factor=0.7
load_combinations[215].items[7].load_case=23
load_combinations[215].items[7].factor=1.0
load_combinations[215].items[8].load_case=33
load_combinations[215].items[8].factor=0.2
load_combinations[215].items[9].load_case=75
load_combinations[215].items[9].factor=0.17
load_combinations[215].items[10].load_case=83
load_combinations[215].items[10].factor=0.17
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
load_combinations[217].items[6].load_case=21
load_combinations[217].items[6].factor=0.7
load_combinations[217].items[7].load_case=23
load_combinations[217].items[7].factor=1.0
load_combinations[217].items[8].load_case=33
load_combinations[217].items[8].factor=0.2
load_combinations[217].items[9].load_case=76
load_combinations[217].items[9].factor=0.17
load_combinations.create(991, design_situation="DS1", user_defined_name_enabled=True, name="EQ All G", static_analysis_settings="SA2")
load_combinations[991].items[1].load_case=1
load_combinations[991].items[1].factor=1.0
load_combinations[991].items[2].load_case=2
load_combinations[991].items[2].factor=1.0
load_combinations[991].items[3].load_case=3
load_combinations[991].items[3].factor=1.0
load_combinations.create(992, design_situation="DS1", user_defined_name_enabled=True, name="EQ All Q", static_analysis_settings="SA2")
load_combinations[992].items[1].load_case=11
load_combinations[992].items[1].factor=0.3
load_combinations[992].items[2].load_case=12
load_combinations[992].items[2].factor=0.6
load_combinations[992].items[3].load_case=21
load_combinations[992].items[3].factor=0.7
load_combinations[992].items[4].load_case=24
load_combinations[992].items[4].factor=1.0
load_combinations[992].items[5].load_case=33
load_combinations[992].items[5].factor=0.2
load_combinations[992].items[6].load_case=41
load_combinations[992].items[6].factor=1.0
load_combinations.create(993, design_situation="DS1", user_defined_name_enabled=True, name="EQ mass", static_analysis_settings="SA2")
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
load_combinations[993].items[6].load_case=21
load_combinations[993].items[6].factor=0.7
load_combinations[993].items[7].load_case=33
load_combinations[993].items[7].factor=0.2
load_combinations[993].items[8].load_case=41
load_combinations[993].items[8].factor=1.0

