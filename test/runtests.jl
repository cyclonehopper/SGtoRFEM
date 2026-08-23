using Test
using SGtoRFEM
using XML

@testset "SGtoRFEM" begin
    sg = parse_sg_file(joinpath(@__DIR__, "..", "sg_txt_out", "sg_export.TXT"))

    @testset "parser" begin
        @test length(sg.nodes) == 14
        @test length(sg.members) == 21
        @test length(sg.sections) == 5
        @test !isempty(sg.nodal_loads)
        # dims picked up from the section continuation rows
        s1 = sg.sections[1]   # 200 UC 46.2
        @test s1.depth ≈ 203.0
        @test s1.flange_width ≈ 203.0
        @test s1.thickness_web ≈ 7.3
        @test s1.thickness_flange ≈ 11.0
    end

    rf = convert_to_rfem(sg)

    @testset "converter" begin
        @test length(rf.members_data) == 21
        @test length(rf.lines) == 21
        @test length(rf.cross_sections) == 5
        # all materials are steel and at least one exists
        @test all(m.type == "STEEL" for (_, m) in rf.materials)
        @test haskey(rf.materials, 1)
        # shapes recognised from descriptions / row-2 dims
        @test rf.cross_sections[2].shape == "CHS"   # 219.1x6.4 CHS
        @test rf.cross_sections[5].shape == "SHS"   # 89*5 SHS
        @test rf.cross_sections[3].shape == "I"     # 310 UB 40.4
        @test rf.cross_sections[3].depth ≈ 0.304
    end

    @testset "titles and combinations" begin
        txt = """
        SPACE GASS Text File - Version 900
        NODES
        1,0.0,0.0,0.0
        2,0.0,0.0,6.0
        MEMBERS
        1,0.000000,0, ,N,1,2,1,1,FFFFFF,FFFFFF
        SECTIONS
        1,"310 UB 40.4","Aust300","S3",5210.0,157000.0,7650000.0,86400000.0,0,0,0,1,1,1,1,1
        MATERIALS
        1,"STEEL","METRIC",200000.0,0.25,7.85,1.17E-5,350.0
        COMBINATIONS
        10,1,1.25
        10,2,1.50
        11,1,0.80
        TITLES
        1,Dead load (DL)
        2,"Live load (LL)"
        10,1.25DL+1.5LL
        """
        path = joinpath(tempdir(), "sgtoRFEM_mini.TXT")
        write(path, txt)
        sg2 = parse_sg_file(path)
        @test sg2.load_titles[1] == "Dead load (DL)"
        @test sg2.load_titles[2] == "Live load (LL)"
        @test length(sg2.combinations) == 3
        rf2 = convert_to_rfem(sg2)
        # LC referenced only by the combination must still exist
        @test [c.id for c in rf2.cases] == [1, 2]
        @test rf2.cases[1].name == "Dead load (DL)"
        @test length(rf2.combinations) == 2
        @test rf2.combinations[1].items == [(1, 1.25), (2, 1.5)]
        out = joinpath(tempdir(), "sgtoRFEM_combo.xml")
        generate_rfem_xml(rf2, out)
        doc = open(f -> read(f, XML.Node), out)   # well-formed check
        rm(out); rm(path)
    end

    @testset "writer" begin
        out = joinpath(tempdir(), "sgtoRFEM_test_export.xml")
        generate_rfem_xml(rf, out)
        @test isfile(out)
        doc = open(f -> read(f, XML.Node), out)   # well-formed check
        root = [c for c in doc.children if c isa Node &&
                c.nodetype === XML.Element && c.tag == "document"][1]
        basic = find_child(root, "model") |> m -> find_child(m, "basic_objects")
        @test length(basic.children) > 0
        rm(out)
    end
end
