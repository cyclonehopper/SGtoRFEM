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

sections.create_standardized_steel(75, "75*6 EA", "1")
sections.create_standardized_steel(89, "88.9*4 CHS", "1")
sections.create_standardized_steel(90, "90*8 EA", "1")
sections.create_standardized_steel(100, "100*6 EA", "1")
sections.create_standardized_steel(140, "139.7*5 CHS", "1")
sections.create_standardized_steel(150, "150 UC 30.0", "1")
sections.create_standardized_steel(168, "168.3x6.4 CHS")
sections.create_standardized_steel(201, "200 PFC", "1")
sections.create_standardized_steel(202, "200 UB 25.4", "1")
sections.create_standardized_steel(203, "200 UC 46.2")
sections.create_standardized_steel(219, "219.1x6.4 CHS")
sections.create_standardized_steel(250, "250 UC 72.9", "1")
sections.create_standardized_steel(251, "250 UB 31.4", "1")
sections.create_standardized_steel(252, "250 UC 89.5", "1")
sections.create_standardized_steel(253, "250 PFC")
sections.create_standardized_steel(301, "310 UB 40.4", "1")
sections.create_standardized_steel(302, "300 PFC")
sections.create_standardized_steel(350, "360 UB 44.7", "1")
sections.create_standardized_steel(401, "410 UB 53.7", "1")
sections.create_standardized_steel(451, "460 UB 67.1", "1")
sections.create_standardized_steel(530, "530 UB 82.0")
sections.create_standardized_steel(601, "610 UB 101", "1")
sections.create_standardized_steel(1101, "90*3CHS_dumy", "2")
sections.create_standardized_steel(1168, "168.3x4.8 CHS")
sections.create_standardized_steel(1200, "200x16 SHS", "2")
sections.create_standardized_steel(1201, "Section 1201", "2")
sections.create_standardized_steel(1401, "DN400_stack_dumm", "1")

# Create Nodes
nodes.create_standard( 1, 0.0, 0.0, 0.0)
nodes.create_standard( 2, 0.0, 0.0, 12.84)
nodes.create_standard( 3, 0.0, 6.4, 0.0)
nodes.create_standard( 4, 0.0, 6.4, 12.84)
nodes.create_standard( 5, 4.0, 0.0, 0.0)
nodes.create_standard( 6, 4.0, 0.0, 12.84)
nodes.create_standard( 7, 4.0, 6.4, 0.0)
nodes.create_standard( 8, 4.0, 6.4, 12.84)
nodes.create_standard( 9, 10.1, 0.0, 0.0)
nodes.create_standard( 10, 10.1, 3.2, 13.24)
nodes.create_standard( 11, 10.1, 6.4, 0.0)
nodes.create_standard( 12, 10.25, 3.2, 13.24)
nodes.create_standard( 13, 13.95, 0.0, 0.0)
nodes.create_standard( 14, 13.95, 0.0, 12.84)
nodes.create_standard( 15, 13.95, 6.4, 0.0)
nodes.create_standard( 16, 13.95, 6.4, 12.84)
nodes.create_standard( 17, 0.0, 0.0, 5.8)
nodes.create_standard( 18, 13.95, 6.4, 8.83)
nodes.create_standard( 19, 4.0, 0.0, 5.8)
nodes.create_standard( 20, 4.0, 6.4, 5.8)
nodes.create_standard( 21, 10.1, 0.0, 5.8)
nodes.create_standard( 22, 10.1, 6.4, 5.8)
nodes.create_standard( 23, 13.95, 0.0, 5.8)
nodes.create_standard( 24, 13.95, 6.4, 5.8)
nodes.create_standard( 25, 0.0, 4.3, 5.8)
nodes.create_standard( 26, 4.0, 4.3, 5.8)
nodes.create_standard( 27, 10.1, 4.3, 5.8)
nodes.create_standard( 28, 13.95, 4.3, 5.8)
nodes.create_standard( 29, 0.0, 2.1, 5.8)
nodes.create_standard( 30, 4.0, 2.1, 5.8)
nodes.create_standard( 31, 10.1, 2.1, 5.8)
nodes.create_standard( 32, 13.95, 2.1, 5.8)
nodes.create_standard( 33, 1.0, 4.3, 5.8)
nodes.create_standard( 34, 2.0, 4.3, 5.8)
nodes.create_standard( 35, 3.0, 4.3, 5.8)
nodes.create_standard( 36, 1.0, 6.4, 5.8)
nodes.create_standard( 37, 1.0, 2.1, 5.8)
nodes.create_standard( 38, 1.0, 0.0, 5.8)
nodes.create_standard( 39, 2.0, 6.4, 5.8)
nodes.create_standard( 40, 2.0, 2.1, 5.8)
nodes.create_standard( 41, 2.0, 0.0, 5.8)
nodes.create_standard( 42, 3.0, 6.4, 5.8)
nodes.create_standard( 43, 3.0, 2.1, 5.8)
nodes.create_standard( 44, 3.0, 0.0, 5.8)
nodes.create_standard( 45, 11.55, 4.3, 5.8)
nodes.create_standard( 46, 12.75, 4.3, 5.8)
nodes.create_standard( 47, 11.55, 2.1, 5.8)
nodes.create_standard( 48, 11.55, 0.0, 5.8)
nodes.create_standard( 49, 11.55, 6.4, 5.8)
nodes.create_standard( 50, 12.75, 2.1, 5.8)
nodes.create_standard( 51, 12.75, 0.0, 5.8)
nodes.create_standard( 52, 12.75, 6.4, 5.8)
nodes.create_standard( 53, 5.27, 4.3, 5.8)
nodes.create_standard( 54, 6.54, 4.3, 5.8)
nodes.create_standard( 55, 7.81, 4.3, 5.8)
nodes.create_standard( 56, 9.08, 4.3, 5.8)
nodes.create_standard( 57, 5.27, 2.1, 5.8)
nodes.create_standard( 58, 5.27, 6.4, 5.8)
nodes.create_standard( 59, 5.27, 0.0, 5.8)
nodes.create_standard( 60, 6.54, 2.1, 5.8)
nodes.create_standard( 61, 6.54, 6.4, 5.8)
nodes.create_standard( 62, 6.54, 0.0, 5.8)
nodes.create_standard( 63, 7.81, 2.1, 5.8)
nodes.create_standard( 64, 7.81, 6.4, 5.8)
nodes.create_standard( 65, 7.81, 0.0, 5.8)
nodes.create_standard( 66, 9.08, 2.1, 5.8)
nodes.create_standard( 67, 9.08, 6.4, 5.8)
nodes.create_standard( 68, 9.08, 0.0, 5.8)
nodes.create_standard( 69, 1.27, 0.0, 12.84)
nodes.create_standard( 70, 1.27, 6.4, 12.84)
nodes.create_standard( 71, 1.27, -1.68, 12.84)
nodes.create_standard( 72, 1.27, 8.08, 12.84)
nodes.create_standard( 73, 0.0, 3.2, 13.24)
nodes.create_standard( 74, 4.0, 3.2, 13.24)
nodes.create_standard( 75, 10.1, 1.97, 13.08625)
nodes.create_standard( 76, 13.95, 3.195, 12.486)
nodes.create_standard( 77, 10.1, 0.0, 12.486)
nodes.create_standard( 78, 13.95, 0.0, 12.486)
nodes.create_standard( 80, 13.95, 6.4, 12.486)
nodes.create_standard( 81, 10.1, 5.5, 12.486)
nodes.create_standard( 82, 13.95, 3.2, 13.24)
nodes.create_standard( 83, 12.038, 2.2, 8.83)
nodes.create_standard( 84, 12.038, 4.2, 8.83)
nodes.create_standard( 85, 13.09, 2.2, 8.83)
nodes.create_standard( 86, 13.09, 4.2, 8.83)
nodes.create_standard( 87, 13.95, 5.5, 12.486)
nodes.create_standard( 88, 11.154, 5.5, 12.486)
nodes.create_standard( 89, 11.154, 3.195, 12.486)
nodes.create_standard( 90, 10.25, 3.195, 12.486)
nodes.create_standard( 92, 12.675, 5.3, 8.83)
nodes.create_standard( 93, 12.7909090909091, 1.2, 8.83)
nodes.create_standard( 94, 12.038, 3.2, 8.83)
nodes.create_standard( 95, 11.4, 3.2, 8.83)
nodes.create_standard( 96, 13.09, 3.2, 8.83)
nodes.create_standard( 97, 11.154, 4.521, 12.486)
nodes.create_standard( 98, 11.154, 4.174, 12.486)
nodes.create_standard( 99, 12.133, 5.5, 12.486)
nodes.create_standard( 100, 12.133, 3.195, 12.486)
nodes.create_standard( 101, 12.971, 3.195, 12.486)
nodes.create_standard( 102, 13.95, 4.174, 12.486)
nodes.create_standard( 103, 12.971, 5.5, 12.486)
nodes.create_standard( 104, 13.95, 4.521, 12.486)
nodes.create_standard( 105, 12.552, 4.3475, 12.486)
nodes.create_standard( 106, 11.76625, 5.13325, 12.486)
nodes.create_standard( 107, 13.33775, 5.13325, 12.486)
nodes.create_standard( 108, 13.33775, 3.56175, 12.486)
nodes.create_standard( 109, 11.76625, 3.56175, 12.486)
nodes.create_standard( 110, 12.552, 4.3475, 14.486)
nodes.create_standard( 111, 12.552, 4.3475, 16.0)
nodes.create_standard( 112, 13.33775, 2.82825, 12.486)
nodes.create_standard( 113, 13.95, 2.216, 12.486)
nodes.create_standard( 114, 13.33775, 1.25675, 12.486)
nodes.create_standard( 115, 13.95, 1.869, 12.486)
nodes.create_standard( 116, 12.971, 0.890000000000001, 12.486)
nodes.create_standard( 117, 12.133, 0.890000000000001, 12.486)
nodes.create_standard( 118, 11.76625, 1.25675, 12.486)
nodes.create_standard( 119, 11.154, 1.869, 12.486)
nodes.create_standard( 120, 11.76625, 2.82825, 12.486)
nodes.create_standard( 121, 11.154, 2.216, 12.486)
nodes.create_standard( 122, 11.154, 0.890000000000001, 12.486)
nodes.create_standard( 123, 13.95, 0.890000000000001, 12.486)
nodes.create_standard( 124, 10.1, 0.890000000000001, 12.486)
nodes.create_standard( 125, 12.552, 2.0425, 12.486)
nodes.create_standard( 126, 12.552, 2.0425, 14.486)
nodes.create_standard( 128, 10.1, 1.97, 12.486)
nodes.create_standard( 129, 10.1, 4.42, 12.486)
nodes.create_standard( 131, 7.175, 0.0, 5.8)
nodes.create_standard( 132, 7.175, 6.4, 5.8)
nodes.create_standard( 133, 7.175, 0.0, 12.84)
nodes.create_standard( 134, 7.175, 6.4, 12.84)
nodes.create_standard( 135, 13.95, 3.2, 5.8)
nodes.create_standard( 137, 11.154, 4.3475, 12.486)
nodes.create_standard( 138, 6.54, 5.35, 5.8)
nodes.create_standard( 139, 12.552, 2.0425, 16.0)
nodes.create_standard( 140, 10.1, 3.195, 12.486)
nodes.create_standard( 141, 4.0, 4.3, 7.02)
nodes.create_standard( 142, 4.0, 2.1, 7.02)
nodes.create_standard( 143, 10.978, 2.1, 5.8)
nodes.create_standard( 144, 10.978, 4.3, 5.8)
nodes.create_standard( 145, 10.978, 2.1, 7.02)
nodes.create_standard( 146, 10.978, 4.3, 7.02)
nodes.create_standard( 147, 7.489, 2.1, 7.02)
nodes.create_standard( 148, 7.489, 4.3, 7.02)
nodes.create_standard( 149, 6.54, 3.2, 5.8)
nodes.create_standard( 150, 12.552, 5.5, 12.486)
nodes.create_standard( 151, 12.552, 6.4, 12.486)
nodes.create_standard( 152, 6.54, 1.05, 5.8)
nodes.create_standard( 153, 11.154, 6.4, 12.486)
nodes.create_standard( 155, 10.1, 5.95, 12.486)
nodes.create_standard( 156, 10.1, 0.45, 12.486)
nodes.create_standard( 157, 12.552, 0.0, 12.486)
nodes.create_standard( 158, 12.552, 0.890000000000001, 12.486)
nodes.create_standard( 159, 11.154, 0.0, 12.486)
nodes.create_standard( 160, 12.552, 2.0425, 13.3)
nodes.create_standard( 161, 0.0, 1.05, 5.8)
nodes.create_standard( 162, 9.08, 1.05, 5.8)
nodes.create_standard( 163, 13.95, 1.05, 5.8)
nodes.create_standard( 164, 4.0, 1.05, 5.8)
nodes.create_standard( 165, 2.0, 1.05, 5.8)
nodes.create_standard( 166, 10.1, 1.05, 5.8)
nodes.create_standard( 167, 11.55, 1.05, 5.8)
nodes.create_standard( 168, 12.552, 4.3475, 13.3)
nodes.create_standard( 169, 10.1, 5.0, 16.09)
nodes.create_standard( 170, 13.95, 5.0, 16.09)
nodes.create_standard( 171, 10.1, 3.7, 16.09)
nodes.create_standard( 172, 10.1, 3.2, 5.8)
nodes.create_standard( 173, 4.0, 3.2, 5.8)
nodes.create_standard( 174, 13.95, 3.7, 16.09)
nodes.create_standard( 175, 12.15, 5.0, 16.09)
nodes.create_standard( 176, 12.15, 3.7, 16.09)
nodes.create_standard( 177, 12.15, 6.4, 16.09)
nodes.create_standard( 178, 8.8, 6.4, 16.09)
nodes.create_standard( 179, 8.8, 3.7, 16.09)
nodes.create_standard( 181, 10.1, 1.4, 13.015)
nodes.create_standard( 182, 3.5527136788005e-15, 3.2, 5.8)
nodes.create_standard( 183, 13.95, 0.0, 8.83)
nodes.create_standard( 184, 10.1, 6.4, 12.486)
nodes.create_standard( 185, 10.1, 2.69, 16.09)
nodes.create_standard( 186, 0.0, 1.4, 13.015)
nodes.create_standard( 187, 0.0, 5.0, 13.015)
nodes.create_standard( 188, 4.0, 5.0, 13.015)
nodes.create_standard( 189, 10.1, 4.42, 13.0875)
nodes.create_standard( 190, 10.1, 5.5, 12.9525)
nodes.create_standard( 191, 4.0, 1.4, 13.015)
nodes.create_standard( 192, 10.1, 5.0, 13.015)
nodes.create_standard( 193, 10.1, 0.890000000000001, 12.95125)
nodes.create_standard( 194, 10.1, 6.4, 8.83)
nodes.create_standard( 195, 11.4, 6.4, 8.83)
nodes.create_standard( 196, 11.4, 0.0, 8.83)
nodes.create_standard( 197, 10.1, 0.0, 8.83)
nodes.create_standard( 198, 13.95, 2.2, 8.83)
nodes.create_standard( 199, 11.4, 2.2, 8.83)
nodes.create_standard( 200, 13.95, 4.2, 8.83)
nodes.create_standard( 201, 11.4, 4.2, 8.83)
nodes.create_standard( 202, 13.95, 1.2, 8.83)
nodes.create_standard( 203, 11.4, 1.2, 8.83)
nodes.create_standard( 204, 13.95, 3.2, 8.83)
nodes.create_standard( 205, 12.15, 2.69, 16.09)
nodes.create_standard( 206, 8.8, 2.69, 16.09)
nodes.create_standard( 207, 13.95, 2.69, 16.09)
nodes.create_standard( 208, 10.1, 1.39, 16.09)
nodes.create_standard( 209, 12.15, 1.39, 16.09)
nodes.create_standard( 210, 8.8, 1.39, 16.09)
nodes.create_standard( 211, 10.1, -1.3, 16.09)
nodes.create_standard( 212, 13.95, -1.3, 16.09)
nodes.create_standard( 213, 13.95, 1.39, 16.09)
nodes.create_standard( 214, 10.1, -0.7, 16.09)
nodes.create_standard( 215, 13.95, -0.7, 16.09)
nodes.create_standard( 216, 13.95, 6.4, 16.09)
nodes.create_standard( 217, 13.95, 3.195, 16.09)
nodes.create_standard( 218, 14.28, 1.97, 13.08625)
nodes.create_standard( 219, 13.95, 0.0, 14.99)
nodes.create_standard( 220, 10.1, 3.195, 16.09)
nodes.create_standard( 221, 10.1, 0.985, 16.09)
nodes.create_standard( 222, 10.1, 0.0, 16.09)
nodes.create_standard( 223, 10.1, 6.4, 16.09)
nodes.create_standard( 224, 14.28, 3.2, 13.24)
nodes.create_standard( 225, 12.15, 0.0, 16.09)
nodes.create_standard( 226, 14.28, 1.4, 13.015)
nodes.create_standard( 227, 14.28, 0.0, 12.84)
nodes.create_standard( 228, 12.81, 3.7, 16.09)
nodes.create_standard( 229, 13.95, 0.0, 16.09)
nodes.create_standard( 230, 12.81, 5.0, 16.09)
nodes.create_standard( 231, 12.81, 2.69, 16.09)
nodes.create_standard( 232, 13.95, 0.35, 16.09)
nodes.create_standard( 233, 14.21, 1.1, 16.09)
nodes.create_standard( 234, 10.1, -0.45, 21.79)
nodes.create_standard( 235, 17.67, 1.1, 13.51)
nodes.create_standard( 237, 12.81, 1.39, 16.09)
nodes.create_standard( 238, 12.81, 2.25, 16.09)
nodes.create_standard( 239, 10.1, 0.0, 21.79)
nodes.create_standard( 240, 12.81, 4.14, 16.09)
nodes.create_standard( 241, 10.1, 0.0, 16.3108760360375)
nodes.create_standard( 242, 10.627, 1.348, 5.8)
nodes.create_standard( 243, 10.175, -0.45, 16.3108760360375)
nodes.create_standard( 244, 10.175, -0.45, 21.79)
nodes.create_standard( 245, 13.95, 0.0, 2.9)
nodes.create_standard( 246, 10.627, 1.348, 12.486)
nodes.create_standard( 247, 12.81, 1.85, 16.09)
nodes.create_standard( 248, 12.81, 4.54, 16.09)
nodes.create_standard( 249, 12.15, 1.85, 16.09)
nodes.create_standard( 250, 12.15, 2.27, 16.09)
nodes.create_standard( 251, 13.95, 5.3, 8.83)
nodes.create_standard( 252, 10.1, 0.0, 14.99)
nodes.create_standard( 253, 12.15, 4.14, 16.09)
nodes.create_standard( 254, 11.4, 5.3, 8.83)
nodes.create_standard( 255, 12.15, 4.54, 16.09)
nodes.create_standard( 256, 7.95, 6.4, 16.09)
nodes.create_standard( 257, 7.95, 0.0, 16.09)
nodes.create_standard( 258, 10.1, 2.69, 15.89)
nodes.create_standard( 259, 7.95, 2.69, 15.89)
nodes.create_standard( 260, 8.8, 2.69, 15.89)
nodes.create_standard( 261, 8.55, 6.4, 16.09)
nodes.create_standard( 262, 8.55, 2.69, 15.89)
nodes.create_standard( 263, 10.1, 6.4, 14.99)
nodes.create_standard( 264, 8.55, 0.0, 16.09)
nodes.create_standard( 265, 8.9, 3.7, 16.09)
nodes.create_standard( 266, 8.9, 5.0, 16.09)
nodes.create_standard( 267, 8.9, 5.0, 18.39)
nodes.create_standard( 268, 8.9, 3.7, 18.39)
nodes.create_standard( 269, 8.9, 1.39, 16.09)
nodes.create_standard( 270, 0.0, 0.0, 12.026)
nodes.create_standard( 271, 10.33, 1.39, 16.09)
nodes.create_standard( 272, 8.9, 1.39, 18.39)
nodes.create_standard( 273, 14.21, 0.35, 16.09)
nodes.create_standard( 274, 8.9, 2.69, 18.39)
nodes.create_standard( 275, 8.9, 2.69, 16.09)
nodes.create_standard( 276, 10.33, 3.7, 16.09)
nodes.create_standard( 277, 10.33, 5.0, 16.09)
nodes.create_standard( 278, 10.0, 5.0, 16.09)
nodes.create_standard( 279, 10.0, 3.7, 16.09)
nodes.create_standard( 280, 8.8, 5.0, 16.09)
nodes.create_standard( 281, 10.0, 5.0, 16.89)
nodes.create_standard( 282, 10.0, 3.7, 16.89)
nodes.create_standard( 284, 10.0, 1.39, 16.89)
nodes.create_standard( 286, 8.8, 0.0, 16.09)
nodes.create_standard( 287, 10.0, 1.39, 16.09)
nodes.create_standard( 288, 10.0, 2.69, 16.09)
nodes.create_standard( 289, 10.0, 2.69, 16.89)
nodes.create_standard( 290, 17.67, 0.35, 13.51)
nodes.create_standard( 291, 10.627, 1.348, 13.486)
nodes.create_standard( 292, 10.1, -0.45, 16.3108760360375)
nodes.create_standard( 293, 10.1, 6.4, 2.9)
nodes.create_standard( 294, 4.0, 6.4, 2.9)
nodes.create_standard( 295, 7.175, 6.4, 2.9)
nodes.create_standard( 296, 10.1, 0.0, 2.9)
nodes.create_standard( 297, 7.175, 0.0, 2.9)
nodes.create_standard( 298, 4.0, 0.0, 2.9)
nodes.create_standard( 299, 13.95, 1.1, 16.09)
nodes.create_standard( 301, 17.9314112407937, 0.35, 13.51)
nodes.create_standard( 302, 17.9314112407937, 1.1, 13.51)
nodes.create_standard( 303, 10.33, 2.69, 16.09)
nodes.create_standard( 304, 11.4, 1.348, 8.83)
nodes.create_standard( 305, 4.0, 3.2, 2.9)
nodes.create_standard( 306, 9.85, 4.42, 13.0875)
nodes.create_standard( 307, 9.85, 5.0, 13.015)
nodes.create_standard( 308, 9.85, 3.2, 13.24)
nodes.create_standard( 309, 9.85, 6.4, 12.84)
nodes.create_standard( 310, 9.85, 1.97, 13.08625)
nodes.create_standard( 311, 9.85, 1.4, 13.015)
nodes.create_standard( 312, 9.85, 0.0, 12.84)
nodes.create_standard( 313, 10.1, 1.273, 12.486)
nodes.create_standard( 314, 4.0, 6.4, 12.026)
nodes.create_standard( 315, 10.1, 6.4, 12.336)
nodes.create_standard( 316, 9.85, 6.4, 12.336)
nodes.create_standard( 317, 10.1, 0.0, 12.336)
nodes.create_standard( 318, 9.85, 0.0, 12.336)
nodes.create_standard( 319, 4.0, 0.0, 12.026)
nodes.create_standard( 321, 10.1, 3.2, 2.9)
nodes.create_standard( 322, 0.0, 6.4, 12.026)
nodes.create_standard( 324, 10.627, 1.273, 12.486)
nodes.create_standard( 328, 14.28, 4.42, 13.0875)
nodes.create_standard( 329, 14.28, 5.0, 13.015)
nodes.create_standard( 330, 14.28, 6.4, 12.84)
nodes.create_standard( 336, 0.0, 6.4, 5.8)
nodes.create_standard( 337, 11.154, 1.273, 12.486)
nodes.create_standard( 338, 11.24, 2.04, 16.79)
nodes.create_standard( 342, 13.95, 6.4, 2.9)
nodes.create_standard( 343, 13.95, 3.2, 2.9)
nodes.create_standard( 344, -1.77635683940025e-15, 0.0, 2.9)
nodes.create_standard( 345, -1.77635683940025e-15, 6.4, 2.9)
nodes.create_standard( 346, 0.0, 3.2, 2.9)
nodes.create_standard( 347, 11.24, 4.35, 16.79)

 # Create Member Hinges
member_hinges.create(1, axial_release_n=inf, axial_release_vy=inf, axial_release_vz=inf, moment_release_mt=inf)
member_hinges.create(2, axial_release_n=inf, axial_release_vy=inf, axial_release_vz=inf, moment_release_mt=inf, moment_release_my=inf)
member_hinges.create(3, axial_release_n=inf, axial_release_vy=inf, axial_release_vz=inf, moment_release_my=inf, moment_release_mz=inf)
member_hinges.create(4, axial_release_n=inf, axial_release_vy=inf, axial_release_vz=inf)
member_hinges.create(5, axial_release_vy=inf, axial_release_vz=inf)# Create Lines

lines.create_polyline(1, "1,344")
lines.create_polyline(2, "3,345")
lines.create_polyline(3, "5,298")
lines.create_polyline(4, "7,294")
lines.create_polyline(5, "9,296")
lines.create_polyline(6, "11,293")
lines.create_polyline(7, "13,245")
lines.create_polyline(8, "15,342")
lines.create_polyline(9, "17,270")
lines.create_polyline(10, "336,322")
lines.create_polyline(11, "19,319")
lines.create_polyline(12, "20,314")
lines.create_polyline(13, "21,197")
lines.create_polyline(14, "22,194")
lines.create_polyline(15, "23,183")
lines.create_polyline(16, "24,18")
lines.create_polyline(17, "336,25")
lines.create_polyline(18, "17,38")
lines.create_polyline(19, "21,48")
lines.create_polyline(20, "19,59")
lines.create_polyline(21, "20,58")
lines.create_polyline(22, "336,36")
lines.create_polyline(23, "22,49")
lines.create_polyline(24, "20,26")
lines.create_polyline(25, "22,27")
lines.create_polyline(26, "24,28")
lines.create_polyline(27, "25,182")
lines.create_polyline(28, "26,173")
lines.create_polyline(29, "27,172")
lines.create_polyline(30, "28,135")
lines.create_polyline(31, "25,33")
lines.create_polyline(32, "27,144")
lines.create_polyline(33, "26,53")
lines.create_polyline(34, "29,161")
lines.create_polyline(35, "30,164")
lines.create_polyline(36, "31,166")
lines.create_polyline(37, "32,163")
lines.create_polyline(38, "29,37")
lines.create_polyline(39, "30,57")
lines.create_polyline(40, "31,143")
lines.create_polyline(41, "33,34")
lines.create_polyline(42, "34,35")
lines.create_polyline(43, "35,26")
lines.create_polyline(44, "36,33")
lines.create_polyline(45, "33,37")
lines.create_polyline(46, "37,38")
lines.create_polyline(47, "39,34")
lines.create_polyline(48, "34,40")
lines.create_polyline(49, "40,165")
lines.create_polyline(50, "42,35")
lines.create_polyline(51, "35,43")
lines.create_polyline(52, "43,44")
lines.create_polyline(53, "45,46")
lines.create_polyline(54, "46,28")
lines.create_polyline(55, "47,167")
lines.create_polyline(56, "45,47")
lines.create_polyline(57, "49,45")
lines.create_polyline(58, "50,51")
lines.create_polyline(59, "46,50")
lines.create_polyline(60, "52,46")
lines.create_polyline(61, "37,40")
lines.create_polyline(62, "40,43")
lines.create_polyline(63, "43,30")
lines.create_polyline(64, "47,50")
lines.create_polyline(65, "50,32")
lines.create_polyline(66, "53,54")
lines.create_polyline(67, "54,55")
lines.create_polyline(68, "55,56")
lines.create_polyline(69, "56,27")
lines.create_polyline(70, "53,57")
lines.create_polyline(71, "58,53")
lines.create_polyline(72, "57,59")
lines.create_polyline(73, "54,149")
lines.create_polyline(74, "61,138")
lines.create_polyline(75, "60,152")
lines.create_polyline(76, "55,63")
lines.create_polyline(77, "64,55")
lines.create_polyline(78, "63,65")
lines.create_polyline(79, "56,66")
lines.create_polyline(80, "67,56")
lines.create_polyline(81, "66,162")
lines.create_polyline(82, "38,41")
lines.create_polyline(83, "41,44")
lines.create_polyline(84, "44,19")
lines.create_polyline(85, "48,51")
lines.create_polyline(86, "51,23")
lines.create_polyline(87, "59,62")
lines.create_polyline(88, "62,131")
lines.create_polyline(89, "65,68")
lines.create_polyline(90, "68,21")
lines.create_polyline(91, "58,61")
lines.create_polyline(92, "61,132")
lines.create_polyline(93, "64,67")
lines.create_polyline(94, "67,22")
lines.create_polyline(95, "36,39")
lines.create_polyline(96, "39,42")
lines.create_polyline(97, "42,20")
lines.create_polyline(98, "49,52")
lines.create_polyline(99, "52,24")
lines.create_polyline(100, "57,60")
lines.create_polyline(101, "60,63")
lines.create_polyline(102, "63,66")
lines.create_polyline(103, "66,31")
lines.create_polyline(104, "2,69")
lines.create_polyline(105, "4,70")
lines.create_polyline(106, "69,6")
lines.create_polyline(107, "70,8")
lines.create_polyline(108, "70,69")
lines.create_polyline(109, "69,71")
lines.create_polyline(110, "72,70")
lines.create_polyline(111, "2,186")
lines.create_polyline(112, "73,187")
lines.create_polyline(113, "74,188")
lines.create_polyline(114, "6,191")
lines.create_polyline(115, "75,10")
lines.create_polyline(116, "181,75")
lines.create_polyline(117, "16,330")
lines.create_polyline(118, "193,181")
lines.create_polyline(119, "73,74")
lines.create_polyline(120, "74,308")
lines.create_polyline(121, "76,82")
lines.create_polyline(122, "8,134")
lines.create_polyline(123, "78,14")
lines.create_polyline(124, "6,133")
lines.create_polyline(125, "80,16")
lines.create_polyline(126, "88,81")
lines.create_polyline(127, "76,101")
lines.create_polyline(128, "80,87")
lines.create_polyline(129, "83,85")
lines.create_polyline(130, "224,82")
lines.create_polyline(131, "14,227")
lines.create_polyline(132, "241,239")
lines.create_polyline(133, "344,17")
lines.create_polyline(134, "345,336")
lines.create_polyline(135, "99,88")
lines.create_polyline(136, "89,90")
lines.create_polyline(137, "88,97")
lines.create_polyline(138, "115,123")
lines.create_polyline(139, "97,137")
lines.create_polyline(140, "104,102")
lines.create_polyline(141, "98,89")
lines.create_polyline(142, "99,106")
lines.create_polyline(143, "150,99")
lines.create_polyline(144, "26,58")
lines.create_polyline(145, "58,54")
lines.create_polyline(146, "84,201")
lines.create_polyline(147, "83,94")
lines.create_polyline(148, "85,198")
lines.create_polyline(149, "271,303")
lines.create_polyline(150, "85,96")
lines.create_polyline(151, "200,92")
lines.create_polyline(152, "92,195")
lines.create_polyline(153, "92,254")
lines.create_polyline(154, "198,93")
lines.create_polyline(155, "93,196")
lines.create_polyline(156, "93,203")
lines.create_polyline(157, "94,84")
lines.create_polyline(158, "95,201")
lines.create_polyline(159, "94,95")
lines.create_polyline(160, "96,86")
lines.create_polyline(161, "96,204")
lines.create_polyline(162, "100,109")
lines.create_polyline(163, "101,100")
lines.create_polyline(164, "100,89")
lines.create_polyline(165, "112,113")
lines.create_polyline(166, "101,108")
lines.create_polyline(167, "103,107")
lines.create_polyline(168, "87,103")
lines.create_polyline(169, "101,112")
lines.create_polyline(170, "114,115")
lines.create_polyline(171, "116,114")
lines.create_polyline(172, "117,118")
lines.create_polyline(173, "106,97")
lines.create_polyline(174, "118,119")
lines.create_polyline(175, "107,104")
lines.create_polyline(176, "120,121")
lines.create_polyline(177, "108,102")
lines.create_polyline(178, "100,120")
lines.create_polyline(179, "109,98")
lines.create_polyline(180, "122,337")
lines.create_polyline(181, "105,168")
lines.create_polyline(182, "110,111")
lines.create_polyline(183, "119,121")
lines.create_polyline(184, "121,89")
lines.create_polyline(185, "123,116")
lines.create_polyline(186, "158,117")
lines.create_polyline(187, "117,122")
lines.create_polyline(188, "122,124")
lines.create_polyline(189, "125,160")
lines.create_polyline(190, "126,139")
lines.create_polyline(191, "103,150")
lines.create_polyline(192, "151,80")
lines.create_polyline(193, "150,151")
lines.create_polyline(194, "153,151")
lines.create_polyline(195, "88,153")
lines.create_polyline(196, "87,151")
lines.create_polyline(197, "151,88")
lines.create_polyline(198, "81,155")
lines.create_polyline(199, "153,81")
lines.create_polyline(200, "318,156")
lines.create_polyline(201, "155,184")
lines.create_polyline(202, "156,124")
lines.create_polyline(203, "137,98")
lines.create_polyline(204, "81,137")
lines.create_polyline(205, "137,140")
lines.create_polyline(206, "123,157")
lines.create_polyline(207, "158,157")
lines.create_polyline(208, "157,122")
lines.create_polyline(209, "122,159")
lines.create_polyline(210, "159,124")
lines.create_polyline(211, "116,158")
lines.create_polyline(212, "160,126")
lines.create_polyline(213, "168,110")
lines.create_polyline(214, "169,277")
lines.create_polyline(215, "171,276")
lines.create_polyline(216, "175,230")
lines.create_polyline(217, "176,228")
lines.create_polyline(218, "176,253")
lines.create_polyline(219, "177,216")
lines.create_polyline(220, "184,263")
lines.create_polyline(221, "77,252")
lines.create_polyline(222, "81,190")
lines.create_polyline(223, "14,219")
lines.create_polyline(224, "245,23")
lines.create_polyline(225, "16,216")
lines.create_polyline(226, "8,73")
lines.create_polyline(227, "73,6")
lines.create_polyline(228, "131,65")
lines.create_polyline(229, "293,22")
lines.create_polyline(230, "296,297")
lines.create_polyline(231, "294,20")
lines.create_polyline(232, "297,298")
lines.create_polyline(233, "133,312")
lines.create_polyline(234, "183,78")
lines.create_polyline(235, "77,183")
lines.create_polyline(236, "18,22")
lines.create_polyline(237, "184,18")
lines.create_polyline(238, "132,64")
lines.create_polyline(239, "134,309")
lines.create_polyline(240, "77,156")
lines.create_polyline(241, "78,222")
lines.create_polyline(242, "128,140")
lines.create_polyline(243, "80,223")
lines.create_polyline(244, "135,32")
lines.create_polyline(245, "176,347")
lines.create_polyline(246, "175,347")
lines.create_polyline(247, "76,113")
lines.create_polyline(248, "23,204")
lines.create_polyline(249, "24,204")
lines.create_polyline(250, "175,177")
lines.create_polyline(251, "129,81")
lines.create_polyline(252, "169,177")
lines.create_polyline(253, "177,170")
lines.create_polyline(254, "222,214")
lines.create_polyline(255, "179,206")
lines.create_polyline(256, "171,279")
lines.create_polyline(257, "185,303")
lines.create_polyline(258, "185,288")
lines.create_polyline(259, "205,231")
lines.create_polyline(260, "208,271")
lines.create_polyline(261, "26,141")
lines.create_polyline(262, "30,142")
lines.create_polyline(263, "143,47")
lines.create_polyline(264, "144,45")
lines.create_polyline(265, "143,145")
lines.create_polyline(266, "144,146")
lines.create_polyline(267, "141,148")
lines.create_polyline(268, "142,147")
lines.create_polyline(269, "141,142")
lines.create_polyline(270, "146,145")
lines.create_polyline(271, "147,145")
lines.create_polyline(272, "148,146")
lines.create_polyline(273, "147,148")
lines.create_polyline(274, "141,147")
lines.create_polyline(275, "147,146")
lines.create_polyline(276, "208,287")
lines.create_polyline(277, "209,237")
lines.create_polyline(278, "209,225")
lines.create_polyline(279, "205,250")
lines.create_polyline(280, "218,224")
lines.create_polyline(281, "208,225")
lines.create_polyline(282, "208,286")
lines.create_polyline(283, "222,286")
lines.create_polyline(284, "169,179")
lines.create_polyline(285, "179,185")
lines.create_polyline(286, "185,210")
lines.create_polyline(287, "205,176")
lines.create_polyline(288, "206,210")
lines.create_polyline(289, "210,286")
lines.create_polyline(290, "226,218")
lines.create_polyline(291, "170,174")
lines.create_polyline(292, "174,217")
lines.create_polyline(293, "27,67")
lines.create_polyline(294, "164,19")
lines.create_polyline(295, "43,165")
lines.create_polyline(296, "138,54")
lines.create_polyline(297, "64,138")
lines.create_polyline(298, "138,55")
lines.create_polyline(299, "149,60")
lines.create_polyline(300, "55,149")
lines.create_polyline(301, "149,63")
lines.create_polyline(302, "152,62")
lines.create_polyline(303, "63,152")
lines.create_polyline(304, "152,65")
lines.create_polyline(305, "161,17")
lines.create_polyline(306, "38,161")
lines.create_polyline(307, "161,37")
lines.create_polyline(308, "162,68")
lines.create_polyline(309, "9,321")
lines.create_polyline(310, "166,21")
lines.create_polyline(311, "167,48")
lines.create_polyline(312, "163,23")
lines.create_polyline(313, "51,163")
lines.create_polyline(314, "163,50")
lines.create_polyline(315, "11,321")
lines.create_polyline(316, "67,55")
lines.create_polyline(317, "5,305")
lines.create_polyline(318, "43,164")
lines.create_polyline(319, "164,44")
lines.create_polyline(320, "165,41")
lines.create_polyline(321, "165,38")
lines.create_polyline(322, "7,305")
lines.create_polyline(323, "173,30")
lines.create_polyline(324, "47,166")
lines.create_polyline(325, "166,48")
lines.create_polyline(326, "50,167")
lines.create_polyline(327, "167,51")
lines.create_polyline(328, "207,213")
lines.create_polyline(329, "213,299")
lines.create_polyline(330, "229,215")
lines.create_polyline(331, "185,220")
lines.create_polyline(332, "214,211")
lines.create_polyline(333, "172,31")
lines.create_polyline(334, "227,226")
lines.create_polyline(335, "224,328")
lines.create_polyline(336, "225,213")
lines.create_polyline(337, "225,229")
lines.create_polyline(338, "124,313")
lines.create_polyline(339, "328,329")
lines.create_polyline(340, "329,330")
lines.create_polyline(341, "228,240")
lines.create_polyline(342, "231,238")
lines.create_polyline(343, "186,73")
lines.create_polyline(344, "238,247")
lines.create_polyline(345, "140,129")
lines.create_polyline(346, "240,248")
lines.create_polyline(347, "247,237")
lines.create_polyline(348, "10,189")
lines.create_polyline(349, "189,192")
lines.create_polyline(350, "187,4")
lines.create_polyline(351, "191,74")
lines.create_polyline(352, "188,8")
lines.create_polyline(353, "192,190")
lines.create_polyline(354, "124,193")
lines.create_polyline(355, "342,24")
lines.create_polyline(356, "82,12")
lines.create_polyline(357, "90,140")
lines.create_polyline(358, "102,76")
lines.create_polyline(359, "347,277")
lines.create_polyline(360, "347,276")
lines.create_polyline(361, "182,29")
lines.create_polyline(362, "183,21")
lines.create_polyline(363, "18,80")
lines.create_polyline(364, "77,159")
lines.create_polyline(365, "248,230")
lines.create_polyline(366, "249,209")
lines.create_polyline(367, "252,286")
lines.create_polyline(368, "18,195")
lines.create_polyline(369, "195,194")
lines.create_polyline(370, "183,196")
lines.create_polyline(371, "196,197")
lines.create_polyline(372, "196,203")
lines.create_polyline(373, "183,202")
lines.create_polyline(374, "198,204")
lines.create_polyline(375, "199,95")
lines.create_polyline(376, "199,83")
lines.create_polyline(377, "200,86")
lines.create_polyline(378, "200,251")
lines.create_polyline(379, "201,254")
lines.create_polyline(380, "202,93")
lines.create_polyline(381, "203,304")
lines.create_polyline(382, "202,198")
lines.create_polyline(383, "197,77")
lines.create_polyline(384, "204,200")
lines.create_polyline(385, "183,76")
lines.create_polyline(386, "18,76")
lines.create_polyline(387, "247,249")
lines.create_polyline(388, "250,249")
lines.create_polyline(389, "238,250")
lines.create_polyline(390, "253,255")
lines.create_polyline(391, "240,253")
lines.create_polyline(392, "255,175")
lines.create_polyline(393, "248,255")
lines.create_polyline(394, "178,261")
lines.create_polyline(395, "286,264")
lines.create_polyline(396, "258,260")
lines.create_polyline(397, "216,170")
lines.create_polyline(398, "215,212")
lines.create_polyline(399, "217,207")
lines.create_polyline(400, "252,211")
lines.create_polyline(401, "171,169")
lines.create_polyline(402, "220,171")
lines.create_polyline(403, "208,185")
lines.create_polyline(404, "221,208")
lines.create_polyline(405, "222,221")
lines.create_polyline(406, "169,223")
lines.create_polyline(407, "260,262")
lines.create_polyline(408, "206,260")
lines.create_polyline(409, "185,258")
lines.create_polyline(410, "261,256")
lines.create_polyline(411, "262,259")
lines.create_polyline(412, "264,257")
lines.create_polyline(413, "265,179")
lines.create_polyline(414, "219,229")
lines.create_polyline(415, "266,280")
lines.create_polyline(416, "266,267")
lines.create_polyline(417, "265,268")
lines.create_polyline(418, "267,268")
lines.create_polyline(419, "269,272")
lines.create_polyline(420, "274,272")
lines.create_polyline(421, "223,177")
lines.create_polyline(422, "275,274")
lines.create_polyline(423, "222,225")
lines.create_polyline(424, "275,206")
lines.create_polyline(425, "78,217")
lines.create_polyline(426, "80,217")
lines.create_polyline(427, "77,220")
lines.create_polyline(428, "220,184")
lines.create_polyline(429, "211,212")
lines.create_polyline(430, "269,210")
lines.create_polyline(431, "276,176")
lines.create_polyline(432, "277,175")
lines.create_polyline(433, "276,277")
lines.create_polyline(434, "278,266")
lines.create_polyline(435, "279,265")
lines.create_polyline(436, "278,281")
lines.create_polyline(437, "279,282")
lines.create_polyline(438, "282,281")
lines.create_polyline(439, "232,273")
lines.create_polyline(440, "284,289")
lines.create_polyline(441, "299,232")
lines.create_polyline(442, "287,284")
lines.create_polyline(443, "273,233")
lines.create_polyline(444, "113,115")
lines.create_polyline(445, "288,289")
lines.create_polyline(446, "288,275")
lines.create_polyline(447, "287,269")
lines.create_polyline(448, "219,212")
lines.create_polyline(449, "286,211")
lines.create_polyline(450, "273,290")
lines.create_polyline(451, "235,290")
lines.create_polyline(452, "222,241")
lines.create_polyline(453, "239,234")
lines.create_polyline(454, "241,292")
lines.create_polyline(455, "245,135")
lines.create_polyline(456, "303,205")
lines.create_polyline(457, "243,244")
lines.create_polyline(458, "233,235")
lines.create_polyline(459, "299,233")
lines.create_polyline(460, "290,301")
lines.create_polyline(461, "235,302")
lines.create_polyline(462, "184,153")
lines.create_polyline(463, "337,119")
lines.create_polyline(464, "251,18")
lines.create_polyline(465, "254,195")
lines.create_polyline(466, "252,222")
lines.create_polyline(467, "313,128")
lines.create_polyline(468, "271,209")
lines.create_polyline(469, "246,291")
lines.create_polyline(470, "291,243")
lines.create_polyline(471, "242,246")
lines.create_polyline(472, "304,199")
lines.create_polyline(473, "313,324")
lines.create_polyline(474, "324,337")
lines.create_polyline(475, "209,338")
lines.create_polyline(476, "205,338")
lines.create_polyline(477, "338,303")
lines.create_polyline(478, "338,271")
lines.create_polyline(479, "230,170")
lines.create_polyline(480, "228,174")
lines.create_polyline(481, "231,207")
lines.create_polyline(482, "237,213")
lines.create_polyline(483, "342,135")
lines.create_polyline(484, "232,229")
lines.create_polyline(485, "343,245")
lines.create_polyline(486, "342,343")
lines.create_polyline(487, "169,278")
lines.create_polyline(488, "251,92")
lines.create_polyline(489, "86,84")
lines.create_polyline(490, "13,343")
lines.create_polyline(491, "15,343")
lines.create_polyline(492, "223,178")
lines.create_polyline(493, "263,223")
lines.create_polyline(494, "263,178")
lines.create_polyline(495, "344,182")
lines.create_polyline(496, "345,182")
lines.create_polyline(497, "346,344")
lines.create_polyline(498, "345,346")
lines.create_polyline(499, "1,346")
lines.create_polyline(500, "3,346")
lines.create_polyline(501, "87,104")
lines.create_polyline(502, "12,10")
lines.create_polyline(503, "90,12")
lines.create_polyline(504, "280,179")
lines.create_polyline(505, "318,312")
lines.create_polyline(506, "159,157")
lines.create_polyline(507, "157,78")
lines.create_polyline(510, "77,317")
lines.create_polyline(511, "178,280")
lines.create_polyline(512, "169,178")
lines.create_polyline(532, "293,295")
lines.create_polyline(534, "293,132")
lines.create_polyline(536, "294,132")
lines.create_polyline(537, "295,294")
lines.create_polyline(538, "11,295")
lines.create_polyline(539, "7,295")
lines.create_polyline(540, "9,297")
lines.create_polyline(541, "5,297")
lines.create_polyline(542, "296,131")
lines.create_polyline(543, "298,131")
lines.create_polyline(544, "298,19")
lines.create_polyline(545, "296,21")
lines.create_polyline(549, "123,78")
lines.create_polyline(561, "294,305")
lines.create_polyline(562, "293,321")
lines.create_polyline(563, "294,173")
lines.create_polyline(564, "298,173")
lines.create_polyline(565, "305,298")
lines.create_polyline(566, "306,307")
lines.create_polyline(567, "308,306")
lines.create_polyline(568, "307,309")
lines.create_polyline(569, "310,308")
lines.create_polyline(570, "311,310")
lines.create_polyline(571, "312,311")
lines.create_polyline(572, "194,315")
lines.create_polyline(573, "317,77")
lines.create_polyline(574, "74,133")
lines.create_polyline(575, "133,308")
lines.create_polyline(576, "315,316")
lines.create_polyline(577, "317,318")
lines.create_polyline(578, "315,184")
lines.create_polyline(579, "314,8")
lines.create_polyline(580, "319,6")
lines.create_polyline(582, "316,155")
lines.create_polyline(585, "270,2")
lines.create_polyline(586, "296,172")
lines.create_polyline(587, "293,172")
lines.create_polyline(588, "321,296")
lines.create_polyline(589, "322,4")
lines.create_polyline(592, "316,309")


# Create Members 
members.create_beam(1, "250", line="1", rotation_angle=1.5707963267948966)
members.create_beam(2, "250", line="2", rotation_angle=-1.5707963267948966)
members.create_beam(3, "250", line="3", rotation_angle=1.5707963267948966)
members.create_beam(4, "250", line="4", rotation_angle=-1.5707963267948966)
members.create_beam(5, "250", line="5", rotation_angle=1.5707963267948966)
members.create_beam(6, "250", line="6", rotation_angle=-1.5707963267948966)
members.create_beam(7, "250", line="7", rotation_angle=3.141592653589793)
members.create_beam(8, "250", line="8", rotation_angle=3.141592653589793)
members.create_beam(9, "250", line="9", rotation_angle=1.5707963267948966)
members.create_beam(10, "250", line="10", rotation_angle=-1.5707963267948966)
members.create_beam(11, "250", line="11", rotation_angle=1.5707963267948966)
members.create_beam(12, "250", line="12", rotation_angle=-1.5707963267948966)
members.create_beam(13, "250", line="13", rotation_angle=1.5707963267948966)
members.create_beam(14, "250", line="14", rotation_angle=-1.5707963267948966)
members.create_beam(15, "250", line="15", rotation_angle=3.141592653589793)
members.create_beam(16, "250", line="16", rotation_angle=3.141592653589793)
members.create_beam(17, "301", line="17", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(18, "301", line="18", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(19, "301", line="19", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(20, "301", line="20", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(21, "301", line="21", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(22, "301", line="22", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(23, "301", line="23", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(24, "601", line="24", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(25, "601", line="25", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(26, "301", line="26", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(27, "301", line="27", rotation_angle=0.0)
members.create_beam(28, "601", line="28", rotation_angle=0.0)
members.create_beam(29, "601", line="29", rotation_angle=0.0)
members.create_beam(30, "301", line="30", rotation_angle=0.0)
members.create_beam(31, "251", line="31", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(32, "301", line="32", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(33, "301", line="33", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(34, "301", line="34", rotation_angle=0.0)
members.create_beam(35, "601", line="35", rotation_angle=0.0)
members.create_beam(36, "601", line="36", rotation_angle=0.0)
members.create_beam(37, "301", line="37", rotation_angle=0.0)
members.create_beam(38, "251", line="38", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(39, "301", line="39", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(40, "301", line="40", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(41, "251", line="41", rotation_angle=0.0)
members.create_beam(42, "251", line="42", rotation_angle=0.0)
members.create_beam(43, "251", line="43", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(44, "201", line="44", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(45, "201", line="45", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(46, "201", line="46", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(47, "201", line="47", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(48, "201", line="48", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(49, "201", line="49", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(50, "201", line="50", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(51, "201", line="51", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(52, "201", line="52", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(53, "301", line="53", rotation_angle=0.0)
members.create_beam(54, "301", line="54", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(55, "201", line="55", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(56, "201", line="56", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(57, "201", line="57", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(58, "201", line="58", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(59, "201", line="59", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(60, "201", line="60", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(61, "251", line="61", rotation_angle=0.0)
members.create_beam(62, "251", line="62", rotation_angle=0.0)
members.create_beam(63, "251", line="63", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(64, "301", line="64", rotation_angle=0.0)
members.create_beam(65, "301", line="65", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(66, "301", line="66", rotation_angle=0.0)
members.create_beam(67, "301", line="67", rotation_angle=0.0)
members.create_beam(68, "301", line="68", rotation_angle=0.0)
members.create_beam(69, "301", line="69", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(70, "201", line="70", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(71, "201", line="71", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(72, "201", line="72", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(73, "201", line="73", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(74, "201", line="74", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(75, "201", line="75", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(76, "201", line="76", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(77, "201", line="77", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(78, "201", line="78", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(79, "201", line="79", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(80, "201", line="80", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(81, "201", line="81", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(82, "301", line="82", rotation_angle=0.0)
members.create_beam(83, "301", line="83", rotation_angle=0.0)
members.create_beam(84, "301", line="84", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(85, "301", line="85", rotation_angle=0.0)
members.create_beam(86, "301", line="86", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(87, "301", line="87", rotation_angle=0.0)
members.create_beam(88, "301", line="88", rotation_angle=0.0)
members.create_beam(89, "301", line="89", rotation_angle=0.0)
members.create_beam(90, "301", line="90", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(91, "301", line="91", rotation_angle=0.0)
members.create_beam(92, "301", line="92", rotation_angle=0.0)
members.create_beam(93, "301", line="93", rotation_angle=0.0)
members.create_beam(94, "301", line="94", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(95, "301", line="95", rotation_angle=0.0)
members.create_beam(96, "301", line="96", rotation_angle=0.0)
members.create_beam(97, "301", line="97", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(98, "301", line="98", rotation_angle=0.0)
members.create_beam(99, "301", line="99", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(100, "301", line="100", rotation_angle=0.0)
members.create_beam(101, "301", line="101", rotation_angle=0.0)
members.create_beam(102, "301", line="102", rotation_angle=0.0)
members.create_beam(103, "301", line="103", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(104, "401", line="104", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(105, "401", line="105", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(106, "401", line="106", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(107, "401", line="107", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(108, "252", line="108", rotation_angle=0.0)
members.create_beam(109, "252", line="109", rotation_angle=0.0)
members.create_beam(110, "252", line="110", rotation_angle=0.0)
members.create_beam(111, "251", line="111", rotation_angle=0.0)
members.create_beam(112, "251", line="112", rotation_angle=0.0)
members.create_beam(113, "251", line="113", rotation_angle=0.0)
members.create_beam(114, "251", line="114", rotation_angle=0.0)
members.create_beam(115, "201", line="115", rotation_angle=0.0)
members.create_beam(116, "201", line="116", rotation_angle=0.0)
members.create_beam(117, "201", line="117", rotation_angle=0.0)
members.create_beam(118, "201", line="118", rotation_angle=0.0)
members.create_beam(119, "202", line="119", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(120, "202", line="120", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(121, "201", line="121", member_hinge_start="2", rotation_angle=1.5707963267948966)
members.create_beam(122, "251", line="122", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(123, "250", line="123", rotation_angle=3.141592653589793)
members.create_beam(124, "251", line="124", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(125, "250", line="125", rotation_angle=3.141592653589793)
members.create_beam(126, "350", line="126", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(127, "350", line="127", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(128, "350", line="128", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(129, "251", line="129", rotation_angle=0.0)
members.create_beam(130, "201", line="130", member_hinge_start="3", rotation_angle=0.0)
members.create_beam(131, "201", line="131", rotation_angle=0.0)
members.create_beam(132, "250", line="132", rotation_angle=1.5707963267948966)
members.create_beam(133, "250", line="133", rotation_angle=1.5707963267948966)
members.create_beam(134, "250", line="134", rotation_angle=-1.5707963267948966)
members.create_beam(135, "350", line="135", rotation_angle=0.0)
members.create_beam(136, "350", line="136", rotation_angle=0.0)
members.create_beam(137, "301", line="137", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(138, "350", line="138", rotation_angle=0.0)
members.create_beam(139, "301", line="139", rotation_angle=0.0)
members.create_beam(140, "350", line="140", rotation_angle=0.0)
members.create_beam(141, "301", line="141", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(142, "301", line="142", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(143, "350", line="143", rotation_angle=0.0)
members.create_beam(144, "90", line="144", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(145, "90", line="145", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(146, "251", line="146", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(147, "201", line="147", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(148, "251", line="148", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(149, "201", line="149", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(150, "201", line="150", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(151, "90", line="151", member_hinge_start="1", member_hinge_end="1", rotation_angle=3.141592653589793)
members.create_beam(152, "90", line="152", member_hinge_start="1", member_hinge_end="1", rotation_angle=3.141592653589793)
members.create_beam(153, "202", line="153", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(154, "90", line="154", member_hinge_start="1", member_hinge_end="1", rotation_angle=3.141592653589793)
members.create_beam(155, "90", line="155", member_hinge_start="1", member_hinge_end="1", rotation_angle=3.141592653589793)
members.create_beam(156, "202", line="156", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(157, "201", line="157", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(158, "301", line="158", rotation_angle=0.0)
members.create_beam(159, "201", line="159", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(160, "201", line="160", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(161, "201", line="161", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(162, "301", line="162", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(163, "350", line="163", rotation_angle=0.0)
members.create_beam(164, "350", line="164", rotation_angle=0.0)
members.create_beam(165, "301", line="165", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(166, "301", line="166", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(167, "301", line="167", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(168, "350", line="168", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(169, "301", line="169", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(170, "301", line="170", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(171, "301", line="171", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(172, "301", line="172", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(173, "301", line="173", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(174, "301", line="174", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(175, "301", line="175", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(176, "301", line="176", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(177, "301", line="177", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(178, "301", line="178", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(179, "301", line="179", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(180, "301", line="180", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(181, "1201", line="181", rotation_angle=0.0)
members.create_beam(182, "1201", line="182", rotation_angle=0.0)
members.create_beam(183, "301", line="183", rotation_angle=0.0)
members.create_beam(184, "301", line="184", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(185, "350", line="185", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(186, "350", line="186", rotation_angle=0.0)
members.create_beam(187, "350", line="187", rotation_angle=0.0)
members.create_beam(188, "350", line="188", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(189, "1201", line="189", rotation_angle=0.0)
members.create_beam(190, "1201", line="190", rotation_angle=0.0)
members.create_beam(191, "350", line="191", rotation_angle=0.0)
members.create_beam(192, "251", line="192", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(193, "201", line="193", rotation_angle=0.0)
members.create_beam(194, "251", line="194", rotation_angle=0.0)
members.create_beam(195, "201", line="195", rotation_angle=0.0)
members.create_beam(196, "90", line="196", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(197, "90", line="197", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(198, "350", line="198", rotation_angle=0.0)
members.create_beam(199, "90", line="199", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(200, "75", line="200", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(201, "350", line="201", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(202, "350", line="202", rotation_angle=0.0)
members.create_beam(203, "301", line="203", rotation_angle=0.0)
members.create_beam(204, "90", line="204", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(205, "90", line="205", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(206, "90", line="206", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(207, "201", line="207", rotation_angle=0.0)
members.create_beam(208, "90", line="208", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(209, "201", line="209", rotation_angle=0.0)
members.create_beam(210, "90", line="210", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(211, "350", line="211", rotation_angle=0.0)
members.create_beam(212, "1201", line="212", rotation_angle=0.0)
members.create_beam(213, "1201", line="213", rotation_angle=0.0)
members.create_beam(214, "451", line="214", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(215, "451", line="215", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(216, "451", line="216", rotation_angle=0.0)
members.create_beam(217, "451", line="217", rotation_angle=0.0)
members.create_beam(218, "201", line="218", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(219, "251", line="219", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(220, "250", line="220", rotation_angle=-1.5707963267948966)
members.create_beam(221, "250", line="221", rotation_angle=1.5707963267948966)
members.create_beam(222, "201", line="222", member_hinge_start="2", rotation_angle=0.0)
members.create_beam(223, "250", line="223", rotation_angle=3.141592653589793)
members.create_beam(224, "250", line="224", rotation_angle=3.141592653589793)
members.create_beam(225, "250", line="225", rotation_angle=3.141592653589793)
members.create_beam(226, "89", line="226", member_hinge_start="1", member_hinge_end="4", rotation_angle=0.0)
members.create_beam(227, "89", line="227", member_hinge_start="1", member_hinge_end="4", rotation_angle=0.0)
members.create_beam(228, "301", line="228", rotation_angle=0.0)
members.create_beam(229, "250", line="229", rotation_angle=-1.5707963267948966)
members.create_beam(230, "251", line="230", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(231, "250", line="231", rotation_angle=-1.5707963267948966)
members.create_beam(232, "251", line="232", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(233, "251", line="233", rotation_angle=0.0)
members.create_beam(234, "250", line="234", rotation_angle=3.141592653589793)
members.create_beam(235, "140", line="235", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(236, "140", line="236", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(237, "140", line="237", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(238, "301", line="238", rotation_angle=0.0)
members.create_beam(239, "251", line="239", rotation_angle=0.0)
members.create_beam(240, "350", line="240", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(241, "140", line="241", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(242, "350", line="242", rotation_angle=0.0)
members.create_beam(243, "140", line="243", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(244, "301", line="244", rotation_angle=0.0)
members.create_beam(245, "1101", line="245", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(246, "1101", line="246", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(247, "350", line="247", rotation_angle=0.0)
members.create_beam(248, "140", line="248", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(249, "140", line="249", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(250, "201", line="250", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(251, "350", line="251", rotation_angle=0.0)
members.create_beam(252, "90", line="252", member_hinge_start="1", member_hinge_end="1", rotation_angle=3.141592653589793)
members.create_beam(253, "90", line="253", member_hinge_start="1", member_hinge_end="1", rotation_angle=3.141592653589793)
members.create_beam(254, "201", line="254", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(255, "201", line="255", rotation_angle=0.0)
members.create_beam(256, "201", line="256", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(257, "451", line="257", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(258, "201", line="258", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(259, "451", line="259", rotation_angle=0.0)
members.create_beam(260, "451", line="260", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(261, "1200", line="261", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(262, "1200", line="262", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(263, "301", line="263", rotation_angle=0.0)
members.create_beam(264, "301", line="264", rotation_angle=0.0)
members.create_beam(265, "1200", line="265", member_hinge_start="1", rotation_angle=3.141592653589793)
members.create_beam(266, "1200", line="266", member_hinge_start="1", rotation_angle=3.141592653589793)
members.create_beam(267, "1200", line="267", member_hinge_end="4", rotation_angle=0.0)
members.create_beam(268, "1200", line="268", member_hinge_end="4", rotation_angle=0.0)
members.create_beam(269, "1200", line="269", rotation_angle=0.0)
members.create_beam(270, "1200", line="270", rotation_angle=0.0)
members.create_beam(271, "1200", line="271", rotation_angle=0.0)
members.create_beam(272, "1200", line="272", rotation_angle=0.0)
members.create_beam(273, "1200", line="273", member_hinge_start="4", rotation_angle=0.0)
members.create_beam(274, "1200", line="274", member_hinge_start="4", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(275, "1200", line="275", member_hinge_start="4", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(276, "201", line="276", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(277, "451", line="277", rotation_angle=0.0)
members.create_beam(278, "201", line="278", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(279, "201", line="279", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(280, "201", line="280", rotation_angle=0.0)
members.create_beam(281, "90", line="281", member_hinge_start="1", rotation_angle=3.141592653589793)
members.create_beam(282, "90", line="282", member_hinge_start="1", rotation_angle=3.141592653589793)
members.create_beam(283, "251", line="283", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(284, "90", line="284", member_hinge_start="1", member_hinge_end="1", rotation_angle=3.141592653589793)
members.create_beam(285, "90", line="285", member_hinge_start="1", member_hinge_end="1", rotation_angle=3.141592653589793)
members.create_beam(286, "90", line="286", member_hinge_start="1", member_hinge_end="1", rotation_angle=3.141592653589793)
members.create_beam(287, "201", line="287", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(288, "201", line="288", rotation_angle=0.0)
members.create_beam(289, "201", line="289", rotation_angle=0.0)
members.create_beam(290, "201", line="290", rotation_angle=0.0)
members.create_beam(291, "451", line="291", rotation_angle=0.0)
members.create_beam(292, "451", line="292", rotation_angle=0.0)
members.create_beam(293, "90", line="293", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(294, "601", line="294", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(295, "90", line="295", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(296, "201", line="296", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(297, "90", line="297", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(298, "90", line="298", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(299, "201", line="299", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(300, "90", line="300", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(301, "90", line="301", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(302, "201", line="302", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(303, "90", line="303", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(304, "90", line="304", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(305, "301", line="305", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(306, "90", line="306", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(307, "90", line="307", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(308, "201", line="308", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(309, "140", line="309", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(310, "601", line="310", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(311, "201", line="311", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(312, "301", line="312", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(313, "90", line="313", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(314, "90", line="314", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(315, "140", line="315", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(316, "90", line="316", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(317, "140", line="317", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(318, "90", line="318", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(319, "90", line="319", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(320, "201", line="320", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(321, "90", line="321", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(322, "140", line="322", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(323, "601", line="323", rotation_angle=0.0)
members.create_beam(324, "90", line="324", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(325, "90", line="325", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(326, "90", line="326", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(327, "90", line="327", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(328, "451", line="328", rotation_angle=0.0)
members.create_beam(329, "451", line="329", rotation_angle=0.0)
members.create_beam(330, "201", line="330", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(331, "451", line="331", rotation_angle=0.0)
members.create_beam(332, "201", line="332", rotation_angle=0.0)
members.create_beam(333, "601", line="333", rotation_angle=0.0)
members.create_beam(334, "201", line="334", member_hinge_start="5", rotation_angle=0.0)
members.create_beam(335, "201", line="335", rotation_angle=0.0)
members.create_beam(336, "90", line="336", member_hinge_end="1", rotation_angle=3.141592653589793)
members.create_beam(337, "251", line="337", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(338, "350", line="338", rotation_angle=0.0)
members.create_beam(339, "201", line="339", rotation_angle=0.0)
members.create_beam(340, "201", line="340", member_hinge_end="5", rotation_angle=0.0)
members.create_beam(341, "201", line="341", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(342, "201", line="342", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(343, "251", line="343", rotation_angle=0.0)
members.create_beam(344, "201", line="344", rotation_angle=0.0)
members.create_beam(345, "350", line="345", rotation_angle=0.0)
members.create_beam(346, "201", line="346", rotation_angle=0.0)
members.create_beam(347, "201", line="347", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(348, "201", line="348", rotation_angle=0.0)
members.create_beam(349, "201", line="349", rotation_angle=0.0)
members.create_beam(350, "251", line="350", rotation_angle=0.0)
members.create_beam(351, "251", line="351", rotation_angle=0.0)
members.create_beam(352, "251", line="352", rotation_angle=0.0)
members.create_beam(353, "201", line="353", rotation_angle=0.0)
members.create_beam(354, "201", line="354", member_hinge_start="2", rotation_angle=0.0)
members.create_beam(355, "250", line="355", rotation_angle=3.141592653589793)
members.create_beam(356, "201", line="356", rotation_angle=0.0)
members.create_beam(357, "350", line="357", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(358, "350", line="358", rotation_angle=0.0)
members.create_beam(359, "1101", line="359", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(360, "1101", line="360", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(361, "301", line="361", rotation_angle=0.0)
members.create_beam(362, "140", line="362", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(363, "250", line="363", rotation_angle=3.141592653589793)
members.create_beam(364, "251", line="364", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(365, "201", line="365", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(366, "201", line="366", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(367, "75", line="367", member_hinge_start="1", member_hinge_end="1", rotation_angle=3.141592653589793)
members.create_beam(368, "251", line="368", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(369, "251", line="369", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(370, "251", line="370", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(371, "251", line="371", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(372, "301", line="372", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(373, "301", line="373", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(374, "301", line="374", rotation_angle=0.0)
members.create_beam(375, "301", line="375", rotation_angle=0.0)
members.create_beam(376, "251", line="376", rotation_angle=0.0)
members.create_beam(377, "251", line="377", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(378, "301", line="378", rotation_angle=0.0)
members.create_beam(379, "301", line="379", rotation_angle=0.0)
members.create_beam(380, "202", line="380", rotation_angle=0.0)
members.create_beam(381, "301", line="381", rotation_angle=0.0)
members.create_beam(382, "301", line="382", rotation_angle=0.0)
members.create_beam(383, "250", line="383", rotation_angle=1.5707963267948966)
members.create_beam(384, "301", line="384", rotation_angle=0.0)
members.create_beam(385, "140", line="385", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(386, "140", line="386", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(387, "201", line="387", rotation_angle=0.0)
members.create_beam(388, "201", line="388", rotation_angle=0.0)
members.create_beam(389, "201", line="389", rotation_angle=0.0)
members.create_beam(390, "201", line="390", rotation_angle=0.0)
members.create_beam(391, "201", line="391", rotation_angle=0.0)
members.create_beam(392, "201", line="392", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(393, "201", line="393", rotation_angle=0.0)
members.create_beam(394, "251", line="394", rotation_angle=0.0)
members.create_beam(395, "251", line="395", rotation_angle=0.0)
members.create_beam(396, "201", line="396", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(397, "451", line="397", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(398, "201", line="398", rotation_angle=0.0)
members.create_beam(399, "451", line="399", rotation_angle=0.0)
members.create_beam(400, "75", line="400", member_hinge_start="1", member_hinge_end="1", rotation_angle=3.141592653589793)
members.create_beam(401, "451", line="401", rotation_angle=0.0)
members.create_beam(402, "451", line="402", rotation_angle=0.0)
members.create_beam(403, "451", line="403", rotation_angle=0.0)
members.create_beam(404, "451", line="404", rotation_angle=0.0)
members.create_beam(405, "451", line="405", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(406, "451", line="406", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(407, "201", line="407", rotation_angle=0.0)
members.create_beam(408, "75", line="408", rotation_angle=0.0)
members.create_beam(409, "75", line="409", rotation_angle=0.0)
members.create_beam(410, "251", line="410", rotation_angle=0.0)
members.create_beam(411, "201", line="411", rotation_angle=0.0)
members.create_beam(412, "251", line="412", rotation_angle=0.0)
members.create_beam(413, "451", line="413", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(414, "250", line="414", rotation_angle=3.141592653589793)
members.create_beam(415, "451", line="415", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(416, "100", line="416", rotation_angle=3.141592653589793)
members.create_beam(417, "100", line="417", rotation_angle=1.5707963267948966)
members.create_beam(418, "100", line="418", rotation_angle=3.141592653589793)
members.create_beam(419, "100", line="419", rotation_angle=1.5707963267948966)
members.create_beam(420, "100", line="420", rotation_angle=3.141592653589793)
members.create_beam(421, "251", line="421", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(422, "100", line="422", rotation_angle=3.141592653589793)
members.create_beam(423, "251", line="423", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(424, "451", line="424", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(425, "140", line="425", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(426, "140", line="426", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(427, "140", line="427", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(428, "140", line="428", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(429, "201", line="429", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(430, "451", line="430", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(431, "451", line="431", rotation_angle=0.0)
members.create_beam(432, "451", line="432", rotation_angle=0.0)
members.create_beam(433, "201", line="433", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(434, "201", line="434", rotation_angle=0.0)
members.create_beam(435, "201", line="435", rotation_angle=0.0)
members.create_beam(436, "201", line="436", rotation_angle=3.141592653589793)
members.create_beam(437, "201", line="437", rotation_angle=3.141592653589793)
members.create_beam(438, "201", line="438", rotation_angle=1.5707963267948966)
members.create_beam(439, "201", line="439", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(440, "201", line="440", rotation_angle=1.5707963267948966)
members.create_beam(441, "451", line="441", rotation_angle=0.0)
members.create_beam(442, "201", line="442", rotation_angle=3.141592653589793)
members.create_beam(443, "201", line="443", rotation_angle=0.0)
members.create_beam(444, "350", line="444", rotation_angle=0.0)
members.create_beam(445, "201", line="445", rotation_angle=3.141592653589793)
members.create_beam(446, "201", line="446", rotation_angle=0.0)
members.create_beam(447, "201", line="447", rotation_angle=0.0)
members.create_beam(448, "75", line="448", member_hinge_start="1", member_hinge_end="1", rotation_angle=3.141592653589793)
members.create_beam(449, "90", line="449", member_hinge_start="1", member_hinge_end="1", rotation_angle=3.141592653589793)
members.create_beam(450, "201", line="450", rotation_angle=0.0)
members.create_beam(451, "201", line="451", rotation_angle=0.0)
members.create_beam(452, "250", line="452", rotation_angle=1.5707963267948966)
members.create_beam(453, "201", line="453", rotation_angle=0.0)
members.create_beam(454, "201", line="454", rotation_angle=0.0)
members.create_beam(455, "140", line="455", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(456, "451", line="456", rotation_angle=0.0)
members.create_beam(457, "1401", line="457", rotation_angle=1.5707963267948966)
members.create_beam(458, "201", line="458", rotation_angle=0.0)
members.create_beam(459, "201", line="459", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(460, "201", line="460", rotation_angle=0.0)
members.create_beam(461, "201", line="461", rotation_angle=0.0)
members.create_beam(462, "251", line="462", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(463, "301", line="463", rotation_angle=0.0)
members.create_beam(464, "301", line="464", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(465, "301", line="465", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(466, "250", line="466", rotation_angle=1.5707963267948966)
members.create_beam(467, "350", line="467", rotation_angle=0.0)
members.create_beam(468, "451", line="468", rotation_angle=0.0)
members.create_beam(469, "1401", line="469", rotation_angle=0.0)
members.create_beam(470, "1401", line="470", rotation_angle=0.0)
members.create_beam(471, "1401", line="471", rotation_angle=0.0)
members.create_beam(472, "301", line="472", rotation_angle=0.0)
members.create_beam(473, "201", line="473", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(474, "201", line="474", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(475, "1101", line="475", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(476, "1101", line="476", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(477, "1101", line="477", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(478, "1101", line="478", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(479, "451", line="479", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(480, "451", line="480", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(481, "451", line="481", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(482, "451", line="482", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(483, "140", line="483", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(484, "451", line="484", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(485, "251", line="485", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(486, "251", line="486", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(487, "201", line="487", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(488, "202", line="488", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(489, "251", line="489", rotation_angle=0.0)
members.create_beam(490, "140", line="490", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(491, "140", line="491", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(492, "251", line="492", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(493, "250", line="493", rotation_angle=-1.5707963267948966)
members.create_beam(494, "75", line="494", member_hinge_start="1", member_hinge_end="1", rotation_angle=3.141592653589793)
members.create_beam(495, "140", line="495", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(496, "140", line="496", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(497, "251", line="497", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(498, "251", line="498", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(499, "140", line="499", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(500, "140", line="500", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(501, "350", line="501", rotation_angle=0.0)
members.create_beam(502, "201", line="502", member_hinge_end="3", rotation_angle=0.0)
members.create_beam(503, "201", line="503", member_hinge_start="2", rotation_angle=1.5707963267948966)
members.create_beam(504, "201", line="504", rotation_angle=0.0)
members.create_beam(505, "150", line="505", member_hinge_start="1", rotation_angle=3.141592653589793)
members.create_beam(506, "251", line="506", rotation_angle=0.0)
members.create_beam(507, "251", line="507", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(510, "250", line="510", rotation_angle=1.5707963267948966)
members.create_beam(511, "201", line="511", rotation_angle=0.0)
members.create_beam(512, "90", line="512", member_hinge_start="1", member_hinge_end="1", rotation_angle=3.141592653589793)
members.create_beam(532, "251", line="532", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(534, "140", line="534", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(536, "140", line="536", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(537, "251", line="537", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(538, "140", line="538", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(539, "140", line="539", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(540, "140", line="540", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(541, "140", line="541", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(542, "140", line="542", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(543, "140", line="543", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(544, "250", line="544", rotation_angle=1.5707963267948966)
members.create_beam(545, "250", line="545", rotation_angle=1.5707963267948966)
members.create_beam(549, "350", line="549", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(561, "251", line="561", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(562, "251", line="562", member_hinge_start="1", rotation_angle=0.0)
members.create_beam(563, "140", line="563", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(564, "140", line="564", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(565, "251", line="565", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(566, "251", line="566", rotation_angle=0.0)
members.create_beam(567, "251", line="567", rotation_angle=0.0)
members.create_beam(568, "251", line="568", rotation_angle=0.0)
members.create_beam(569, "251", line="569", rotation_angle=0.0)
members.create_beam(570, "251", line="570", rotation_angle=0.0)
members.create_beam(571, "251", line="571", rotation_angle=0.0)
members.create_beam(572, "250", line="572", rotation_angle=-1.5707963267948966)
members.create_beam(573, "250", line="573", rotation_angle=1.5707963267948966)
members.create_beam(574, "89", line="574", member_hinge_start="1", member_hinge_end="4", rotation_angle=0.0)
members.create_beam(575, "89", line="575", member_hinge_start="1", member_hinge_end="4", rotation_angle=0.0)
members.create_beam(576, "250", line="576", rotation_angle=0.0)
members.create_beam(577, "250", line="577", rotation_angle=0.0)
members.create_beam(578, "250", line="578", rotation_angle=-1.5707963267948966)
members.create_beam(579, "250", line="579", rotation_angle=-1.5707963267948966)
members.create_beam(580, "250", line="580", rotation_angle=1.5707963267948966)
members.create_beam(582, "75", line="582", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(585, "250", line="585", rotation_angle=1.5707963267948966)
members.create_beam(586, "140", line="586", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(587, "140", line="587", member_hinge_start="1", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(588, "251", line="588", member_hinge_end="1", rotation_angle=0.0)
members.create_beam(589, "250", line="589", rotation_angle=-1.5707963267948966)
members.create_beam(592, "150", line="592", member_hinge_start="1", rotation_angle=3.141592653589793)

# Create Nodal Supports
nodal_supports.create(1, nodes="1,3,5,7,9,11,13,15",  spring=[inf,inf,inf], rotational_restraint=[0,0,inf])
nodal_supports.create(2, nodes="301,302",  spring=[0,inf,inf], rotational_restraint=[inf,0,0])

# Create Static Analysis Settings
static_analysis_settings.create(1)
static_analysis_settings.create(2, analysis_type="Second-order (P-Δ)")

# Create Load Cases
load_cases.create(1, name="SW", static_analysis_settings="SA1", to_solve=False)
load_cases.create(2, name="GDstruct", static_analysis_settings="SA1", to_solve=False)
load_cases.create(3, name="GDmec", static_analysis_settings="SA1", to_solve=False)
load_cases.create(11, name="QL", static_analysis_settings="SA1", to_solve=False)
load_cases.create(12, name="QS", static_analysis_settings="SA1", to_solve=False)
load_cases.create(13, name="QML1", static_analysis_settings="SA1", to_solve=False)
load_cases.create(15, name="QMF", static_analysis_settings="SA1", to_solve=False)
load_cases.create(16, name="QCpt1", static_analysis_settings="SA1", to_solve=False)
load_cases.create(17, name="QBTo", static_analysis_settings="SA1", to_solve=False)
load_cases.create(18, name="QBTs", static_analysis_settings="SA1", to_solve=False)
load_cases.create(19, name="QBTn", static_analysis_settings="SA1", to_solve=False)
load_cases.create(20, name="QBTp", static_analysis_settings="SA1", to_solve=False)
load_cases.create(21, name="QMS", static_analysis_settings="SA1", to_solve=False)
load_cases.create(23, name="QV", static_analysis_settings="SA1", to_solve=False)
load_cases.create(24, name="Qbc", static_analysis_settings="SA1", to_solve=False)
load_cases.create(25, name="Qbo", static_analysis_settings="SA1", to_solve=False)
load_cases.create(26, name="QCpt2", static_analysis_settings="SA1", to_solve=False)
load_cases.create(31, name="Wuex", static_analysis_settings="SA1", to_solve=False)
load_cases.create(32, name="Wuix", static_analysis_settings="SA1", to_solve=False)
load_cases.create(33, name="Wdex", static_analysis_settings="SA1", to_solve=False)
load_cases.create(34, name="Wdix", static_analysis_settings="SA1", to_solve=False)
load_cases.create(35, name="Wuey", static_analysis_settings="SA1", to_solve=False)
load_cases.create(36, name="Wuiy", static_analysis_settings="SA1", to_solve=False)
load_cases.create(37, name="Wdey", static_analysis_settings="SA1", to_solve=False)
load_cases.create(38, name="Wdiy", static_analysis_settings="SA1", to_solve=False)
load_cases.create(39, name="-Wuex", static_analysis_settings="SA1", to_solve=False)
load_cases.create(40, name="-Wuix", static_analysis_settings="SA1", to_solve=False)
load_cases.create(41, name="-Wdex", static_analysis_settings="SA1", to_solve=False)
load_cases.create(42, name="-Wdix", static_analysis_settings="SA1", to_solve=False)
load_cases.create(43, name="-Wuey", static_analysis_settings="SA1", to_solve=False)
load_cases.create(44, name="-Wuiy", static_analysis_settings="SA1", to_solve=False)
load_cases.create(45, name="-Wdey", static_analysis_settings="SA1", to_solve=False)
load_cases.create(46, name="-Wdiy", static_analysis_settings="SA1", to_solve=False)
load_cases.create(51, name="Eqx", static_analysis_settings="SA1", to_solve=False)
load_cases.create(52, name="Eqy", static_analysis_settings="SA1", to_solve=False)

# Create Design Situations
design_situations.create(1, name="ULS - Strength", design_situation_type="DESIGN_SITUATION_TYPE_ULS_STRENGTH_AS_NZS")
design_situations.create(2, name="SLS - Serviceability", design_situation_type="DESIGN_SITUATION_TYPE_SLS_SERVICEABILITY_NZS")

# Create Load Combinations Titles
load_combinations.create(4, design_situation="DS1", user_defined_name_enabled=True, name="G", static_analysis_settings="SA2")
load_combinations[4].items[1].load_case=1
load_combinations[4].items[1].factor=1.0
load_combinations[4].items[2].load_case=2
load_combinations[4].items[2].factor=1.0
load_combinations[4].items[3].load_case=3
load_combinations[4].items[3].factor=1.0
load_combinations.create(53, design_situation="DS1", user_defined_name_enabled=True, name="Mseis  Seismic mass", static_analysis_settings="SA2")
load_combinations[53].items[1].load_case=1
load_combinations[53].items[1].factor=1.0
load_combinations[53].items[2].load_case=2
load_combinations[53].items[2].factor=1.0
load_combinations[53].items[3].load_case=3
load_combinations[53].items[3].factor=1.0
load_combinations[53].items[4].load_case=11
load_combinations[53].items[4].factor=0.4
load_combinations[53].items[5].load_case=12
load_combinations[53].items[5].factor=1.0
load_combinations[53].items[6].load_case=13
load_combinations[53].items[6].factor=1.0
load_combinations[53].items[7].load_case=25
load_combinations[53].items[7].factor=1.0
load_combinations.create(101, design_situation="DS1", user_defined_name_enabled=True, name="+1.35G", static_analysis_settings="SA2")
load_combinations[101].items[1].load_case=1
load_combinations[101].items[1].factor=1.350000023841858
load_combinations[101].items[2].load_case=2
load_combinations[101].items[2].factor=1.350000023841858
load_combinations[101].items[3].load_case=3
load_combinations[101].items[3].factor=1.350000023841858
load_combinations.create(102, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+1.5QL+1.2QS +1.5QML1+1.2QMS+1.5QV+1.25Qbc", static_analysis_settings="SA2")
load_combinations[102].items[1].load_case=1
load_combinations[102].items[1].factor=1.2000000476837158
load_combinations[102].items[2].load_case=2
load_combinations[102].items[2].factor=1.2000000476837158
load_combinations[102].items[3].load_case=3
load_combinations[102].items[3].factor=1.2000000476837158
load_combinations[102].items[4].load_case=11
load_combinations[102].items[4].factor=1.5
load_combinations[102].items[5].load_case=12
load_combinations[102].items[5].factor=1.2
load_combinations[102].items[6].load_case=13
load_combinations[102].items[6].factor=1.5
load_combinations[102].items[7].load_case=21
load_combinations[102].items[7].factor=1.2
load_combinations[102].items[8].load_case=23
load_combinations[102].items[8].factor=1.5
load_combinations[102].items[9].load_case=24
load_combinations[102].items[9].factor=1.25
load_combinations.create(103, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+1.5QL+1.2QS +1.5QML1+1.2QMS+1.5QV+1.5Qbo+0.2Wuex+0.2Wuix", static_analysis_settings="SA2")
load_combinations[103].items[1].load_case=1
load_combinations[103].items[1].factor=1.2000000476837158
load_combinations[103].items[2].load_case=2
load_combinations[103].items[2].factor=1.2000000476837158
load_combinations[103].items[3].load_case=3
load_combinations[103].items[3].factor=1.2000000476837158
load_combinations[103].items[4].load_case=11
load_combinations[103].items[4].factor=1.5
load_combinations[103].items[5].load_case=12
load_combinations[103].items[5].factor=1.2
load_combinations[103].items[6].load_case=13
load_combinations[103].items[6].factor=1.5
load_combinations[103].items[7].load_case=21
load_combinations[103].items[7].factor=1.2
load_combinations[103].items[8].load_case=23
load_combinations[103].items[8].factor=1.5
load_combinations[103].items[9].load_case=25
load_combinations[103].items[9].factor=1.5
load_combinations[103].items[10].load_case=31
load_combinations[103].items[10].factor=0.2
load_combinations[103].items[11].load_case=32
load_combinations[103].items[11].factor=0.2
load_combinations.create(104, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+1.5QL+1.2QS +1.5QML1+1.2QMS+1.5QV+1.5Qbo+0.2Wdex+0.2Wdix", static_analysis_settings="SA2")
load_combinations[104].items[1].load_case=1
load_combinations[104].items[1].factor=1.2000000476837158
load_combinations[104].items[2].load_case=2
load_combinations[104].items[2].factor=1.2000000476837158
load_combinations[104].items[3].load_case=3
load_combinations[104].items[3].factor=1.2000000476837158
load_combinations[104].items[4].load_case=11
load_combinations[104].items[4].factor=1.5
load_combinations[104].items[5].load_case=12
load_combinations[104].items[5].factor=1.2
load_combinations[104].items[6].load_case=13
load_combinations[104].items[6].factor=1.5
load_combinations[104].items[7].load_case=21
load_combinations[104].items[7].factor=1.2
load_combinations[104].items[8].load_case=23
load_combinations[104].items[8].factor=1.5
load_combinations[104].items[9].load_case=25
load_combinations[104].items[9].factor=1.5
load_combinations[104].items[10].load_case=33
load_combinations[104].items[10].factor=0.2
load_combinations[104].items[11].load_case=34
load_combinations[104].items[11].factor=0.2
load_combinations.create(105, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+1.5QL+1.2QS +1.5QML1+1.2QMS+1.5QV+1.5Qbo+0.2Wuey+0.2Wuiy", static_analysis_settings="SA2")
load_combinations[105].items[1].load_case=1
load_combinations[105].items[1].factor=1.2000000476837158
load_combinations[105].items[2].load_case=2
load_combinations[105].items[2].factor=1.2000000476837158
load_combinations[105].items[3].load_case=3
load_combinations[105].items[3].factor=1.2000000476837158
load_combinations[105].items[4].load_case=11
load_combinations[105].items[4].factor=1.5
load_combinations[105].items[5].load_case=12
load_combinations[105].items[5].factor=1.2
load_combinations[105].items[6].load_case=13
load_combinations[105].items[6].factor=1.5
load_combinations[105].items[7].load_case=21
load_combinations[105].items[7].factor=1.2
load_combinations[105].items[8].load_case=23
load_combinations[105].items[8].factor=1.5
load_combinations[105].items[9].load_case=25
load_combinations[105].items[9].factor=1.5
load_combinations[105].items[10].load_case=35
load_combinations[105].items[10].factor=0.2
load_combinations[105].items[11].load_case=36
load_combinations[105].items[11].factor=0.2
load_combinations.create(106, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+1.5QL+1.2QS +1.5QML1+1.2QMS+1.5QV+1.5Qbo+0.2Wdey+0.2Wdiy", static_analysis_settings="SA2")
load_combinations[106].items[1].load_case=1
load_combinations[106].items[1].factor=1.2000000476837158
load_combinations[106].items[2].load_case=2
load_combinations[106].items[2].factor=1.2000000476837158
load_combinations[106].items[3].load_case=3
load_combinations[106].items[3].factor=1.2000000476837158
load_combinations[106].items[4].load_case=11
load_combinations[106].items[4].factor=1.5
load_combinations[106].items[5].load_case=12
load_combinations[106].items[5].factor=1.2
load_combinations[106].items[6].load_case=13
load_combinations[106].items[6].factor=1.5
load_combinations[106].items[7].load_case=21
load_combinations[106].items[7].factor=1.2
load_combinations[106].items[8].load_case=23
load_combinations[106].items[8].factor=1.5
load_combinations[106].items[9].load_case=25
load_combinations[106].items[9].factor=1.5
load_combinations[106].items[10].load_case=37
load_combinations[106].items[10].factor=0.2
load_combinations[106].items[11].load_case=38
load_combinations[106].items[11].factor=0.2
load_combinations.create(107, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+1.5QL+1.2QS +1.5QML1+1.2QMS+1.5QV+1.5Qbo+0.2-Wuex+0.2-Wuix", static_analysis_settings="SA2")
load_combinations[107].items[1].load_case=1
load_combinations[107].items[1].factor=1.2000000476837158
load_combinations[107].items[2].load_case=2
load_combinations[107].items[2].factor=1.2000000476837158
load_combinations[107].items[3].load_case=3
load_combinations[107].items[3].factor=1.2000000476837158
load_combinations[107].items[4].load_case=11
load_combinations[107].items[4].factor=1.5
load_combinations[107].items[5].load_case=12
load_combinations[107].items[5].factor=1.2
load_combinations[107].items[6].load_case=13
load_combinations[107].items[6].factor=1.5
load_combinations[107].items[7].load_case=21
load_combinations[107].items[7].factor=1.2
load_combinations[107].items[8].load_case=23
load_combinations[107].items[8].factor=1.5
load_combinations[107].items[9].load_case=25
load_combinations[107].items[9].factor=1.5
load_combinations[107].items[10].load_case=39
load_combinations[107].items[10].factor=0.2
load_combinations[107].items[11].load_case=40
load_combinations[107].items[11].factor=0.2
load_combinations.create(108, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+1.5QL+1.2QS +1.5QML1+1.2QMS+1.5QV+1.5Qbo+0.2-Wdex+0.2-Wdix", static_analysis_settings="SA2")
load_combinations[108].items[1].load_case=1
load_combinations[108].items[1].factor=1.2000000476837158
load_combinations[108].items[2].load_case=2
load_combinations[108].items[2].factor=1.2000000476837158
load_combinations[108].items[3].load_case=3
load_combinations[108].items[3].factor=1.2000000476837158
load_combinations[108].items[4].load_case=11
load_combinations[108].items[4].factor=1.5
load_combinations[108].items[5].load_case=12
load_combinations[108].items[5].factor=1.2
load_combinations[108].items[6].load_case=13
load_combinations[108].items[6].factor=1.5
load_combinations[108].items[7].load_case=21
load_combinations[108].items[7].factor=1.2
load_combinations[108].items[8].load_case=23
load_combinations[108].items[8].factor=1.5
load_combinations[108].items[9].load_case=25
load_combinations[108].items[9].factor=1.5
load_combinations[108].items[10].load_case=41
load_combinations[108].items[10].factor=0.2
load_combinations[108].items[11].load_case=42
load_combinations[108].items[11].factor=0.2
load_combinations.create(109, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+1.5QL+1.2QS +1.5QML1+1.2QMS+1.5QV+1.5Qbo+0.2-Wuey+0.2-Wuiy", static_analysis_settings="SA2")
load_combinations[109].items[1].load_case=1
load_combinations[109].items[1].factor=1.2000000476837158
load_combinations[109].items[2].load_case=2
load_combinations[109].items[2].factor=1.2000000476837158
load_combinations[109].items[3].load_case=3
load_combinations[109].items[3].factor=1.2000000476837158
load_combinations[109].items[4].load_case=11
load_combinations[109].items[4].factor=1.5
load_combinations[109].items[5].load_case=12
load_combinations[109].items[5].factor=1.2
load_combinations[109].items[6].load_case=13
load_combinations[109].items[6].factor=1.5
load_combinations[109].items[7].load_case=21
load_combinations[109].items[7].factor=1.2
load_combinations[109].items[8].load_case=23
load_combinations[109].items[8].factor=1.5
load_combinations[109].items[9].load_case=25
load_combinations[109].items[9].factor=1.5
load_combinations[109].items[10].load_case=43
load_combinations[109].items[10].factor=0.2
load_combinations[109].items[11].load_case=44
load_combinations[109].items[11].factor=0.2
load_combinations.create(110, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+1.5QL+1.2QS +1.5QML1+1.2QMS+1.5QV+1.5Qbo+0.2-Wdey+0.2-Wdiy", static_analysis_settings="SA2")
load_combinations[110].items[1].load_case=1
load_combinations[110].items[1].factor=1.2000000476837158
load_combinations[110].items[2].load_case=2
load_combinations[110].items[2].factor=1.2000000476837158
load_combinations[110].items[3].load_case=3
load_combinations[110].items[3].factor=1.2000000476837158
load_combinations[110].items[4].load_case=11
load_combinations[110].items[4].factor=1.5
load_combinations[110].items[5].load_case=12
load_combinations[110].items[5].factor=1.2
load_combinations[110].items[6].load_case=13
load_combinations[110].items[6].factor=1.5
load_combinations[110].items[7].load_case=21
load_combinations[110].items[7].factor=1.2
load_combinations[110].items[8].load_case=23
load_combinations[110].items[8].factor=1.5
load_combinations[110].items[9].load_case=25
load_combinations[110].items[9].factor=1.5
load_combinations[110].items[10].load_case=45
load_combinations[110].items[10].factor=0.2
load_combinations[110].items[11].load_case=46
load_combinations[110].items[11].factor=0.2
load_combinations.create(111, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+1.5QL+1.2QS +1.5QML1+1.9QCpt1+1.2QMS+1.5QV+1.5Qbo", static_analysis_settings="SA2")
load_combinations[111].items[1].load_case=1
load_combinations[111].items[1].factor=1.2000000476837158
load_combinations[111].items[2].load_case=2
load_combinations[111].items[2].factor=1.2000000476837158
load_combinations[111].items[3].load_case=3
load_combinations[111].items[3].factor=1.2000000476837158
load_combinations[111].items[4].load_case=11
load_combinations[111].items[4].factor=1.5
load_combinations[111].items[5].load_case=12
load_combinations[111].items[5].factor=1.2
load_combinations[111].items[6].load_case=13
load_combinations[111].items[6].factor=1.5
load_combinations[111].items[7].load_case=16
load_combinations[111].items[7].factor=1.9
load_combinations[111].items[8].load_case=21
load_combinations[111].items[8].factor=1.2
load_combinations[111].items[9].load_case=23
load_combinations[111].items[9].factor=1.5
load_combinations[111].items[10].load_case=25
load_combinations[111].items[10].factor=1.5
load_combinations.create(112, design_situation="DS1", user_defined_name_enabled=True, name="+1.9QCpt2", static_analysis_settings="SA2")
load_combinations[112].items[1].load_case=26
load_combinations[112].items[1].factor=1.9
load_combinations.create(121, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+0.6QL+1.2QS +1.5QML1+1.5QBTn+0.6QMS+Qbo+Wuex+Wuix", static_analysis_settings="SA2")
load_combinations[121].items[1].load_case=1
load_combinations[121].items[1].factor=1.2000000476837158
load_combinations[121].items[2].load_case=2
load_combinations[121].items[2].factor=1.2000000476837158
load_combinations[121].items[3].load_case=3
load_combinations[121].items[3].factor=1.2000000476837158
load_combinations[121].items[4].load_case=11
load_combinations[121].items[4].factor=0.6
load_combinations[121].items[5].load_case=12
load_combinations[121].items[5].factor=1.2
load_combinations[121].items[6].load_case=13
load_combinations[121].items[6].factor=1.5
load_combinations[121].items[7].load_case=19
load_combinations[121].items[7].factor=1.5
load_combinations[121].items[8].load_case=21
load_combinations[121].items[8].factor=0.6
load_combinations[121].items[9].load_case=25
load_combinations[121].items[9].factor=1.0
load_combinations[121].items[10].load_case=31
load_combinations[121].items[10].factor=1.0
load_combinations[121].items[11].load_case=32
load_combinations[121].items[11].factor=1.0
load_combinations.create(122, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+0.6QL+1.2QS +1.5QML1+1.5QBTn+0.6QMS+Qbo+Wdex+Wdix", static_analysis_settings="SA2")
load_combinations[122].items[1].load_case=1
load_combinations[122].items[1].factor=1.2000000476837158
load_combinations[122].items[2].load_case=2
load_combinations[122].items[2].factor=1.2000000476837158
load_combinations[122].items[3].load_case=3
load_combinations[122].items[3].factor=1.2000000476837158
load_combinations[122].items[4].load_case=11
load_combinations[122].items[4].factor=0.6
load_combinations[122].items[5].load_case=12
load_combinations[122].items[5].factor=1.2
load_combinations[122].items[6].load_case=13
load_combinations[122].items[6].factor=1.5
load_combinations[122].items[7].load_case=19
load_combinations[122].items[7].factor=1.5
load_combinations[122].items[8].load_case=21
load_combinations[122].items[8].factor=0.6
load_combinations[122].items[9].load_case=25
load_combinations[122].items[9].factor=1.0
load_combinations[122].items[10].load_case=33
load_combinations[122].items[10].factor=1.0
load_combinations[122].items[11].load_case=34
load_combinations[122].items[11].factor=1.0
load_combinations.create(123, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+0.6QL+1.2QS +1.5QML1+1.5QBTn+0.6QMS+Qbo+Wuey+Wuiy", static_analysis_settings="SA2")
load_combinations[123].items[1].load_case=1
load_combinations[123].items[1].factor=1.2000000476837158
load_combinations[123].items[2].load_case=2
load_combinations[123].items[2].factor=1.2000000476837158
load_combinations[123].items[3].load_case=3
load_combinations[123].items[3].factor=1.2000000476837158
load_combinations[123].items[4].load_case=11
load_combinations[123].items[4].factor=0.6
load_combinations[123].items[5].load_case=12
load_combinations[123].items[5].factor=1.2
load_combinations[123].items[6].load_case=13
load_combinations[123].items[6].factor=1.5
load_combinations[123].items[7].load_case=19
load_combinations[123].items[7].factor=1.5
load_combinations[123].items[8].load_case=21
load_combinations[123].items[8].factor=0.6
load_combinations[123].items[9].load_case=25
load_combinations[123].items[9].factor=1.0
load_combinations[123].items[10].load_case=35
load_combinations[123].items[10].factor=1.0
load_combinations[123].items[11].load_case=36
load_combinations[123].items[11].factor=1.0
load_combinations.create(124, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+0.6QL+1.2QS +1.5QML1+1.5QBTn+0.6QMS+Qbo+Wdey+Wdiy", static_analysis_settings="SA2")
load_combinations[124].items[1].load_case=1
load_combinations[124].items[1].factor=1.2000000476837158
load_combinations[124].items[2].load_case=2
load_combinations[124].items[2].factor=1.2000000476837158
load_combinations[124].items[3].load_case=3
load_combinations[124].items[3].factor=1.2000000476837158
load_combinations[124].items[4].load_case=11
load_combinations[124].items[4].factor=0.6
load_combinations[124].items[5].load_case=12
load_combinations[124].items[5].factor=1.2
load_combinations[124].items[6].load_case=13
load_combinations[124].items[6].factor=1.5
load_combinations[124].items[7].load_case=19
load_combinations[124].items[7].factor=1.5
load_combinations[124].items[8].load_case=21
load_combinations[124].items[8].factor=0.6
load_combinations[124].items[9].load_case=25
load_combinations[124].items[9].factor=1.0
load_combinations[124].items[10].load_case=37
load_combinations[124].items[10].factor=1.0
load_combinations[124].items[11].load_case=38
load_combinations[124].items[11].factor=1.0
load_combinations.create(125, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+0.6QL+1.2QS +1.5QML1+1.5QBTn+0.6QMS+Qbo+-Wuex+-Wuix", static_analysis_settings="SA2")
load_combinations[125].items[1].load_case=1
load_combinations[125].items[1].factor=1.2000000476837158
load_combinations[125].items[2].load_case=2
load_combinations[125].items[2].factor=1.2000000476837158
load_combinations[125].items[3].load_case=3
load_combinations[125].items[3].factor=1.2000000476837158
load_combinations[125].items[4].load_case=11
load_combinations[125].items[4].factor=0.6
load_combinations[125].items[5].load_case=12
load_combinations[125].items[5].factor=1.2
load_combinations[125].items[6].load_case=13
load_combinations[125].items[6].factor=1.5
load_combinations[125].items[7].load_case=19
load_combinations[125].items[7].factor=1.5
load_combinations[125].items[8].load_case=21
load_combinations[125].items[8].factor=0.6
load_combinations[125].items[9].load_case=25
load_combinations[125].items[9].factor=1.0
load_combinations[125].items[10].load_case=39
load_combinations[125].items[10].factor=1.0
load_combinations[125].items[11].load_case=40
load_combinations[125].items[11].factor=1.0
load_combinations.create(126, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+0.6QL+1.2QS +1.5QML1+1.5QBTn+0.6QMS+Qbo+-Wdex+-Wdix", static_analysis_settings="SA2")
load_combinations[126].items[1].load_case=1
load_combinations[126].items[1].factor=1.2000000476837158
load_combinations[126].items[2].load_case=2
load_combinations[126].items[2].factor=1.2000000476837158
load_combinations[126].items[3].load_case=3
load_combinations[126].items[3].factor=1.2000000476837158
load_combinations[126].items[4].load_case=11
load_combinations[126].items[4].factor=0.6
load_combinations[126].items[5].load_case=12
load_combinations[126].items[5].factor=1.2
load_combinations[126].items[6].load_case=13
load_combinations[126].items[6].factor=1.5
load_combinations[126].items[7].load_case=19
load_combinations[126].items[7].factor=1.5
load_combinations[126].items[8].load_case=21
load_combinations[126].items[8].factor=0.6
load_combinations[126].items[9].load_case=25
load_combinations[126].items[9].factor=1.0
load_combinations[126].items[10].load_case=41
load_combinations[126].items[10].factor=1.0
load_combinations[126].items[11].load_case=42
load_combinations[126].items[11].factor=1.0
load_combinations.create(127, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+0.6QL+1.2QS +1.5QML1+1.5QBTn+0.6QMS+Qbo+-Wuey+-Wuiy", static_analysis_settings="SA2")
load_combinations[127].items[1].load_case=1
load_combinations[127].items[1].factor=1.2000000476837158
load_combinations[127].items[2].load_case=2
load_combinations[127].items[2].factor=1.2000000476837158
load_combinations[127].items[3].load_case=3
load_combinations[127].items[3].factor=1.2000000476837158
load_combinations[127].items[4].load_case=11
load_combinations[127].items[4].factor=0.6
load_combinations[127].items[5].load_case=12
load_combinations[127].items[5].factor=1.2
load_combinations[127].items[6].load_case=13
load_combinations[127].items[6].factor=1.5
load_combinations[127].items[7].load_case=19
load_combinations[127].items[7].factor=1.5
load_combinations[127].items[8].load_case=21
load_combinations[127].items[8].factor=0.6
load_combinations[127].items[9].load_case=25
load_combinations[127].items[9].factor=1.0
load_combinations[127].items[10].load_case=43
load_combinations[127].items[10].factor=1.0
load_combinations[127].items[11].load_case=44
load_combinations[127].items[11].factor=1.0
load_combinations.create(128, design_situation="DS1", user_defined_name_enabled=True, name="+1.2G+0.6QL+1.2QS +1.5QML1+1.5QBTn+0.6QMS+Qbo+-Wdey+-Wdiy", static_analysis_settings="SA2")
load_combinations[128].items[1].load_case=1
load_combinations[128].items[1].factor=1.2000000476837158
load_combinations[128].items[2].load_case=2
load_combinations[128].items[2].factor=1.2000000476837158
load_combinations[128].items[3].load_case=3
load_combinations[128].items[3].factor=1.2000000476837158
load_combinations[128].items[4].load_case=11
load_combinations[128].items[4].factor=0.6
load_combinations[128].items[5].load_case=12
load_combinations[128].items[5].factor=1.2
load_combinations[128].items[6].load_case=13
load_combinations[128].items[6].factor=1.5
load_combinations[128].items[7].load_case=19
load_combinations[128].items[7].factor=1.5
load_combinations[128].items[8].load_case=21
load_combinations[128].items[8].factor=0.6
load_combinations[128].items[9].load_case=25
load_combinations[128].items[9].factor=1.0
load_combinations[128].items[10].load_case=45
load_combinations[128].items[10].factor=1.0
load_combinations[128].items[11].load_case=46
load_combinations[128].items[11].factor=1.0
load_combinations.create(129, design_situation="DS1", user_defined_name_enabled=True, name="+0.9G+1.5QBTn+Wuex+Wuix", static_analysis_settings="SA2")
load_combinations[129].items[1].load_case=1
load_combinations[129].items[1].factor=0.8999999761581421
load_combinations[129].items[2].load_case=2
load_combinations[129].items[2].factor=0.8999999761581421
load_combinations[129].items[3].load_case=3
load_combinations[129].items[3].factor=0.8999999761581421
load_combinations[129].items[4].load_case=19
load_combinations[129].items[4].factor=1.5
load_combinations[129].items[5].load_case=31
load_combinations[129].items[5].factor=1.0
load_combinations[129].items[6].load_case=32
load_combinations[129].items[6].factor=1.0
load_combinations.create(130, design_situation="DS1", user_defined_name_enabled=True, name="+0.9G+1.5QBTn+Wdex+Wdix", static_analysis_settings="SA2")
load_combinations[130].items[1].load_case=1
load_combinations[130].items[1].factor=0.8999999761581421
load_combinations[130].items[2].load_case=2
load_combinations[130].items[2].factor=0.8999999761581421
load_combinations[130].items[3].load_case=3
load_combinations[130].items[3].factor=0.8999999761581421
load_combinations[130].items[4].load_case=19
load_combinations[130].items[4].factor=1.5
load_combinations[130].items[5].load_case=33
load_combinations[130].items[5].factor=1.0
load_combinations[130].items[6].load_case=34
load_combinations[130].items[6].factor=1.0
load_combinations.create(131, design_situation="DS1", user_defined_name_enabled=True, name="+0.9G+1.5QBTn+Wuey+Wuiy", static_analysis_settings="SA2")
load_combinations[131].items[1].load_case=1
load_combinations[131].items[1].factor=0.8999999761581421
load_combinations[131].items[2].load_case=2
load_combinations[131].items[2].factor=0.8999999761581421
load_combinations[131].items[3].load_case=3
load_combinations[131].items[3].factor=0.8999999761581421
load_combinations[131].items[4].load_case=19
load_combinations[131].items[4].factor=1.5
load_combinations[131].items[5].load_case=35
load_combinations[131].items[5].factor=1.0
load_combinations[131].items[6].load_case=36
load_combinations[131].items[6].factor=1.0
load_combinations.create(132, design_situation="DS1", user_defined_name_enabled=True, name="+0.9G+1.5QBTn+Wdey+Wdiy", static_analysis_settings="SA2")
load_combinations[132].items[1].load_case=1
load_combinations[132].items[1].factor=0.8999999761581421
load_combinations[132].items[2].load_case=2
load_combinations[132].items[2].factor=0.8999999761581421
load_combinations[132].items[3].load_case=3
load_combinations[132].items[3].factor=0.8999999761581421
load_combinations[132].items[4].load_case=19
load_combinations[132].items[4].factor=1.5
load_combinations[132].items[5].load_case=37
load_combinations[132].items[5].factor=1.0
load_combinations[132].items[6].load_case=38
load_combinations[132].items[6].factor=1.0
load_combinations.create(133, design_situation="DS1", user_defined_name_enabled=True, name="+0.9G+1.5QBTn+-Wuex+-Wuix", static_analysis_settings="SA2")
load_combinations[133].items[1].load_case=1
load_combinations[133].items[1].factor=0.8999999761581421
load_combinations[133].items[2].load_case=2
load_combinations[133].items[2].factor=0.8999999761581421
load_combinations[133].items[3].load_case=3
load_combinations[133].items[3].factor=0.8999999761581421
load_combinations[133].items[4].load_case=19
load_combinations[133].items[4].factor=1.5
load_combinations[133].items[5].load_case=39
load_combinations[133].items[5].factor=1.0
load_combinations[133].items[6].load_case=40
load_combinations[133].items[6].factor=1.0
load_combinations.create(134, design_situation="DS1", user_defined_name_enabled=True, name="+0.9G+1.5QBTn+-Wdex+-Wdix", static_analysis_settings="SA2")
load_combinations[134].items[1].load_case=1
load_combinations[134].items[1].factor=0.8999999761581421
load_combinations[134].items[2].load_case=2
load_combinations[134].items[2].factor=0.8999999761581421
load_combinations[134].items[3].load_case=3
load_combinations[134].items[3].factor=0.8999999761581421
load_combinations[134].items[4].load_case=19
load_combinations[134].items[4].factor=1.5
load_combinations[134].items[5].load_case=41
load_combinations[134].items[5].factor=1.0
load_combinations[134].items[6].load_case=42
load_combinations[134].items[6].factor=1.0
load_combinations.create(135, design_situation="DS1", user_defined_name_enabled=True, name="+0.9G+1.5QBTn+-Wuey+-Wuiy", static_analysis_settings="SA2")
load_combinations[135].items[1].load_case=1
load_combinations[135].items[1].factor=0.8999999761581421
load_combinations[135].items[2].load_case=2
load_combinations[135].items[2].factor=0.8999999761581421
load_combinations[135].items[3].load_case=3
load_combinations[135].items[3].factor=0.8999999761581421
load_combinations[135].items[4].load_case=19
load_combinations[135].items[4].factor=1.5
load_combinations[135].items[5].load_case=43
load_combinations[135].items[5].factor=1.0
load_combinations[135].items[6].load_case=44
load_combinations[135].items[6].factor=1.0
load_combinations.create(136, design_situation="DS1", user_defined_name_enabled=True, name="+0.9G+1.5QBTn+-Wdey+-Wdiy", static_analysis_settings="SA2")
load_combinations[136].items[1].load_case=1
load_combinations[136].items[1].factor=0.8999999761581421
load_combinations[136].items[2].load_case=2
load_combinations[136].items[2].factor=0.8999999761581421
load_combinations[136].items[3].load_case=3
load_combinations[136].items[3].factor=0.8999999761581421
load_combinations[136].items[4].load_case=19
load_combinations[136].items[4].factor=1.5
load_combinations[136].items[5].load_case=45
load_combinations[136].items[5].factor=1.0
load_combinations[136].items[6].load_case=46
load_combinations[136].items[6].factor=1.0
load_combinations.create(141, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.6QL+QS +QML1+1.5QBTo+0.6QMS+QV+Qbo+Eqx+0.3Eqy", static_analysis_settings="SA2")
load_combinations[141].items[1].load_case=1
load_combinations[141].items[1].factor=1.0
load_combinations[141].items[2].load_case=2
load_combinations[141].items[2].factor=1.0
load_combinations[141].items[3].load_case=3
load_combinations[141].items[3].factor=1.0
load_combinations[141].items[4].load_case=11
load_combinations[141].items[4].factor=0.6
load_combinations[141].items[5].load_case=12
load_combinations[141].items[5].factor=1.0
load_combinations[141].items[6].load_case=13
load_combinations[141].items[6].factor=1.0
load_combinations[141].items[7].load_case=17
load_combinations[141].items[7].factor=1.5
load_combinations[141].items[8].load_case=21
load_combinations[141].items[8].factor=0.6
load_combinations[141].items[9].load_case=23
load_combinations[141].items[9].factor=1.0
load_combinations[141].items[10].load_case=25
load_combinations[141].items[10].factor=1.0
load_combinations[141].items[11].load_case=51
load_combinations[141].items[11].factor=1.0
load_combinations[141].items[12].load_case=52
load_combinations[141].items[12].factor=0.3
load_combinations.create(142, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.6QL+QS +QML1+1.5QBTo+0.6QMS+QV+Qbo+Eqx-0.3Eqy", static_analysis_settings="SA2")
load_combinations[142].items[1].load_case=1
load_combinations[142].items[1].factor=1.0
load_combinations[142].items[2].load_case=2
load_combinations[142].items[2].factor=1.0
load_combinations[142].items[3].load_case=3
load_combinations[142].items[3].factor=1.0
load_combinations[142].items[4].load_case=11
load_combinations[142].items[4].factor=0.6
load_combinations[142].items[5].load_case=12
load_combinations[142].items[5].factor=1.0
load_combinations[142].items[6].load_case=13
load_combinations[142].items[6].factor=1.0
load_combinations[142].items[7].load_case=17
load_combinations[142].items[7].factor=1.5
load_combinations[142].items[8].load_case=21
load_combinations[142].items[8].factor=0.6
load_combinations[142].items[9].load_case=23
load_combinations[142].items[9].factor=1.0
load_combinations[142].items[10].load_case=25
load_combinations[142].items[10].factor=1.0
load_combinations[142].items[11].load_case=51
load_combinations[142].items[11].factor=1.0
load_combinations[142].items[12].load_case=52
load_combinations[142].items[12].factor=-0.3
load_combinations.create(143, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.6QL+QS +QML1+1.5QBTo+0.6QMS+QV+Qbo-Eqx+0.3Eqy", static_analysis_settings="SA2")
load_combinations[143].items[1].load_case=1
load_combinations[143].items[1].factor=1.0
load_combinations[143].items[2].load_case=2
load_combinations[143].items[2].factor=1.0
load_combinations[143].items[3].load_case=3
load_combinations[143].items[3].factor=1.0
load_combinations[143].items[4].load_case=11
load_combinations[143].items[4].factor=0.6
load_combinations[143].items[5].load_case=12
load_combinations[143].items[5].factor=1.0
load_combinations[143].items[6].load_case=13
load_combinations[143].items[6].factor=1.0
load_combinations[143].items[7].load_case=17
load_combinations[143].items[7].factor=1.5
load_combinations[143].items[8].load_case=21
load_combinations[143].items[8].factor=0.6
load_combinations[143].items[9].load_case=23
load_combinations[143].items[9].factor=1.0
load_combinations[143].items[10].load_case=25
load_combinations[143].items[10].factor=1.0
load_combinations[143].items[11].load_case=51
load_combinations[143].items[11].factor=-1.0
load_combinations[143].items[12].load_case=52
load_combinations[143].items[12].factor=0.3
load_combinations.create(144, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.6QL+QS +QML1+1.5QBTo+0.6QMS+QV+Qbo-Eqx-0.3Eqy", static_analysis_settings="SA2")
load_combinations[144].items[1].load_case=1
load_combinations[144].items[1].factor=1.0
load_combinations[144].items[2].load_case=2
load_combinations[144].items[2].factor=1.0
load_combinations[144].items[3].load_case=3
load_combinations[144].items[3].factor=1.0
load_combinations[144].items[4].load_case=11
load_combinations[144].items[4].factor=0.6
load_combinations[144].items[5].load_case=12
load_combinations[144].items[5].factor=1.0
load_combinations[144].items[6].load_case=13
load_combinations[144].items[6].factor=1.0
load_combinations[144].items[7].load_case=17
load_combinations[144].items[7].factor=1.5
load_combinations[144].items[8].load_case=21
load_combinations[144].items[8].factor=0.6
load_combinations[144].items[9].load_case=23
load_combinations[144].items[9].factor=1.0
load_combinations[144].items[10].load_case=25
load_combinations[144].items[10].factor=1.0
load_combinations[144].items[11].load_case=51
load_combinations[144].items[11].factor=-1.0
load_combinations[144].items[12].load_case=52
load_combinations[144].items[12].factor=-0.3
load_combinations.create(145, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.6QL+QS +QML1+1.5QBTo+0.6QMS+QV+Qbo+0.3Eqx+Eqy", static_analysis_settings="SA2")
load_combinations[145].items[1].load_case=1
load_combinations[145].items[1].factor=1.0
load_combinations[145].items[2].load_case=2
load_combinations[145].items[2].factor=1.0
load_combinations[145].items[3].load_case=3
load_combinations[145].items[3].factor=1.0
load_combinations[145].items[4].load_case=11
load_combinations[145].items[4].factor=0.6
load_combinations[145].items[5].load_case=12
load_combinations[145].items[5].factor=1.0
load_combinations[145].items[6].load_case=13
load_combinations[145].items[6].factor=1.0
load_combinations[145].items[7].load_case=17
load_combinations[145].items[7].factor=1.5
load_combinations[145].items[8].load_case=21
load_combinations[145].items[8].factor=0.6
load_combinations[145].items[9].load_case=23
load_combinations[145].items[9].factor=1.0
load_combinations[145].items[10].load_case=25
load_combinations[145].items[10].factor=1.0
load_combinations[145].items[11].load_case=51
load_combinations[145].items[11].factor=0.3
load_combinations[145].items[12].load_case=52
load_combinations[145].items[12].factor=1.0
load_combinations.create(146, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.6QL+QS +QML1+1.5QBTo+0.6QMS+QV+Qbo-0.3Eqx+Eqy", static_analysis_settings="SA2")
load_combinations[146].items[1].load_case=1
load_combinations[146].items[1].factor=1.0
load_combinations[146].items[2].load_case=2
load_combinations[146].items[2].factor=1.0
load_combinations[146].items[3].load_case=3
load_combinations[146].items[3].factor=1.0
load_combinations[146].items[4].load_case=11
load_combinations[146].items[4].factor=0.6
load_combinations[146].items[5].load_case=12
load_combinations[146].items[5].factor=1.0
load_combinations[146].items[6].load_case=13
load_combinations[146].items[6].factor=1.0
load_combinations[146].items[7].load_case=17
load_combinations[146].items[7].factor=1.5
load_combinations[146].items[8].load_case=21
load_combinations[146].items[8].factor=0.6
load_combinations[146].items[9].load_case=23
load_combinations[146].items[9].factor=1.0
load_combinations[146].items[10].load_case=25
load_combinations[146].items[10].factor=1.0
load_combinations[146].items[11].load_case=51
load_combinations[146].items[11].factor=-0.3
load_combinations[146].items[12].load_case=52
load_combinations[146].items[12].factor=1.0
load_combinations.create(147, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.6QL+QS +QML1+1.5QBTo+0.6QMS+QV+Qbo+0.3Eqx-Eqy", static_analysis_settings="SA2")
load_combinations[147].items[1].load_case=1
load_combinations[147].items[1].factor=1.0
load_combinations[147].items[2].load_case=2
load_combinations[147].items[2].factor=1.0
load_combinations[147].items[3].load_case=3
load_combinations[147].items[3].factor=1.0
load_combinations[147].items[4].load_case=11
load_combinations[147].items[4].factor=0.6
load_combinations[147].items[5].load_case=12
load_combinations[147].items[5].factor=1.0
load_combinations[147].items[6].load_case=13
load_combinations[147].items[6].factor=1.0
load_combinations[147].items[7].load_case=17
load_combinations[147].items[7].factor=1.5
load_combinations[147].items[8].load_case=21
load_combinations[147].items[8].factor=0.6
load_combinations[147].items[9].load_case=23
load_combinations[147].items[9].factor=1.0
load_combinations[147].items[10].load_case=25
load_combinations[147].items[10].factor=1.0
load_combinations[147].items[11].load_case=51
load_combinations[147].items[11].factor=0.3
load_combinations[147].items[12].load_case=52
load_combinations[147].items[12].factor=-1.0
load_combinations.create(148, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.6QL+QS +QML1+1.5QBTo+0.6QMS+QV+Qbo-0.3Eqx-Eqy", static_analysis_settings="SA2")
load_combinations[148].items[1].load_case=1
load_combinations[148].items[1].factor=1.0
load_combinations[148].items[2].load_case=2
load_combinations[148].items[2].factor=1.0
load_combinations[148].items[3].load_case=3
load_combinations[148].items[3].factor=1.0
load_combinations[148].items[4].load_case=11
load_combinations[148].items[4].factor=0.6
load_combinations[148].items[5].load_case=12
load_combinations[148].items[5].factor=1.0
load_combinations[148].items[6].load_case=13
load_combinations[148].items[6].factor=1.0
load_combinations[148].items[7].load_case=17
load_combinations[148].items[7].factor=1.5
load_combinations[148].items[8].load_case=21
load_combinations[148].items[8].factor=0.6
load_combinations[148].items[9].load_case=23
load_combinations[148].items[9].factor=1.0
load_combinations[148].items[10].load_case=25
load_combinations[148].items[10].factor=1.0
load_combinations[148].items[11].load_case=51
load_combinations[148].items[11].factor=-0.3
load_combinations[148].items[12].load_case=52
load_combinations[148].items[12].factor=-1.0
load_combinations.create(301, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QBTo+QMS+Qbo", static_analysis_settings="SA2")
load_combinations[301].items[1].load_case=1
load_combinations[301].items[1].factor=1.0
load_combinations[301].items[2].load_case=2
load_combinations[301].items[2].factor=1.0
load_combinations[301].items[3].load_case=3
load_combinations[301].items[3].factor=1.0
load_combinations[301].items[4].load_case=11
load_combinations[301].items[4].factor=0.5
load_combinations[301].items[5].load_case=12
load_combinations[301].items[5].factor=1.0
load_combinations[301].items[6].load_case=13
load_combinations[301].items[6].factor=1.0
load_combinations[301].items[7].load_case=17
load_combinations[301].items[7].factor=1.0
load_combinations[301].items[8].load_case=21
load_combinations[301].items[8].factor=1.0
load_combinations[301].items[9].load_case=25
load_combinations[301].items[9].factor=1.0
load_combinations.create(302, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QBTo+QMS+Qbo+0.48Wuex+0.48Wuix", static_analysis_settings="SA2")
load_combinations[302].items[1].load_case=1
load_combinations[302].items[1].factor=1.0
load_combinations[302].items[2].load_case=2
load_combinations[302].items[2].factor=1.0
load_combinations[302].items[3].load_case=3
load_combinations[302].items[3].factor=1.0
load_combinations[302].items[4].load_case=11
load_combinations[302].items[4].factor=0.5
load_combinations[302].items[5].load_case=12
load_combinations[302].items[5].factor=1.0
load_combinations[302].items[6].load_case=13
load_combinations[302].items[6].factor=1.0
load_combinations[302].items[7].load_case=17
load_combinations[302].items[7].factor=1.0
load_combinations[302].items[8].load_case=21
load_combinations[302].items[8].factor=1.0
load_combinations[302].items[9].load_case=25
load_combinations[302].items[9].factor=1.0
load_combinations[302].items[10].load_case=31
load_combinations[302].items[10].factor=0.48
load_combinations[302].items[11].load_case=32
load_combinations[302].items[11].factor=0.48
load_combinations.create(303, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QBTo+QMS+Qbo+0.48Wdex+0.48Wdix", static_analysis_settings="SA2")
load_combinations[303].items[1].load_case=1
load_combinations[303].items[1].factor=1.0
load_combinations[303].items[2].load_case=2
load_combinations[303].items[2].factor=1.0
load_combinations[303].items[3].load_case=3
load_combinations[303].items[3].factor=1.0
load_combinations[303].items[4].load_case=11
load_combinations[303].items[4].factor=0.5
load_combinations[303].items[5].load_case=12
load_combinations[303].items[5].factor=1.0
load_combinations[303].items[6].load_case=13
load_combinations[303].items[6].factor=1.0
load_combinations[303].items[7].load_case=17
load_combinations[303].items[7].factor=1.0
load_combinations[303].items[8].load_case=21
load_combinations[303].items[8].factor=1.0
load_combinations[303].items[9].load_case=25
load_combinations[303].items[9].factor=1.0
load_combinations[303].items[10].load_case=33
load_combinations[303].items[10].factor=0.48
load_combinations[303].items[11].load_case=34
load_combinations[303].items[11].factor=0.48
load_combinations.create(304, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QBTo+QMS+Qbo+0.48Wuey+0.48Wuiy", static_analysis_settings="SA2")
load_combinations[304].items[1].load_case=1
load_combinations[304].items[1].factor=1.0
load_combinations[304].items[2].load_case=2
load_combinations[304].items[2].factor=1.0
load_combinations[304].items[3].load_case=3
load_combinations[304].items[3].factor=1.0
load_combinations[304].items[4].load_case=11
load_combinations[304].items[4].factor=0.5
load_combinations[304].items[5].load_case=12
load_combinations[304].items[5].factor=1.0
load_combinations[304].items[6].load_case=13
load_combinations[304].items[6].factor=1.0
load_combinations[304].items[7].load_case=17
load_combinations[304].items[7].factor=1.0
load_combinations[304].items[8].load_case=21
load_combinations[304].items[8].factor=1.0
load_combinations[304].items[9].load_case=25
load_combinations[304].items[9].factor=1.0
load_combinations[304].items[10].load_case=35
load_combinations[304].items[10].factor=0.48
load_combinations[304].items[11].load_case=36
load_combinations[304].items[11].factor=0.48
load_combinations.create(305, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QBTo+QMS+Qbo+0.48Wdey+0.48Wdiy", static_analysis_settings="SA2")
load_combinations[305].items[1].load_case=1
load_combinations[305].items[1].factor=1.0
load_combinations[305].items[2].load_case=2
load_combinations[305].items[2].factor=1.0
load_combinations[305].items[3].load_case=3
load_combinations[305].items[3].factor=1.0
load_combinations[305].items[4].load_case=11
load_combinations[305].items[4].factor=0.5
load_combinations[305].items[5].load_case=12
load_combinations[305].items[5].factor=1.0
load_combinations[305].items[6].load_case=13
load_combinations[305].items[6].factor=1.0
load_combinations[305].items[7].load_case=17
load_combinations[305].items[7].factor=1.0
load_combinations[305].items[8].load_case=21
load_combinations[305].items[8].factor=1.0
load_combinations[305].items[9].load_case=25
load_combinations[305].items[9].factor=1.0
load_combinations[305].items[10].load_case=37
load_combinations[305].items[10].factor=0.48
load_combinations[305].items[11].load_case=38
load_combinations[305].items[11].factor=0.48
load_combinations.create(306, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QBTo+QMS+Qbo+0.48-Wuex+0.48-Wuix", static_analysis_settings="SA2")
load_combinations[306].items[1].load_case=1
load_combinations[306].items[1].factor=1.0
load_combinations[306].items[2].load_case=2
load_combinations[306].items[2].factor=1.0
load_combinations[306].items[3].load_case=3
load_combinations[306].items[3].factor=1.0
load_combinations[306].items[4].load_case=11
load_combinations[306].items[4].factor=0.5
load_combinations[306].items[5].load_case=12
load_combinations[306].items[5].factor=1.0
load_combinations[306].items[6].load_case=13
load_combinations[306].items[6].factor=1.0
load_combinations[306].items[7].load_case=17
load_combinations[306].items[7].factor=1.0
load_combinations[306].items[8].load_case=21
load_combinations[306].items[8].factor=1.0
load_combinations[306].items[9].load_case=25
load_combinations[306].items[9].factor=1.0
load_combinations[306].items[10].load_case=39
load_combinations[306].items[10].factor=0.48
load_combinations[306].items[11].load_case=40
load_combinations[306].items[11].factor=0.48
load_combinations.create(307, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QBTo+QMS+Qbo+0.48-Wdex+0.48-Wdix", static_analysis_settings="SA2")
load_combinations[307].items[1].load_case=1
load_combinations[307].items[1].factor=1.0
load_combinations[307].items[2].load_case=2
load_combinations[307].items[2].factor=1.0
load_combinations[307].items[3].load_case=3
load_combinations[307].items[3].factor=1.0
load_combinations[307].items[4].load_case=11
load_combinations[307].items[4].factor=0.5
load_combinations[307].items[5].load_case=12
load_combinations[307].items[5].factor=1.0
load_combinations[307].items[6].load_case=13
load_combinations[307].items[6].factor=1.0
load_combinations[307].items[7].load_case=17
load_combinations[307].items[7].factor=1.0
load_combinations[307].items[8].load_case=21
load_combinations[307].items[8].factor=1.0
load_combinations[307].items[9].load_case=25
load_combinations[307].items[9].factor=1.0
load_combinations[307].items[10].load_case=41
load_combinations[307].items[10].factor=0.48
load_combinations[307].items[11].load_case=42
load_combinations[307].items[11].factor=0.48
load_combinations.create(308, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QBTo+QMS+Qbo+0.48-Wuey+0.48-Wuiy", static_analysis_settings="SA2")
load_combinations[308].items[1].load_case=1
load_combinations[308].items[1].factor=1.0
load_combinations[308].items[2].load_case=2
load_combinations[308].items[2].factor=1.0
load_combinations[308].items[3].load_case=3
load_combinations[308].items[3].factor=1.0
load_combinations[308].items[4].load_case=11
load_combinations[308].items[4].factor=0.5
load_combinations[308].items[5].load_case=12
load_combinations[308].items[5].factor=1.0
load_combinations[308].items[6].load_case=13
load_combinations[308].items[6].factor=1.0
load_combinations[308].items[7].load_case=17
load_combinations[308].items[7].factor=1.0
load_combinations[308].items[8].load_case=21
load_combinations[308].items[8].factor=1.0
load_combinations[308].items[9].load_case=25
load_combinations[308].items[9].factor=1.0
load_combinations[308].items[10].load_case=43
load_combinations[308].items[10].factor=0.48
load_combinations[308].items[11].load_case=44
load_combinations[308].items[11].factor=0.48
load_combinations.create(309, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QBTo+QMS+Qbo+0.48-Wdey+0.48-Wdiy", static_analysis_settings="SA2")
load_combinations[309].items[1].load_case=1
load_combinations[309].items[1].factor=1.0
load_combinations[309].items[2].load_case=2
load_combinations[309].items[2].factor=1.0
load_combinations[309].items[3].load_case=3
load_combinations[309].items[3].factor=1.0
load_combinations[309].items[4].load_case=11
load_combinations[309].items[4].factor=0.5
load_combinations[309].items[5].load_case=12
load_combinations[309].items[5].factor=1.0
load_combinations[309].items[6].load_case=13
load_combinations[309].items[6].factor=1.0
load_combinations[309].items[7].load_case=17
load_combinations[309].items[7].factor=1.0
load_combinations[309].items[8].load_case=21
load_combinations[309].items[8].factor=1.0
load_combinations[309].items[9].load_case=25
load_combinations[309].items[9].factor=1.0
load_combinations[309].items[10].load_case=45
load_combinations[309].items[10].factor=0.48
load_combinations[309].items[11].load_case=46
load_combinations[309].items[11].factor=0.48
load_combinations.create(310, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QCpt1+QBTo+QMS+Qbo+0.2Wuex+0.2Wuix", static_analysis_settings="SA2")
load_combinations[310].items[1].load_case=1
load_combinations[310].items[1].factor=1.0
load_combinations[310].items[2].load_case=2
load_combinations[310].items[2].factor=1.0
load_combinations[310].items[3].load_case=3
load_combinations[310].items[3].factor=1.0
load_combinations[310].items[4].load_case=11
load_combinations[310].items[4].factor=0.5
load_combinations[310].items[5].load_case=12
load_combinations[310].items[5].factor=1.0
load_combinations[310].items[6].load_case=13
load_combinations[310].items[6].factor=1.0
load_combinations[310].items[7].load_case=16
load_combinations[310].items[7].factor=1.0
load_combinations[310].items[8].load_case=17
load_combinations[310].items[8].factor=1.0
load_combinations[310].items[9].load_case=21
load_combinations[310].items[9].factor=1.0
load_combinations[310].items[10].load_case=25
load_combinations[310].items[10].factor=1.0
load_combinations[310].items[11].load_case=31
load_combinations[310].items[11].factor=0.2
load_combinations[310].items[12].load_case=32
load_combinations[310].items[12].factor=0.2
load_combinations.create(311, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QCpt1+QBTo+QMS+Qbo+0.2Wdex+0.2Wdix", static_analysis_settings="SA2")
load_combinations[311].items[1].load_case=1
load_combinations[311].items[1].factor=1.0
load_combinations[311].items[2].load_case=2
load_combinations[311].items[2].factor=1.0
load_combinations[311].items[3].load_case=3
load_combinations[311].items[3].factor=1.0
load_combinations[311].items[4].load_case=11
load_combinations[311].items[4].factor=0.5
load_combinations[311].items[5].load_case=12
load_combinations[311].items[5].factor=1.0
load_combinations[311].items[6].load_case=13
load_combinations[311].items[6].factor=1.0
load_combinations[311].items[7].load_case=16
load_combinations[311].items[7].factor=1.0
load_combinations[311].items[8].load_case=17
load_combinations[311].items[8].factor=1.0
load_combinations[311].items[9].load_case=21
load_combinations[311].items[9].factor=1.0
load_combinations[311].items[10].load_case=25
load_combinations[311].items[10].factor=1.0
load_combinations[311].items[11].load_case=33
load_combinations[311].items[11].factor=0.2
load_combinations[311].items[12].load_case=34
load_combinations[311].items[12].factor=0.2
load_combinations.create(312, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QCpt1+QBTo+QMS+Qbo+0.2Wuey+0.2Wuiy", static_analysis_settings="SA2")
load_combinations[312].items[1].load_case=1
load_combinations[312].items[1].factor=1.0
load_combinations[312].items[2].load_case=2
load_combinations[312].items[2].factor=1.0
load_combinations[312].items[3].load_case=3
load_combinations[312].items[3].factor=1.0
load_combinations[312].items[4].load_case=11
load_combinations[312].items[4].factor=0.5
load_combinations[312].items[5].load_case=12
load_combinations[312].items[5].factor=1.0
load_combinations[312].items[6].load_case=13
load_combinations[312].items[6].factor=1.0
load_combinations[312].items[7].load_case=16
load_combinations[312].items[7].factor=1.0
load_combinations[312].items[8].load_case=17
load_combinations[312].items[8].factor=1.0
load_combinations[312].items[9].load_case=21
load_combinations[312].items[9].factor=1.0
load_combinations[312].items[10].load_case=25
load_combinations[312].items[10].factor=1.0
load_combinations[312].items[11].load_case=35
load_combinations[312].items[11].factor=0.2
load_combinations[312].items[12].load_case=36
load_combinations[312].items[12].factor=0.2
load_combinations.create(313, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QCpt1+QBTo+QMS+Qbo+0.2Wdey+0.2Wdiy", static_analysis_settings="SA2")
load_combinations[313].items[1].load_case=1
load_combinations[313].items[1].factor=1.0
load_combinations[313].items[2].load_case=2
load_combinations[313].items[2].factor=1.0
load_combinations[313].items[3].load_case=3
load_combinations[313].items[3].factor=1.0
load_combinations[313].items[4].load_case=11
load_combinations[313].items[4].factor=0.5
load_combinations[313].items[5].load_case=12
load_combinations[313].items[5].factor=1.0
load_combinations[313].items[6].load_case=13
load_combinations[313].items[6].factor=1.0
load_combinations[313].items[7].load_case=16
load_combinations[313].items[7].factor=1.0
load_combinations[313].items[8].load_case=17
load_combinations[313].items[8].factor=1.0
load_combinations[313].items[9].load_case=21
load_combinations[313].items[9].factor=1.0
load_combinations[313].items[10].load_case=25
load_combinations[313].items[10].factor=1.0
load_combinations[313].items[11].load_case=37
load_combinations[313].items[11].factor=0.2
load_combinations[313].items[12].load_case=38
load_combinations[313].items[12].factor=0.2
load_combinations.create(314, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QCpt1+QBTo+QMS+Qbo+0.2-Wuex+0.2-Wuix", static_analysis_settings="SA2")
load_combinations[314].items[1].load_case=1
load_combinations[314].items[1].factor=1.0
load_combinations[314].items[2].load_case=2
load_combinations[314].items[2].factor=1.0
load_combinations[314].items[3].load_case=3
load_combinations[314].items[3].factor=1.0
load_combinations[314].items[4].load_case=11
load_combinations[314].items[4].factor=0.5
load_combinations[314].items[5].load_case=12
load_combinations[314].items[5].factor=1.0
load_combinations[314].items[6].load_case=13
load_combinations[314].items[6].factor=1.0
load_combinations[314].items[7].load_case=16
load_combinations[314].items[7].factor=1.0
load_combinations[314].items[8].load_case=17
load_combinations[314].items[8].factor=1.0
load_combinations[314].items[9].load_case=21
load_combinations[314].items[9].factor=1.0
load_combinations[314].items[10].load_case=25
load_combinations[314].items[10].factor=1.0
load_combinations[314].items[11].load_case=39
load_combinations[314].items[11].factor=0.2
load_combinations[314].items[12].load_case=40
load_combinations[314].items[12].factor=0.2
load_combinations.create(315, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QCpt1+QBTo+QMS+Qbo+0.2-Wdex+0.2-Wdix", static_analysis_settings="SA2")
load_combinations[315].items[1].load_case=1
load_combinations[315].items[1].factor=1.0
load_combinations[315].items[2].load_case=2
load_combinations[315].items[2].factor=1.0
load_combinations[315].items[3].load_case=3
load_combinations[315].items[3].factor=1.0
load_combinations[315].items[4].load_case=11
load_combinations[315].items[4].factor=0.5
load_combinations[315].items[5].load_case=12
load_combinations[315].items[5].factor=1.0
load_combinations[315].items[6].load_case=13
load_combinations[315].items[6].factor=1.0
load_combinations[315].items[7].load_case=16
load_combinations[315].items[7].factor=1.0
load_combinations[315].items[8].load_case=17
load_combinations[315].items[8].factor=1.0
load_combinations[315].items[9].load_case=21
load_combinations[315].items[9].factor=1.0
load_combinations[315].items[10].load_case=25
load_combinations[315].items[10].factor=1.0
load_combinations[315].items[11].load_case=41
load_combinations[315].items[11].factor=0.2
load_combinations[315].items[12].load_case=42
load_combinations[315].items[12].factor=0.2
load_combinations.create(316, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QCpt1+QBTo+QMS+Qbo+0.2-Wuey+0.2-Wuiy", static_analysis_settings="SA2")
load_combinations[316].items[1].load_case=1
load_combinations[316].items[1].factor=1.0
load_combinations[316].items[2].load_case=2
load_combinations[316].items[2].factor=1.0
load_combinations[316].items[3].load_case=3
load_combinations[316].items[3].factor=1.0
load_combinations[316].items[4].load_case=11
load_combinations[316].items[4].factor=0.5
load_combinations[316].items[5].load_case=12
load_combinations[316].items[5].factor=1.0
load_combinations[316].items[6].load_case=13
load_combinations[316].items[6].factor=1.0
load_combinations[316].items[7].load_case=16
load_combinations[316].items[7].factor=1.0
load_combinations[316].items[8].load_case=17
load_combinations[316].items[8].factor=1.0
load_combinations[316].items[9].load_case=21
load_combinations[316].items[9].factor=1.0
load_combinations[316].items[10].load_case=25
load_combinations[316].items[10].factor=1.0
load_combinations[316].items[11].load_case=43
load_combinations[316].items[11].factor=0.2
load_combinations[316].items[12].load_case=44
load_combinations[316].items[12].factor=0.2
load_combinations.create(317, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QCpt1+QBTo+QMS+Qbo+0.2-Wdey+0.2-Wdiy", static_analysis_settings="SA2")
load_combinations[317].items[1].load_case=1
load_combinations[317].items[1].factor=1.0
load_combinations[317].items[2].load_case=2
load_combinations[317].items[2].factor=1.0
load_combinations[317].items[3].load_case=3
load_combinations[317].items[3].factor=1.0
load_combinations[317].items[4].load_case=11
load_combinations[317].items[4].factor=0.5
load_combinations[317].items[5].load_case=12
load_combinations[317].items[5].factor=1.0
load_combinations[317].items[6].load_case=13
load_combinations[317].items[6].factor=1.0
load_combinations[317].items[7].load_case=16
load_combinations[317].items[7].factor=1.0
load_combinations[317].items[8].load_case=17
load_combinations[317].items[8].factor=1.0
load_combinations[317].items[9].load_case=21
load_combinations[317].items[9].factor=1.0
load_combinations[317].items[10].load_case=25
load_combinations[317].items[10].factor=1.0
load_combinations[317].items[11].load_case=45
load_combinations[317].items[11].factor=0.2
load_combinations[317].items[12].load_case=46
load_combinations[317].items[12].factor=0.2
load_combinations.create(318, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QCpt2+QBTo+QMS+Qbo+0.2Wuex+0.2Wuix", static_analysis_settings="SA2")
load_combinations[318].items[1].load_case=1
load_combinations[318].items[1].factor=1.0
load_combinations[318].items[2].load_case=2
load_combinations[318].items[2].factor=1.0
load_combinations[318].items[3].load_case=3
load_combinations[318].items[3].factor=1.0
load_combinations[318].items[4].load_case=11
load_combinations[318].items[4].factor=0.5
load_combinations[318].items[5].load_case=12
load_combinations[318].items[5].factor=1.0
load_combinations[318].items[6].load_case=13
load_combinations[318].items[6].factor=1.0
load_combinations[318].items[7].load_case=17
load_combinations[318].items[7].factor=1.0
load_combinations[318].items[8].load_case=21
load_combinations[318].items[8].factor=1.0
load_combinations[318].items[9].load_case=25
load_combinations[318].items[9].factor=1.0
load_combinations[318].items[10].load_case=26
load_combinations[318].items[10].factor=1.0
load_combinations[318].items[11].load_case=31
load_combinations[318].items[11].factor=0.2
load_combinations[318].items[12].load_case=32
load_combinations[318].items[12].factor=0.2
load_combinations.create(319, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QCpt2+QBTo+QMS+Qbo+0.2Wdex+0.2Wdix", static_analysis_settings="SA2")
load_combinations[319].items[1].load_case=1
load_combinations[319].items[1].factor=1.0
load_combinations[319].items[2].load_case=2
load_combinations[319].items[2].factor=1.0
load_combinations[319].items[3].load_case=3
load_combinations[319].items[3].factor=1.0
load_combinations[319].items[4].load_case=11
load_combinations[319].items[4].factor=0.5
load_combinations[319].items[5].load_case=12
load_combinations[319].items[5].factor=1.0
load_combinations[319].items[6].load_case=13
load_combinations[319].items[6].factor=1.0
load_combinations[319].items[7].load_case=17
load_combinations[319].items[7].factor=1.0
load_combinations[319].items[8].load_case=21
load_combinations[319].items[8].factor=1.0
load_combinations[319].items[9].load_case=25
load_combinations[319].items[9].factor=1.0
load_combinations[319].items[10].load_case=26
load_combinations[319].items[10].factor=1.0
load_combinations[319].items[11].load_case=33
load_combinations[319].items[11].factor=0.2
load_combinations[319].items[12].load_case=34
load_combinations[319].items[12].factor=0.2
load_combinations.create(320, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QCpt2+QBTo+QMS+Qbo+0.2Wuey+0.2Wuiy", static_analysis_settings="SA2")
load_combinations[320].items[1].load_case=1
load_combinations[320].items[1].factor=1.0
load_combinations[320].items[2].load_case=2
load_combinations[320].items[2].factor=1.0
load_combinations[320].items[3].load_case=3
load_combinations[320].items[3].factor=1.0
load_combinations[320].items[4].load_case=11
load_combinations[320].items[4].factor=0.5
load_combinations[320].items[5].load_case=12
load_combinations[320].items[5].factor=1.0
load_combinations[320].items[6].load_case=13
load_combinations[320].items[6].factor=1.0
load_combinations[320].items[7].load_case=17
load_combinations[320].items[7].factor=1.0
load_combinations[320].items[8].load_case=21
load_combinations[320].items[8].factor=1.0
load_combinations[320].items[9].load_case=25
load_combinations[320].items[9].factor=1.0
load_combinations[320].items[10].load_case=26
load_combinations[320].items[10].factor=1.0
load_combinations[320].items[11].load_case=35
load_combinations[320].items[11].factor=0.2
load_combinations[320].items[12].load_case=36
load_combinations[320].items[12].factor=0.2
load_combinations.create(321, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QCpt2+QBTo+QMS+Qbo+0.2Wdey+0.2Wdiy", static_analysis_settings="SA2")
load_combinations[321].items[1].load_case=1
load_combinations[321].items[1].factor=1.0
load_combinations[321].items[2].load_case=2
load_combinations[321].items[2].factor=1.0
load_combinations[321].items[3].load_case=3
load_combinations[321].items[3].factor=1.0
load_combinations[321].items[4].load_case=11
load_combinations[321].items[4].factor=0.5
load_combinations[321].items[5].load_case=12
load_combinations[321].items[5].factor=1.0
load_combinations[321].items[6].load_case=13
load_combinations[321].items[6].factor=1.0
load_combinations[321].items[7].load_case=17
load_combinations[321].items[7].factor=1.0
load_combinations[321].items[8].load_case=21
load_combinations[321].items[8].factor=1.0
load_combinations[321].items[9].load_case=25
load_combinations[321].items[9].factor=1.0
load_combinations[321].items[10].load_case=26
load_combinations[321].items[10].factor=1.0
load_combinations[321].items[11].load_case=37
load_combinations[321].items[11].factor=0.2
load_combinations[321].items[12].load_case=38
load_combinations[321].items[12].factor=0.2
load_combinations.create(322, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QCpt2+QBTo+QMS+Qbo+0.2-Wuex+0.2-Wuix", static_analysis_settings="SA2")
load_combinations[322].items[1].load_case=1
load_combinations[322].items[1].factor=1.0
load_combinations[322].items[2].load_case=2
load_combinations[322].items[2].factor=1.0
load_combinations[322].items[3].load_case=3
load_combinations[322].items[3].factor=1.0
load_combinations[322].items[4].load_case=11
load_combinations[322].items[4].factor=0.5
load_combinations[322].items[5].load_case=12
load_combinations[322].items[5].factor=1.0
load_combinations[322].items[6].load_case=13
load_combinations[322].items[6].factor=1.0
load_combinations[322].items[7].load_case=17
load_combinations[322].items[7].factor=1.0
load_combinations[322].items[8].load_case=21
load_combinations[322].items[8].factor=1.0
load_combinations[322].items[9].load_case=25
load_combinations[322].items[9].factor=1.0
load_combinations[322].items[10].load_case=26
load_combinations[322].items[10].factor=1.0
load_combinations[322].items[11].load_case=39
load_combinations[322].items[11].factor=0.2
load_combinations[322].items[12].load_case=40
load_combinations[322].items[12].factor=0.2
load_combinations.create(323, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QCpt2+QBTo+QMS+Qbo+0.2-Wdex+0.2-Wdix", static_analysis_settings="SA2")
load_combinations[323].items[1].load_case=1
load_combinations[323].items[1].factor=1.0
load_combinations[323].items[2].load_case=2
load_combinations[323].items[2].factor=1.0
load_combinations[323].items[3].load_case=3
load_combinations[323].items[3].factor=1.0
load_combinations[323].items[4].load_case=11
load_combinations[323].items[4].factor=0.5
load_combinations[323].items[5].load_case=12
load_combinations[323].items[5].factor=1.0
load_combinations[323].items[6].load_case=13
load_combinations[323].items[6].factor=1.0
load_combinations[323].items[7].load_case=17
load_combinations[323].items[7].factor=1.0
load_combinations[323].items[8].load_case=21
load_combinations[323].items[8].factor=1.0
load_combinations[323].items[9].load_case=25
load_combinations[323].items[9].factor=1.0
load_combinations[323].items[10].load_case=26
load_combinations[323].items[10].factor=1.0
load_combinations[323].items[11].load_case=41
load_combinations[323].items[11].factor=0.2
load_combinations[323].items[12].load_case=42
load_combinations[323].items[12].factor=0.2
load_combinations.create(324, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QCpt2+QBTo+QMS+Qbo+0.2-Wuey+0.2-Wuiy", static_analysis_settings="SA2")
load_combinations[324].items[1].load_case=1
load_combinations[324].items[1].factor=1.0
load_combinations[324].items[2].load_case=2
load_combinations[324].items[2].factor=1.0
load_combinations[324].items[3].load_case=3
load_combinations[324].items[3].factor=1.0
load_combinations[324].items[4].load_case=11
load_combinations[324].items[4].factor=0.5
load_combinations[324].items[5].load_case=12
load_combinations[324].items[5].factor=1.0
load_combinations[324].items[6].load_case=13
load_combinations[324].items[6].factor=1.0
load_combinations[324].items[7].load_case=17
load_combinations[324].items[7].factor=1.0
load_combinations[324].items[8].load_case=21
load_combinations[324].items[8].factor=1.0
load_combinations[324].items[9].load_case=25
load_combinations[324].items[9].factor=1.0
load_combinations[324].items[10].load_case=26
load_combinations[324].items[10].factor=1.0
load_combinations[324].items[11].load_case=43
load_combinations[324].items[11].factor=0.2
load_combinations[324].items[12].load_case=44
load_combinations[324].items[12].factor=0.2
load_combinations.create(325, design_situation="DS1", user_defined_name_enabled=True, name="+G+0.5QL+QS +QML1+QCpt2+QBTo+QMS+Qbo+0.2-Wdey+0.2-Wdiy", static_analysis_settings="SA2")
load_combinations[325].items[1].load_case=1
load_combinations[325].items[1].factor=1.0
load_combinations[325].items[2].load_case=2
load_combinations[325].items[2].factor=1.0
load_combinations[325].items[3].load_case=3
load_combinations[325].items[3].factor=1.0
load_combinations[325].items[4].load_case=11
load_combinations[325].items[4].factor=0.5
load_combinations[325].items[5].load_case=12
load_combinations[325].items[5].factor=1.0
load_combinations[325].items[6].load_case=13
load_combinations[325].items[6].factor=1.0
load_combinations[325].items[7].load_case=17
load_combinations[325].items[7].factor=1.0
load_combinations[325].items[8].load_case=21
load_combinations[325].items[8].factor=1.0
load_combinations[325].items[9].load_case=25
load_combinations[325].items[9].factor=1.0
load_combinations[325].items[10].load_case=26
load_combinations[325].items[10].factor=1.0
load_combinations[325].items[11].load_case=45
load_combinations[325].items[11].factor=0.2
load_combinations[325].items[12].load_case=46
load_combinations[325].items[12].factor=0.2

# Create Nodal Loads
load_cases[3].nodal_loads.create_force(1, "110,126", -25000.0, load_direction="W", load_case=3)
load_cases[3].nodal_loads.create_force(2, "141,142,145,146", -45000.0, load_direction="W", load_case=3)
load_cases[3].nodal_loads.create_force(3, "175,176,205,209,271,276,277,303", -2500.0, load_direction="W", load_case=3)
load_cases[16].nodal_loads.create_force(1, "72", -600.0, load_case=16)
load_cases[16].nodal_loads.create_force(2, "72", -16500.0, load_direction="W", load_case=16)
load_cases[25].nodal_loads.create_force(1, "110,126", -138000.0, load_direction="W", load_case=25)
load_cases[25].nodal_loads.create_force(2, "141,142,145,146", -3000.0, load_direction="W", load_case=25)
load_cases[31].nodal_loads.create_force(1, "141,142,145,146", 5600.0, load_case=31)
load_cases[31].nodal_loads.create_force(2, "338,347", 5740.0, load_case=31)
load_cases[33].nodal_loads.create_force(1, "141,142,145,146", 5600.0, load_case=33)
load_cases[33].nodal_loads.create_force(2, "338,347", 5740.0, load_case=33)
load_cases[35].nodal_loads.create_force(1, "338,347", 11000.0, load_direction="V", load_case=35)
load_cases[37].nodal_loads.create_force(1, "338,347", 11000.0, load_direction="V", load_case=37)
load_cases[39].nodal_loads.create_force(1, "338,347", -5740.0, load_case=39)
load_cases[41].nodal_loads.create_force(1, "338,347", -5740.0, load_case=41)
load_cases[43].nodal_loads.create_force(1, "338,347", -11000.0, load_direction="V", load_case=43)
load_cases[45].nodal_loads.create_force(1, "338,347", -11000.0, load_direction="V", load_case=45)
load_cases[51].nodal_loads.create_force(1, "2,4", 35.18, load_case=51)
load_cases[51].nodal_loads.create_force(2, "6,8", 91.04, load_case=51)
load_cases[51].nodal_loads.create_force(3, "14,16,227,330", 19.67, load_case=51)
load_cases[51].nodal_loads.create_force(4, "17", 89.479996, load_case=51)
load_cases[51].nodal_loads.create_force(5, "18", 244.66, load_case=51)
load_cases[51].nodal_loads.create_force(6, "19", 217.23001, load_case=51)
load_cases[51].nodal_loads.create_force(7, "20,259,262", 319.38998, load_case=51)
load_cases[51].nodal_loads.create_force(8, "21", 165.0, load_case=51)
load_cases[51].nodal_loads.create_force(9, "22", 276.16, load_case=51)
load_cases[51].nodal_loads.create_force(10, "23", 73.48, load_case=51)
load_cases[51].nodal_loads.create_force(11, "24", 127.49, load_case=51)
load_cases[51].nodal_loads.create_force(12, "25", 137.15001, load_case=51)
load_cases[51].nodal_loads.create_force(13, "26", 311.34, load_case=51)
load_cases[51].nodal_loads.create_force(14, "27", 338.77, load_case=51)
load_cases[51].nodal_loads.create_force(15, "28", 164.58, load_case=51)
load_cases[51].nodal_loads.create_force(16, "29", 92.15, load_case=51)
load_cases[51].nodal_loads.create_force(17, "30", 209.18, load_case=51)
load_cases[51].nodal_loads.create_force(18, "31", 227.61, load_case=51)
load_cases[51].nodal_loads.create_force(19, "32", 110.579994, load_case=51)
load_cases[51].nodal_loads.create_force(20, "33,34,35,37,43", 368.6, load_case=51)
load_cases[51].nodal_loads.create_force(21, "36,38,39,42,44,165", 180.01001, load_case=51)
load_cases[51].nodal_loads.create_force(22, "40", 278.59, load_case=51)
load_cases[51].nodal_loads.create_force(23, "41,161", 90.01, load_case=51)
load_cases[51].nodal_loads.create_force(24, "45,46,50", 442.31998, load_case=51)
load_cases[51].nodal_loads.create_force(25, "47", 334.31, load_case=51)
load_cases[51].nodal_loads.create_force(26, "48,163", 108.01, load_case=51)
load_cases[51].nodal_loads.create_force(27, "49,51,52,167", 216.01001, load_case=51)
load_cases[51].nodal_loads.create_force(28, "53,55,56,57,63", 468.12, load_case=51)
load_cases[51].nodal_loads.create_force(29, "54,60", 234.06, load_case=51)
load_cases[51].nodal_loads.create_force(30, "58,59,64,65,67,138,152,162", 228.62, load_case=51)
load_cases[51].nodal_loads.create_force(31, "61,62,68", 114.31, load_case=51)
load_cases[51].nodal_loads.create_force(32, "66", 353.81, load_case=51)
load_cases[51].nodal_loads.create_force(33, "73", 59.16, load_case=51)
load_cases[51].nodal_loads.create_force(34, "74", 153.08, load_case=51)
load_cases[51].nodal_loads.create_force(35, "75,189,218,328", 25.78, load_case=51)
load_cases[51].nodal_loads.create_force(36, "77", 382.47998, load_case=51)
load_cases[51].nodal_loads.create_force(37, "78", 318.77, load_case=51)
load_cases[51].nodal_loads.create_force(38, "80", 203.74, load_case=51)
load_cases[51].nodal_loads.create_force(39, "81", 105.88, load_case=51)
load_cases[51].nodal_loads.create_force(40, "83", 131.39, load_case=51)
load_cases[51].nodal_loads.create_force(41, "84", 142.18999, load_case=51)
load_cases[51].nodal_loads.create_force(42, "85", 4433.0903, load_case=51)
load_cases[51].nodal_loads.create_force(43, "86", 165.94, load_case=51)
load_cases[51].nodal_loads.create_force(44, "92,93", 358.43, load_case=51)
load_cases[51].nodal_loads.create_force(45, "94", 46.829998, load_case=51)
load_cases[51].nodal_loads.create_force(46, "95", 63.150005, load_case=51)
load_cases[51].nodal_loads.create_force(47, "96,204", 63.129997, load_case=51)
load_cases[51].nodal_loads.create_force(48, "110,126", 29081.05, load_case=51)
load_cases[51].nodal_loads.create_force(49, "124", 56.95, load_case=51)
load_cases[51].nodal_loads.create_force(50, "128", 133.0, load_case=51)
load_cases[51].nodal_loads.create_force(51, "129", 159.51, load_case=51)
load_cases[51].nodal_loads.create_force(52, "135", 113.15, load_case=51)
load_cases[51].nodal_loads.create_force(53, "140", 169.54001, load_case=51)
load_cases[51].nodal_loads.create_force(54, "141,142,145,146", 4150.04, load_case=51)
load_cases[51].nodal_loads.create_force(55, "149", 239.5, load_case=51)
load_cases[51].nodal_loads.create_force(56, "151", 32.25, load_case=51)
load_cases[51].nodal_loads.create_force(57, "153", 28.279999, load_case=51)
load_cases[51].nodal_loads.create_force(58, "155", 62.28, load_case=51)
load_cases[51].nodal_loads.create_force(59, "156", 61.59, load_case=51)
load_cases[51].nodal_loads.create_force(60, "164", 204.31, load_case=51)
load_cases[51].nodal_loads.create_force(61, "166", 222.32, load_case=51)
load_cases[51].nodal_loads.create_force(62, "169", 38.34, load_case=51)
load_cases[51].nodal_loads.create_force(63, "170", 205.86, load_case=51)
load_cases[51].nodal_loads.create_force(64, "171,185", 29.73, load_case=51)
load_cases[51].nodal_loads.create_force(65, "172", 232.9, load_case=51)
load_cases[51].nodal_loads.create_force(66, "173", 214.04, load_case=51)
load_cases[51].nodal_loads.create_force(67, "174,207", 176.12, load_case=51)
load_cases[51].nodal_loads.create_force(68, "175", 783.52997, load_case=51)
load_cases[51].nodal_loads.create_force(69, "176,205", 718.84, load_case=51)
load_cases[51].nodal_loads.create_force(70, "177", 360.49, load_case=51)
load_cases[51].nodal_loads.create_force(71, "178", 121.72, load_case=51)
load_cases[51].nodal_loads.create_force(72, "179,206", 9.01, load_case=51)
load_cases[51].nodal_loads.create_force(73, "181,226", 28.06, load_case=51)
load_cases[51].nodal_loads.create_force(74, "182", 94.29, load_case=51)
load_cases[51].nodal_loads.create_force(75, "183", 260.95, load_case=51)
load_cases[51].nodal_loads.create_force(76, "184", 49.03, load_case=51)
load_cases[51].nodal_loads.create_force(77, "186,187", 51.690002, load_case=51)
load_cases[51].nodal_loads.create_force(78, "188,191", 133.76001, load_case=51)
load_cases[51].nodal_loads.create_force(79, "192,329", 28.2, load_case=51)
load_cases[51].nodal_loads.create_force(80, "194", 176.81, load_case=51)
load_cases[51].nodal_loads.create_force(81, "195", 188.19, load_case=51)
load_cases[51].nodal_loads.create_force(82, "196", 205.3, load_case=51)
load_cases[51].nodal_loads.create_force(83, "197", 180.87, load_case=51)
load_cases[51].nodal_loads.create_force(84, "198", 86.51, load_case=51)
load_cases[51].nodal_loads.create_force(85, "199", 79.29, load_case=51)
load_cases[51].nodal_loads.create_force(86, "200", 92.01, load_case=51)
load_cases[51].nodal_loads.create_force(87, "201", 85.380005, load_case=51)
load_cases[51].nodal_loads.create_force(88, "202", 162.92, load_case=51)
load_cases[51].nodal_loads.create_force(89, "203", 206.5, load_case=51)
load_cases[51].nodal_loads.create_force(90, "208", 38.120003, load_case=51)
load_cases[51].nodal_loads.create_force(91, "209", 781.87, load_case=51)
load_cases[51].nodal_loads.create_force(92, "210", 11.55, load_case=51)
load_cases[51].nodal_loads.create_force(93, "211,214", 303.19, load_case=51)
load_cases[51].nodal_loads.create_force(94, "212,215", 800.94, load_case=51)
load_cases[51].nodal_loads.create_force(95, "213", 205.1, load_case=51)
load_cases[51].nodal_loads.create_force(96, "216", 168.54001, load_case=51)
load_cases[51].nodal_loads.create_force(97, "222", 310.07, load_case=51)
load_cases[51].nodal_loads.create_force(98, "223", 313.67, load_case=51)
load_cases[51].nodal_loads.create_force(99, "224", 35.51, load_case=51)
load_cases[51].nodal_loads.create_force(100, "225", 2.56, load_case=51)
load_cases[51].nodal_loads.create_force(101, "228,231", 235.59, load_case=51)
load_cases[51].nodal_loads.create_force(102, "229", 166.14, load_case=51)
load_cases[51].nodal_loads.create_force(103, "230", 282.54, load_case=51)
load_cases[51].nodal_loads.create_force(104, "232,299", 9.0199995, load_case=51)
load_cases[51].nodal_loads.create_force(105, "233,273", 300.06, load_case=51)
load_cases[51].nodal_loads.create_force(106, "235,290", 260.69, load_case=51)
load_cases[51].nodal_loads.create_force(107, "237", 281.33, load_case=51)
load_cases[51].nodal_loads.create_force(108, "251", 179.22, load_case=51)
load_cases[51].nodal_loads.create_force(109, "253,255", 193.21, load_case=51)
load_cases[51].nodal_loads.create_force(110, "254", 197.16, load_case=51)
load_cases[51].nodal_loads.create_force(111, "256,261", 187.48, load_case=51)
load_cases[51].nodal_loads.create_force(112, "257", 201.62, load_case=51)
load_cases[51].nodal_loads.create_force(113, "264", 207.65001, load_case=51)
load_cases[51].nodal_loads.create_force(114, "265,275,279,288", 108.11, load_case=51)
load_cases[51].nodal_loads.create_force(115, "266,278", 139.41, load_case=51)
load_cases[51].nodal_loads.create_force(116, "267,268,272,274", 181.19, load_case=51)
load_cases[51].nodal_loads.create_force(117, "269,287", 138.61, load_case=51)
load_cases[51].nodal_loads.create_force(118, "270,322", 104.27, load_case=51)
load_cases[51].nodal_loads.create_force(119, "271", 925.42, load_case=51)
load_cases[51].nodal_loads.create_force(120, "276,303", 873.32, load_case=51)
load_cases[51].nodal_loads.create_force(121, "277", 926.79, load_case=51)
load_cases[51].nodal_loads.create_force(122, "280", 11.62, load_case=51)
load_cases[51].nodal_loads.create_force(123, "282,284", 270.43, load_case=51)
load_cases[51].nodal_loads.create_force(124, "286", 126.880005, load_case=51)
load_cases[51].nodal_loads.create_force(125, "301,302", 16.310001, load_case=51)
load_cases[51].nodal_loads.create_force(126, "304", 8.16, load_case=51)
load_cases[51].nodal_loads.create_force(127, "306,310", 72.729996, load_case=51)
load_cases[51].nodal_loads.create_force(128, "307", 79.56, load_case=51)
load_cases[51].nodal_loads.create_force(129, "308", 100.149994, load_case=51)
load_cases[51].nodal_loads.create_force(130, "309,312", 55.5, load_case=51)
load_cases[51].nodal_loads.create_force(131, "311", 79.159996, load_case=51)
load_cases[51].nodal_loads.create_force(132, "313", 74.74, load_case=51)
load_cases[51].nodal_loads.create_force(133, "314,319", 269.80002, load_case=51)
load_cases[51].nodal_loads.create_force(134, "315", 138.17, load_case=51)
load_cases[51].nodal_loads.create_force(135, "317", 11.34, load_case=51)
load_cases[51].nodal_loads.create_force(136, "336", 134.48, load_case=51)
load_cases[52].nodal_loads.create_force(1, "2,4", 35.18429, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(2, "6,8", 91.03932, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(3, "14,16,227,330", 19.66771, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(4, "17", 89.47763, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(5, "18", 244.6556, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(6, "19", 217.2349, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(7, "20", 319.392, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(8, "21", 164.9981, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(9, "22", 276.1558, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(10, "23", 73.48368, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(11, "24", 127.487404, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(12, "25", 137.1524, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(13, "26", 311.33588, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(14, "27", 338.76648, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(15, "28", 164.58281, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(16, "29", 92.14925, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(17, "30", 209.1788, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(18, "31", 227.60869, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(19, "32", 110.5791, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(20, "33,34,35,37,43", 368.59702, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(21, "36,38,39,42,44,165", 180.0125, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(22, "40", 278.5907, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(23, "41,161", 90.00625, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(24, "45,46,50", 442.3164, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(25, "47", 334.3089, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(26, "48,163", 108.0075, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(27, "49,51,52,167", 216.015, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(28, "53,55,56,57,63", 468.1184, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(29, "54,60", 234.0591, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(30, "58,59,64,65,67,138,152,162", 228.61589, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(31, "61,62,68", 114.3079, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(32, "66", 353.8104, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(33, "73", 59.16043, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(34, "74", 153.0776, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(35, "75,218", 25.7822, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(36, "77", 382.47888, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(37, "78", 318.77368, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(38, "80", 203.74051, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(39, "81", 105.8769, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(40, "83", 131.3934, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(41, "84", 142.1911, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(42, "85", 4433.0923, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(43, "86", 165.94159, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(44, "92,93", 358.431, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(45, "94", 46.83378, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(46, "95", 63.14649, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(47, "96,204", 63.13019, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(48, "110,126", 29081.05, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(49, "124", 56.95211, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(50, "128", 133.0036, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(51, "129", 159.5074, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(52, "135", 113.1507, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(53, "140", 169.54149, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(54, "141,142,145,146", 4150.042, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(55, "149", 239.50229, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(56, "151", 32.24749, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(57, "153", 28.27998, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(58, "155", 62.280552, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(59, "156", 61.58854, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(60, "164", 204.31421, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(61, "166", 222.3154, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(62, "169", 38.337772, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(63, "170", 205.8603, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(64, "171,185", 29.73017, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(65, "172", 232.9019, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(66, "173", 214.0434, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(67, "174,207", 176.1249, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(68, "175", 783.5303, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(69, "176,205", 718.8429, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(70, "177", 360.4896, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(71, "178", 121.723694, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(72, "179,206", 9.009143, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(73, "181,226", 28.0604, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(74, "182", 94.29225, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(75, "183", 260.9479, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(76, "184", 49.03441, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(77, "186,187", 51.69338, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(78, "188,191", 133.75659, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(79, "189,328", 25.78472, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(80, "192,329", 28.202839, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(81, "194", 176.8112, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(82, "195", 188.1875, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(83, "196", 205.2954, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(84, "197", 180.869, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(85, "198", 86.51173, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(86, "199", 79.28518, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(87, "200", 92.00639, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(88, "201", 85.384254, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(89, "202", 162.9232, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(90, "203", 206.5026, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(91, "208", 38.11707, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(92, "209", 781.8717, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(93, "210", 11.550631, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(94, "211,214", 303.1947, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(95, "212,215", 800.93933, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(96, "213", 205.0979, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(97, "216", 168.5406, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(98, "222", 310.0709, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(99, "223", 313.6727, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(100, "224", 35.51323, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(101, "225", 2.556533, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(102, "228,231", 235.5853, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(103, "229", 166.1414, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(104, "230", 282.5358, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(105, "232,299", 9.016573, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(106, "233,273", 300.0643, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(107, "235,290", 260.69, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(108, "237", 281.3319, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(109, "251", 179.2155, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(110, "253,255", 193.2123, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(111, "254", 197.1595, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(112, "256,261", 187.4754, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(113, "257", 201.62439, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(114, "259,262", 319.3877, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(115, "264", 207.6499, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(116, "265,275,279,288", 108.109695, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(117, "266,278", 139.4101, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(118, "267,268,272,274", 181.1948, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(119, "269,287", 138.6075, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(120, "270,322", 104.272095, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(121, "271", 925.4164, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(122, "276,303", 873.316, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(123, "277", 926.78735, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(124, "280", 11.61751, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(125, "282,284", 270.4252, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(126, "286", 126.8798, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(127, "301,302", 16.31116, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(128, "304", 8.156355, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(129, "306", 72.73326, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(130, "307", 79.56338, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(131, "308", 100.151596, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(132, "309,312", 55.50051, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(133, "310", 72.72632, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(134, "311", 79.161545, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(135, "313", 74.736664, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(136, "314,319", 269.80402, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(137, "315", 138.1713, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(138, "317", 11.33791, load_direction="V", load_case=52)
load_cases[52].nodal_loads.create_force(139, "336", 134.4808, load_direction="V", load_case=52)

# Create Member Loads - Concentrated
load_cases[3].member_loads.create_force(13, "129", "Concentrated - 1", load_case=3, magnitude=-6000.0, distance_a_is_defined_as_relative=True, distance_a_relative=1.0)
load_cases[3].member_loads.create_force(14, "149,390,433", "Concentrated - 1", load_case=3, magnitude=-1500.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.5)
load_cases[3].member_loads.create_force(15, "438,440", "Concentrated - 1", load_case=3, magnitude=-2100.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.5)
load_cases[12].member_loads.create_force(29, "418,420", "Concentrated - 1", load_case=12, magnitude=-1600.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.5)
load_cases[24].member_loads.create_force(9, "149,390,433", "Concentrated - 1", load_case=24, magnitude=-4500.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.5)
load_cases[24].member_loads.create_force(10, "438,440", "Concentrated - 1", load_case=24, magnitude=-5000.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.5)
load_cases[25].member_loads.create_force(13, "129", "Concentrated - 1", load_case=25, magnitude=-33350.0, distance_a_is_defined_as_relative=True, distance_a_relative=1.0)
load_cases[25].member_loads.create_force(14, "149,390,433", "Concentrated - 1", load_case=25, magnitude=-450.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.5)
load_cases[25].member_loads.create_force(15, "438,440", "Concentrated - 1", load_case=25, magnitude=-500.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.5)
load_cases[26].member_loads.create_force(9, "108", "Concentrated - 1", load_case=26, load_direction="X_L (U_L )", magnitude=-600.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.5)
load_cases[26].member_loads.create_force(10, "108", "Concentrated - 1", load_case=26, magnitude=-16500.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.5)

# Create Member Loads - Distributed
load_cases[2].member_loads.create_force(97, "9,10,111,112,343,350,585,589", "Trapezoidal", load_case=2, load_direction="Z_L (W_L )", magnitude_1=-200.0, magnitude_2=-200.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(98, "11,12,113,114,351,352,579,580", "Trapezoidal", load_case=2, load_direction="Z_L (W_L )", magnitude_1=-517.5, magnitude_2=-517.5, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(99, "13,14,383,510,566,567,568,569,570,571,572,573,578", "Trapezoidal", load_case=2, load_direction="Z_L (W_L )", magnitude_1=-497.5, magnitude_2=-497.5, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(100, "15,16,115,116,118,234,280,290,334,335,339,340,348,349,353,363", "Trapezoidal", load_case=2, load_direction="Z_L (W_L )", magnitude_1=-180.0, magnitude_2=-180.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(101, "17,27,34,305,361", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-200.0, magnitude_2=-200.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(102, "24,28,35,294,323", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-454.0, magnitude_2=-454.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(103, "25,29,36,310,333", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-494.0, magnitude_2=-494.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(104, "26,30,37,244,312", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-240.0, magnitude_2=-240.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(105, "44,45,46,47,48,49,50,51,52,320", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-400.0, magnitude_2=-400.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(106, "55,56,57,58,59,60,311", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-480.0, magnitude_2=-480.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(107, "70,71,72,73,74,75,76,77,78,79,80,81,296,299,302,308", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-508.00003, magnitude_2=-508.00003, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(108, "128,138,198,201,202,240,242,251,338,345,467,501,549", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-300.0, magnitude_2=-300.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(109, "129,146,148,376,377", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-175.0, magnitude_2=-175.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(110, "146,368,377,489", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-192.5, magnitude_2=-192.5, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(111, "153,156,380,488", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-385.0, magnitude_2=-385.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(112, "158,192,194,372,375,379,381,462,465,472", "Trapezoidal", load_case=2, load_direction="Z_L (W_L )", magnitude_1=-150.0, magnitude_2=-150.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(113, "159,161,439,450,458,459,460,461", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-350.0, magnitude_2=-350.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(114, "214,216,415,432,434,479,487", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-472.5, magnitude_2=-472.5, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(115, "215,217,256,257,258,259,413,424,431,435,446,456,480,481", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-404.25, magnitude_2=-404.25, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(116, "219,421,492", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-245.0, magnitude_2=-245.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(117, "260,276,277,430,447,468,482", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-470.75, magnitude_2=-470.75, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(118, "283,337,395,423", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-243.25, magnitude_2=-243.25, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(119, "364,506,507", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-125.6579, magnitude_2=-125.6579, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[2].member_loads.create_force(120, "370", "Trapezoidal", load_case=2, load_direction="Z_P (W_P )", magnitude_1=-210.0, magnitude_2=-210.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(69, "17,27,34,129,148,159,161,305,361,376", "Trapezoidal", load_case=11, load_direction="Z_P (W_P )", magnitude_1=-2500.0, magnitude_2=-2500.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(70, "24,28,35,294,323", "Trapezoidal", load_case=11, load_direction="Z_P (W_P )", magnitude_1=-5675.0, magnitude_2=-5675.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(71, "25,29,36,310,333", "Trapezoidal", load_case=11, load_direction="Z_P (W_P )", magnitude_1=-6175.0, magnitude_2=-6175.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(72, "26,30,37,244,312,370", "Trapezoidal", load_case=11, load_direction="Z_P (W_P )", magnitude_1=-3000.0, magnitude_2=-3000.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(73, "44,45,46,47,48,49,50,51,52,320", "Trapezoidal", load_case=11, load_direction="Z_P (W_P )", magnitude_1=-5000.0, magnitude_2=-5000.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(74, "55,56,57,58,59,60,311", "Trapezoidal", load_case=11, load_direction="Z_P (W_P )", magnitude_1=-6000.0, magnitude_2=-6000.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(75, "70,71,72,73,74,75,76,77,78,79,80,81,296,299,302,308", "Trapezoidal", load_case=11, load_direction="Z_P (W_P )", magnitude_1=-6350.0, magnitude_2=-6350.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(76, "128,138,198,201,202,240,242,251,338,345,467,501,549", "Trapezoidal", load_case=11, load_direction="Z_P (W_P )", magnitude_1=-1500.0, magnitude_2=-1500.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(77, "146,148,376,377", "Trapezoidal", load_case=11, load_direction="Z_P (W_P )", magnitude_1=-1250.0, magnitude_2=-1250.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(78, "146,368,377,489", "Trapezoidal", load_case=11, load_direction="Z_P (W_P )", magnitude_1=-2750.0, magnitude_2=-2750.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(79, "153,156,380,488", "Trapezoidal", load_case=11, load_direction="Z_P (W_P )", magnitude_1=-5500.0, magnitude_2=-5500.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(80, "214,216,219,415,421,432,434,479,487,492", "Trapezoidal", load_case=11, load_direction="Z_P (W_P )", magnitude_1=-1750.0, magnitude_2=-1750.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(81, "215,217,256,257,258,259,413,424,431,435,446,456,480,481", "Trapezoidal", load_case=11, load_direction="Z_P (W_P )", magnitude_1=-1262.5, magnitude_2=-1262.5, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(82, "260,276,277,283,337,423,430,447,468,482", "Trapezoidal", load_case=11, load_direction="Z_P (W_P )", magnitude_1=-1737.5, magnitude_2=-1737.5, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(83, "364,506,507", "Trapezoidal", load_case=11, load_direction="Z_P (W_P )", magnitude_1=-1375.0, magnitude_2=-1375.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(84, "450,458,460,461", "Trapezoidal", load_case=11, load_direction="Y_P (V_P )", magnitude_1=-1000.0, magnitude_2=-1000.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[11].member_loads.create_force(85, "479,480,481,482", "Trapezoidal", load_case=11, load_direction="Z_P (W_P )", magnitude_1=-1625.0, magnitude_2=-1625.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[12].member_loads.create_force(30, "332", "Trapezoidal", load_case=12, load_direction="Z_P (W_P )", magnitude_1=-5100.0, magnitude_2=-5100.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[12].member_loads.create_force(31, "398", "Trapezoidal", load_case=12, load_direction="Z_P (W_P )", magnitude_1=-3272.5, magnitude_2=-3272.5, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[12].member_loads.create_force(32, "398", "Trapezoidal", load_case=12, load_direction="Z_P (W_P )", magnitude_1=-10200.0, magnitude_2=-10200.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[12].member_loads.create_force(33, "410", "Trapezoidal", load_case=12, load_direction="Z_P (W_P )", magnitude_1=-3153.5, magnitude_2=-3153.5, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[12].member_loads.create_force(34, "411", "Trapezoidal", load_case=12, load_direction="Z_P (W_P )", magnitude_1=-5440.0, magnitude_2=-5440.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[12].member_loads.create_force(35, "412", "Trapezoidal", load_case=12, load_direction="Z_P (W_P )", magnitude_1=-3391.5, magnitude_2=-3391.5, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(85, "1,2,3,4,5,6,7,8,9,10,11,12,13,14,123,125,132,133,134,220,221,223,224,225,229,231,355,383,414,452,466,493,510,544,545,572,573,578,579,580,585,589", "Trapezoidal", load_case=31, load_direction="X_L (U_L )", magnitude_1=1100.0, magnitude_2=1100.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(86, "9,10,585,589", "Trapezoidal", load_case=31, coordinate_system="Local", load_direction="y", magnitude_1=1980.0, magnitude_2=1980.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(87, "11,12,13,14,383,510,572,573,578,579,580", "Trapezoidal", load_case=31, coordinate_system="Local", load_direction="y", magnitude_1=4565.0, magnitude_2=4565.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(88, "15,16,234,363", "Trapezoidal", load_case=31, load_direction="X_L (U_L )", magnitude_1=7392.0, magnitude_2=7392.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(89, "15,16,234,363", "Trapezoidal", load_case=31, coordinate_system="Local", load_direction="y", magnitude_1=2090.0, magnitude_2=2090.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(90, "24,25,28,29,35,36,294,310,323,333", "Trapezoidal", load_case=31, load_direction="X_L (U_L )", magnitude_1=2332.0, magnitude_2=2332.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(91, "44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,70,71,72,73,74,75,76,77,78,79,80,81,296,299,302,308,311,320", "Trapezoidal", load_case=31, load_direction="X_L (U_L )", magnitude_1=176.0, magnitude_2=176.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(92, "111,112,113,114,115,116,118,280,290,334,335,339,340,343,348,349,350,351,352,353,566,567,568,569,570,571", "Trapezoidal", load_case=31, load_direction="X_L (U_L )", magnitude_1=1364.0, magnitude_2=1364.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(93, "111,112,343,350", "Trapezoidal", load_case=31, coordinate_system="Local", load_direction="y", magnitude_1=3190.0, magnitude_2=3190.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(94, "113,114,351,352", "Trapezoidal", load_case=31, coordinate_system="Local", load_direction="y", magnitude_1=7700.0, magnitude_2=7700.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(95, "115,116,118,280,290,334,335,339,340,348,349,353", "Trapezoidal", load_case=31, coordinate_system="Local", load_direction="y", magnitude_1=2420.0, magnitude_2=2420.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(96, "182,190,212,213", "Trapezoidal", load_case=31, load_direction="X_L (U_L )", magnitude_1=4840.0, magnitude_2=4840.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(97, "218,250,278,279,287,366,388,390,392", "Trapezoidal", load_case=31, load_direction="Y_L (V_L )", magnitude_1=200.0, magnitude_2=200.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(98, "254,255,288,289,330,332,398,504,511", "Trapezoidal", load_case=31, load_direction="X_L (U_L )", magnitude_1=500.0, magnitude_2=500.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(99, "291,292,328,329,331,397,399,401,402,403,404,405,406,441,484", "Trapezoidal", load_case=31, load_direction="X_L (U_L )", magnitude_1=1800.0, magnitude_2=1800.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(100, "309,315,317,322,425,426,427,428,455,483,490,491,495,496,499,500,563,564,586,587", "Trapezoidal", load_case=31, load_direction="X_L (U_L )", magnitude_1=352.0, magnitude_2=352.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(101, "416,417,418,419,420,422", "Trapezoidal", load_case=31, load_direction="X_L (U_L )", magnitude_1=390.0, magnitude_2=390.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(102, "450,458", "Trapezoidal", load_case=31, load_direction="X_P (U_P )", magnitude_1=858.0, magnitude_2=858.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(103, "457,469,470", "Trapezoidal", load_case=31, load_direction="X_P (U_P )", magnitude_1=960.0, magnitude_2=960.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(104, "485,486,497,498,561,562,565,588", "Trapezoidal", load_case=31, load_direction="X_L (U_L )", magnitude_1=980.0, magnitude_2=980.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[31].member_loads.create_force(105, "566,567,568,569,570,571", "Trapezoidal", load_case=31, coordinate_system="Local", load_direction="y", magnitude_1=5896.0, magnitude_2=5896.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(81, "1,2,3,4,5,6,7,8,9,10,11,12,13,14,123,125,132,133,134,220,221,223,224,225,229,231,355,383,414,452,466,493,510,544,545,572,573,578,579,580,585,589", "Trapezoidal", load_case=33, load_direction="X_L (U_L )", magnitude_1=1100.0, magnitude_2=1100.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(82, "9,10,15,16,234,363,585,589", "Trapezoidal", load_case=33, coordinate_system="Local", load_direction="y", magnitude_1=1980.0, magnitude_2=1980.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(83, "11,12,13,14,383,510,572,573,578,579,580", "Trapezoidal", load_case=33, coordinate_system="Local", load_direction="y", magnitude_1=4565.0, magnitude_2=4565.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(84, "15,16,234,363", "Trapezoidal", load_case=33, load_direction="X_L (U_L )", magnitude_1=7084.0, magnitude_2=7084.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(85, "24,25,28,29,35,36,294,310,323,333", "Trapezoidal", load_case=33, load_direction="X_L (U_L )", magnitude_1=2332.0, magnitude_2=2332.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(86, "44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,70,71,72,73,74,75,76,77,78,79,80,81,296,299,302,308,311,320", "Trapezoidal", load_case=33, load_direction="X_L (U_L )", magnitude_1=176.0, magnitude_2=176.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(87, "111,112,113,114,115,116,118,280,290,334,335,339,340,343,348,349,350,351,352,353,566,567,568,569,570,571", "Trapezoidal", load_case=33, load_direction="X_L (U_L )", magnitude_1=1364.0, magnitude_2=1364.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(88, "111,112,343,350", "Trapezoidal", load_case=33, coordinate_system="Local", load_direction="y", magnitude_1=1496.0, magnitude_2=1496.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(89, "113,114,351,352", "Trapezoidal", load_case=33, coordinate_system="Local", load_direction="y", magnitude_1=3520.0, magnitude_2=3520.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(90, "115,116,118,280,290,334,335,339,340,348,349,353", "Trapezoidal", load_case=33, coordinate_system="Local", load_direction="y", magnitude_1=1056.0, magnitude_2=1056.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(91, "182,190,212,213", "Trapezoidal", load_case=33, load_direction="X_L (U_L )", magnitude_1=4840.0, magnitude_2=4840.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(92, "218,250,278,279,287,366,388,390,392", "Trapezoidal", load_case=33, load_direction="Y_L (V_L )", magnitude_1=200.0, magnitude_2=200.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(93, "254,255,288,289,330,332,398,504,511", "Trapezoidal", load_case=33, load_direction="X_L (U_L )", magnitude_1=500.0, magnitude_2=500.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(94, "291,292,328,329,331,397,399,401,402,403,404,405,406,441,484", "Trapezoidal", load_case=33, load_direction="X_L (U_L )", magnitude_1=1800.0, magnitude_2=1800.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(95, "309,315,317,322,425,426,427,428,455,483,490,491,495,496,499,500,563,564,586,587", "Trapezoidal", load_case=33, load_direction="X_L (U_L )", magnitude_1=352.0, magnitude_2=352.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(96, "416,417,418,419,420,422", "Trapezoidal", load_case=33, load_direction="X_L (U_L )", magnitude_1=390.0, magnitude_2=390.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(97, "450,458", "Trapezoidal", load_case=33, load_direction="X_P (U_P )", magnitude_1=858.0, magnitude_2=858.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(98, "457,469,470", "Trapezoidal", load_case=33, load_direction="X_P (U_P )", magnitude_1=960.0, magnitude_2=960.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(99, "485,486,497,498,561,562,565,588", "Trapezoidal", load_case=33, load_direction="X_L (U_L )", magnitude_1=980.0, magnitude_2=980.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[33].member_loads.create_force(100, "566,567,568,569,570,571", "Trapezoidal", load_case=33, coordinate_system="Local", load_direction="y", magnitude_1=2585.0, magnitude_2=2585.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[34].member_loads.create_force(9, "9,10,15,16,111,112,115,116,118,123,125,234,280,290,334,335,339,340,343,348,349,350,353,363,585,589", "Trapezoidal", load_case=34, coordinate_system="Local", load_direction="y", magnitude_1=-1133.0, magnitude_2=-1133.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[34].member_loads.create_force(10, "11,12,13,14,113,114,351,352,383,510,566,567,568,569,570,571,572,573,578,579,580", "Trapezoidal", load_case=34, coordinate_system="Local", load_direction="y", magnitude_1=-2937.0, magnitude_2=-2937.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(73, "1,2,3,4,5,6,7,8,132,133,134,220,221,223,224,225,229,231,355,414,452,466,493,544,545", "Trapezoidal", load_case=35, load_direction="Y_L (V_L )", magnitude_1=1100.0, magnitude_2=1100.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(74, "9,15,16,234,363,585", "Trapezoidal", load_case=35, load_direction="Y_L (V_L )", magnitude_1=2090.0, magnitude_2=2090.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(75, "10,589", "Trapezoidal", load_case=35, load_direction="Y_L (V_L )", magnitude_1=1683.0, magnitude_2=1683.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(76, "11,13,383,510,573,580", "Trapezoidal", load_case=35, load_direction="Y_L (V_L )", magnitude_1=5170.0, magnitude_2=5170.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(77, "12,14,572,578,579", "Trapezoidal", load_case=35, load_direction="Y_L (V_L )", magnitude_1=3905.0, magnitude_2=3905.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(78, "15,16,234,363", "Trapezoidal", load_case=35, load_direction="X_L (U_L )", magnitude_1=3014.0, magnitude_2=3014.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(79, "111,112,115,116,118,280,290,334,335,339,343,348,349", "Trapezoidal", load_case=35, coordinate_system="Local", load_direction="y", magnitude_1=3850.0, magnitude_2=3850.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(80, "113,114,351,566,567,569,570,571", "Trapezoidal", load_case=35, coordinate_system="Local", load_direction="y", magnitude_1=9020.0, magnitude_2=9020.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(81, "182,190,212,213", "Trapezoidal", load_case=35, load_direction="Y_L (V_L )", magnitude_1=2420.0, magnitude_2=2420.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(82, "214,215,216,217,256,257,258,259,260,276,277,413,415,424,430,431,432,456,468,479,480,481,482,487", "Trapezoidal", load_case=35, load_direction="Y_L (V_L )", magnitude_1=720.0, magnitude_2=720.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(83, "219,230,232,283,337,394,395,410,412,421,423,492,532,537", "Trapezoidal", load_case=35, load_direction="Y_L (V_L )", magnitude_1=980.0, magnitude_2=980.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(84, "241,243", "Trapezoidal", load_case=35, load_direction="Y_L (V_L )", magnitude_1=352.0, magnitude_2=352.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(85, "340,350,353", "Trapezoidal", load_case=35, coordinate_system="Local", load_direction="y", magnitude_1=2079.0, magnitude_2=2079.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(86, "352,568", "Trapezoidal", load_case=35, coordinate_system="Local", load_direction="y", magnitude_1=4862.0, magnitude_2=4862.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(87, "416,417,419,422", "Trapezoidal", load_case=35, load_direction="Y_L (V_L )", magnitude_1=390.0, magnitude_2=390.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(88, "429,434,435,446,447", "Trapezoidal", load_case=35, load_direction="Y_L (V_L )", magnitude_1=200.0, magnitude_2=200.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(89, "450,458,460,461", "Trapezoidal", load_case=35, load_direction="Y_L (V_L )", magnitude_1=858.0, magnitude_2=858.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[35].member_loads.create_force(90, "457,469,470", "Trapezoidal", load_case=35, load_direction="Y_P (V_P )", magnitude_1=960.0, magnitude_2=960.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[37].member_loads.create_force(41, "111,112,115,116,118,280,290,334,335,339,343,348,349", "Trapezoidal", load_case=37, coordinate_system="Local", load_direction="y", magnitude_1=1782.0, magnitude_2=1782.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[37].member_loads.create_force(42, "113,114,351,566,567,569,570,571", "Trapezoidal", load_case=37, coordinate_system="Local", load_direction="y", magnitude_1=4180.0, magnitude_2=4180.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[37].member_loads.create_force(43, "182,190,212,213", "Trapezoidal", load_case=37, load_direction="Y_L (V_L )", magnitude_1=2420.0, magnitude_2=2420.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[37].member_loads.create_force(44, "214,215,216,217,256,257,258,259,260,276,277,413,415,424,430,431,432,456,468,479,480,481,482,487", "Trapezoidal", load_case=37, load_direction="Y_L (V_L )", magnitude_1=720.0, magnitude_2=720.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[37].member_loads.create_force(45, "219,230,232,283,337,394,395,410,412,421,423,492,532,537", "Trapezoidal", load_case=37, load_direction="Y_L (V_L )", magnitude_1=980.0, magnitude_2=980.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[37].member_loads.create_force(46, "340,350,353", "Trapezoidal", load_case=37, coordinate_system="Local", load_direction="y", magnitude_1=891.0, magnitude_2=891.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[37].member_loads.create_force(47, "352,568", "Trapezoidal", load_case=37, coordinate_system="Local", load_direction="y", magnitude_1=2079.0, magnitude_2=2079.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[37].member_loads.create_force(48, "416,417,419,422", "Trapezoidal", load_case=37, load_direction="Y_L (V_L )", magnitude_1=390.0, magnitude_2=390.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[37].member_loads.create_force(49, "429,434,435,446,447", "Trapezoidal", load_case=37, load_direction="Y_L (V_L )", magnitude_1=200.0, magnitude_2=200.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[37].member_loads.create_force(50, "457,469,470", "Trapezoidal", load_case=37, load_direction="Y_P (V_P )", magnitude_1=960.0, magnitude_2=960.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[38].member_loads.create_force(9, "9,10,15,16,111,112,115,116,118,123,125,234,280,290,334,335,339,340,343,348,349,350,353,363,585,589", "Trapezoidal", load_case=38, coordinate_system="Local", load_direction="y", magnitude_1=-1133.0, magnitude_2=-1133.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[38].member_loads.create_force(10, "11,12,13,14,113,114,351,352,383,510,566,567,568,569,570,571,572,573,578,579,580", "Trapezoidal", load_case=38, coordinate_system="Local", load_direction="y", magnitude_1=-2937.0, magnitude_2=-2937.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(73, "1,2,3,4,5,6,7,8,123,125,132,133,134,220,221,223,224,225,229,231,355,414,452,466,493,544,545", "Trapezoidal", load_case=39, load_direction="X_L (U_L )", magnitude_1=-1100.0, magnitude_2=-1100.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(74, "9,10,15,16,234,363,585,589", "Trapezoidal", load_case=39, coordinate_system="Local", load_direction="y", magnitude_1=2090.0, magnitude_2=2090.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(75, "11,12,13,14,383,510,572,573,578,579,580", "Trapezoidal", load_case=39, coordinate_system="Local", load_direction="y", magnitude_1=4752.0, magnitude_2=4752.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(76, "15,16,234,363", "Trapezoidal", load_case=39, load_direction="X_L (U_L )", magnitude_1=-7392.0, magnitude_2=-7392.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(77, "111,112,343,350", "Trapezoidal", load_case=39, coordinate_system="Local", load_direction="y", magnitude_1=2530.0, magnitude_2=2530.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(78, "113,114,351,352", "Trapezoidal", load_case=39, coordinate_system="Local", load_direction="y", magnitude_1=5940.0, magnitude_2=5940.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(79, "115,116,118,280,290,334,335,339,340,348,349,353", "Trapezoidal", load_case=39, coordinate_system="Local", load_direction="y", magnitude_1=3190.0, magnitude_2=3190.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(80, "182,190,212,213", "Trapezoidal", load_case=39, load_direction="X_L (U_L )", magnitude_1=-4840.0, magnitude_2=-4840.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(81, "218,250,278,279,287,366,388,390,392", "Trapezoidal", load_case=39, load_direction="Y_L (V_L )", magnitude_1=-200.0, magnitude_2=-200.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(82, "254,330,332,398", "Trapezoidal", load_case=39, load_direction="X_L (U_L )", magnitude_1=-500.0, magnitude_2=-500.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(83, "255,288,289,504,511", "Trapezoidal", load_case=39, load_direction="X_P (U_P )", magnitude_1=-500.0, magnitude_2=-500.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(84, "291,292,328,329,331,397,399,401,402,403,404,405,406,441,484", "Trapezoidal", load_case=39, load_direction="X_L (U_L )", magnitude_1=-1800.0, magnitude_2=-1800.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(85, "309,315,317,322,425,426,427,428,455,483,490,491,495,496,499,500,563,564,586,587", "Trapezoidal", load_case=39, load_direction="X_L (U_L )", magnitude_1=-352.0, magnitude_2=-352.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(86, "416,417,418,419,420,422", "Trapezoidal", load_case=39, load_direction="X_L (U_L )", magnitude_1=-390.0, magnitude_2=-390.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(87, "439,450,458,459", "Trapezoidal", load_case=39, load_direction="X_P (U_P )", magnitude_1=-858.0, magnitude_2=-858.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(88, "457,470", "Trapezoidal", load_case=39, load_direction="X_P (U_P )", magnitude_1=-960.0, magnitude_2=-960.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(89, "485,486,497,498,561,562,565,588", "Trapezoidal", load_case=39, load_direction="X_L (U_L )", magnitude_1=-980.0, magnitude_2=-980.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[39].member_loads.create_force(90, "566,567,568,569,570,571", "Trapezoidal", load_case=39, coordinate_system="Local", load_direction="y", magnitude_1=7700.0, magnitude_2=7700.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(73, "1,2,3,4,5,6,7,8,123,125,132,133,134,220,221,223,224,225,229,231,355,414,452,466,493,544,545", "Trapezoidal", load_case=41, load_direction="X_L (U_L )", magnitude_1=-1100.0, magnitude_2=-1100.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(74, "9,10,15,16,234,363,585,589", "Trapezoidal", load_case=41, coordinate_system="Local", load_direction="y", magnitude_1=2090.0, magnitude_2=2090.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(75, "11,12,13,14,383,510,572,573,578,579,580", "Trapezoidal", load_case=41, coordinate_system="Local", load_direction="y", magnitude_1=4752.0, magnitude_2=4752.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(76, "15,16,234,363", "Trapezoidal", load_case=41, load_direction="X_L (U_L )", magnitude_1=-7392.0, magnitude_2=-7392.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(77, "111,112,343,350", "Trapezoidal", load_case=41, coordinate_system="Local", load_direction="y", magnitude_1=2530.0, magnitude_2=2530.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(78, "113,114,351,352", "Trapezoidal", load_case=41, coordinate_system="Local", load_direction="y", magnitude_1=5940.0, magnitude_2=5940.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(79, "115,116,118,280,290,334,335,339,340,348,349,353", "Trapezoidal", load_case=41, coordinate_system="Local", load_direction="y", magnitude_1=3190.0, magnitude_2=3190.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(80, "182,190,212,213", "Trapezoidal", load_case=41, load_direction="X_L (U_L )", magnitude_1=-4840.0, magnitude_2=-4840.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(81, "218,250,278,279,287,366,388,390,392", "Trapezoidal", load_case=41, load_direction="Y_L (V_L )", magnitude_1=-200.0, magnitude_2=-200.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(82, "254,330,332,398", "Trapezoidal", load_case=41, load_direction="X_L (U_L )", magnitude_1=-500.0, magnitude_2=-500.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(83, "255,288,289,504,511", "Trapezoidal", load_case=41, load_direction="X_P (U_P )", magnitude_1=-500.0, magnitude_2=-500.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(84, "291,292,328,329,331,397,399,401,402,403,404,405,406,441,484", "Trapezoidal", load_case=41, load_direction="X_L (U_L )", magnitude_1=-1800.0, magnitude_2=-1800.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(85, "309,315,317,322,425,426,427,428,455,483,490,491,495,496,499,500,563,564,586,587", "Trapezoidal", load_case=41, load_direction="X_L (U_L )", magnitude_1=-352.0, magnitude_2=-352.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(86, "416,417,418,419,420,422", "Trapezoidal", load_case=41, load_direction="X_L (U_L )", magnitude_1=-390.0, magnitude_2=-390.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(87, "439,450,458,459", "Trapezoidal", load_case=41, load_direction="X_P (U_P )", magnitude_1=-858.0, magnitude_2=-858.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(88, "457,470", "Trapezoidal", load_case=41, load_direction="X_P (U_P )", magnitude_1=-960.0, magnitude_2=-960.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(89, "485,486,497,498,561,562,565,588", "Trapezoidal", load_case=41, load_direction="X_L (U_L )", magnitude_1=-980.0, magnitude_2=-980.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[41].member_loads.create_force(90, "566,567,568,569,570,571", "Trapezoidal", load_case=41, coordinate_system="Local", load_direction="y", magnitude_1=7700.0, magnitude_2=7700.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[42].member_loads.create_force(9, "9,10,15,16,111,112,115,116,118,123,125,234,280,290,334,335,339,340,343,348,349,350,353,363,585,589", "Trapezoidal", load_case=42, coordinate_system="Local", load_direction="y", magnitude_1=-1133.0, magnitude_2=-1133.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[42].member_loads.create_force(10, "11,12,13,14,113,114,351,352,383,510,566,567,568,569,570,571,572,573,578,579,580", "Trapezoidal", load_case=42, coordinate_system="Local", load_direction="y", magnitude_1=-2937.0, magnitude_2=-2937.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(89, "1,2,3,4,5,6,7,8,132,133,134,220,221,223,224,225,229,231,355,414,452,466,493,544,545", "Trapezoidal", load_case=43, load_direction="Y_L (V_L )", magnitude_1=-1100.0, magnitude_2=-1100.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(90, "9", "Trapezoidal", load_case=43, load_direction="Y_L (V_L )", magnitude_1=-1518.0, magnitude_2=-1507.583, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(91, "10,16,363,589", "Trapezoidal", load_case=43, load_direction="Y_L (V_L )", magnitude_1=-2090.0, magnitude_2=-2090.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(92, "11,13,383,510,573,580", "Trapezoidal", load_case=43, load_direction="Y_L (V_L )", magnitude_1=-3905.0, magnitude_2=-3905.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(93, "12,14,572,578,579", "Trapezoidal", load_case=43, load_direction="Y_L (V_L )", magnitude_1=-5170.0, magnitude_2=-5170.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(94, "15", "Trapezoidal", load_case=43, load_direction="Y_L (V_L )", magnitude_1=-1518.0, magnitude_2=-1512.5, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(95, "15,16,234,363", "Trapezoidal", load_case=43, load_direction="X_L (U_L )", magnitude_1=3014.0, magnitude_2=3014.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(96, "111,118,334", "Trapezoidal", load_case=43, coordinate_system="Local", load_direction="y", magnitude_1=2079.0, magnitude_2=2079.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(97, "112,115,116,280,290,335,339,340,343,348,349,350,353", "Trapezoidal", load_case=43, coordinate_system="Local", load_direction="y", magnitude_1=3850.0, magnitude_2=3850.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(98, "113,351,352,566,567,568,569,570", "Trapezoidal", load_case=43, coordinate_system="Local", load_direction="y", magnitude_1=9020.0, magnitude_2=9020.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(99, "114,571", "Trapezoidal", load_case=43, coordinate_system="Local", load_direction="y", magnitude_1=4862.0, magnitude_2=4862.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(100, "182,190,212,213", "Trapezoidal", load_case=43, load_direction="Y_L (V_L )", magnitude_1=-2420.0, magnitude_2=-2420.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(101, "214,215,216,217,256,257,258,259,260,276,277,413,415,424,430,431,432,456,468,479,480,481,482,487", "Trapezoidal", load_case=43, load_direction="Y_L (V_L )", magnitude_1=-720.0, magnitude_2=-720.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(102, "219,230,232,283,337,394,395,410,412,421,423,492,532,537", "Trapezoidal", load_case=43, load_direction="Y_L (V_L )", magnitude_1=-980.0, magnitude_2=-980.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(103, "234", "Trapezoidal", load_case=43, load_direction="Y_L (V_L )", magnitude_1=-1512.5, magnitude_2=-1508.69, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(104, "241,243", "Trapezoidal", load_case=43, load_direction="Y_L (V_L )", magnitude_1=-352.0, magnitude_2=-352.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(105, "416,417,419,422", "Trapezoidal", load_case=43, load_direction="Y_L (V_L )", magnitude_1=-390.0, magnitude_2=-390.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(106, "429,434,435,446,447", "Trapezoidal", load_case=43, load_direction="Y_L (V_L )", magnitude_1=-200.0, magnitude_2=-200.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(107, "439,459", "Trapezoidal", load_case=43, load_direction="Y_P (V_P )", magnitude_1=-858.0, magnitude_2=-858.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(108, "450,458,460,461", "Trapezoidal", load_case=43, load_direction="Y_L (V_L )", magnitude_1=-858.0, magnitude_2=-858.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(109, "457,470", "Trapezoidal", load_case=43, load_direction="Y_P (V_P )", magnitude_1=-960.0, magnitude_2=-960.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[43].member_loads.create_force(110, "585", "Trapezoidal", load_case=43, load_direction="Y_L (V_L )", magnitude_1=-1507.583, magnitude_2=-1507.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(85, "1,2,3,4,5,6,7,8,132,133,134,220,221,223,224,225,229,231,355,414,452,466,493,544,545", "Trapezoidal", load_case=45, load_direction="Y_L (V_L )", magnitude_1=-1100.0, magnitude_2=-1100.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(86, "9", "Trapezoidal", load_case=45, load_direction="Y_L (V_L )", magnitude_1=-1518.0, magnitude_2=-1507.583, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(87, "10,16,363,589", "Trapezoidal", load_case=45, load_direction="Y_L (V_L )", magnitude_1=-2090.0, magnitude_2=-2090.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(88, "11,13,383,510,573,580", "Trapezoidal", load_case=45, load_direction="Y_L (V_L )", magnitude_1=-3905.0, magnitude_2=-3905.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(89, "12,14,572,578,579", "Trapezoidal", load_case=45, load_direction="Y_L (V_L )", magnitude_1=-5170.0, magnitude_2=-5170.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(90, "15", "Trapezoidal", load_case=45, load_direction="Y_L (V_L )", magnitude_1=-1518.0, magnitude_2=-1512.5, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(91, "111,118,334", "Trapezoidal", load_case=45, coordinate_system="Local", load_direction="y", magnitude_1=891.0, magnitude_2=891.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(92, "112,115,116,280,290,335,339,340,343,348,349,350,353", "Trapezoidal", load_case=45, coordinate_system="Local", load_direction="y", magnitude_1=1782.0, magnitude_2=1782.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(93, "113,351,352,566,567,568,569,570", "Trapezoidal", load_case=45, coordinate_system="Local", load_direction="y", magnitude_1=4180.0, magnitude_2=4180.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(94, "114,571", "Trapezoidal", load_case=45, coordinate_system="Local", load_direction="y", magnitude_1=2079.0, magnitude_2=2079.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(95, "182,190,212,213", "Trapezoidal", load_case=45, load_direction="Y_L (V_L )", magnitude_1=-2420.0, magnitude_2=-2420.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(96, "214,215,216,217,256,257,258,259,260,276,277,413,415,424,430,431,432,456,468,479,480,481,482,487", "Trapezoidal", load_case=45, load_direction="Y_L (V_L )", magnitude_1=-720.0, magnitude_2=-720.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(97, "219,230,232,283,337,394,395,410,412,421,423,492,532,537", "Trapezoidal", load_case=45, load_direction="Y_L (V_L )", magnitude_1=-980.0, magnitude_2=-980.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(98, "234", "Trapezoidal", load_case=45, load_direction="Y_L (V_L )", magnitude_1=-1512.5, magnitude_2=-1508.69, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(99, "241,243", "Trapezoidal", load_case=45, load_direction="Y_L (V_L )", magnitude_1=-352.0, magnitude_2=-352.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(100, "416,417,419,422", "Trapezoidal", load_case=45, load_direction="Y_L (V_L )", magnitude_1=-390.0, magnitude_2=-390.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(101, "429,434,435,446,447", "Trapezoidal", load_case=45, load_direction="Y_L (V_L )", magnitude_1=-200.0, magnitude_2=-200.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(102, "439,459", "Trapezoidal", load_case=45, load_direction="Y_P (V_P )", magnitude_1=-858.0, magnitude_2=-858.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(103, "450,458,460,461", "Trapezoidal", load_case=45, load_direction="Y_L (V_L )", magnitude_1=-858.0, magnitude_2=-858.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(104, "457,470", "Trapezoidal", load_case=45, load_direction="Y_P (V_P )", magnitude_1=-960.0, magnitude_2=-960.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[45].member_loads.create_force(105, "585", "Trapezoidal", load_case=45, load_direction="Y_L (V_L )", magnitude_1=-1507.583, magnitude_2=-1507.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[46].member_loads.create_force(9, "9,10,15,16,111,112,115,116,118,123,125,234,280,290,334,335,339,340,343,348,349,350,353,363,585,589", "Trapezoidal", load_case=46, coordinate_system="Local", load_direction="y", magnitude_1=-1133.0, magnitude_2=-1133.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)
load_cases[46].member_loads.create_force(10, "11,12,13,14,113,114,351,352,383,510,566,567,568,569,570,571,572,573,578,579,580", "Trapezoidal", load_case=46, coordinate_system="Local", load_direction="y", magnitude_1=-2937.0, magnitude_2=-2937.0, distance_a_is_defined_as_relative=True, distance_a_relative=0.0, distance_b_is_defined_as_relative=True, distance_b_relative=1.0)

