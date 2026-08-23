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
