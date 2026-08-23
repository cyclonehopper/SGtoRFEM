# AGENTS.md — guidance for coding agents working in this repo

## What this is

SGtoRFEM: a Julia package converting Space GASS text exports (.TXT) into
Dlubal RFEM 6 XML project files.

Pipeline: `parser.jl` → `converter.jl` → `rfem_writer.jl`, all included into
the single module `SGtoRFEM` (src/SGtoRFEM.jl). There are no submodules.

## Conventions & facts you must know

- **Units**: SG model is Z-up, m / kN / kN-m; sections in mm, strength MPa.
  RFEM XML wants m / Pa. Convert in `converter.jl` only.
- **Member local axes** (identical in SG and RFEM): x = member length,
  y = section minor axis, z = section major axis. Right-hand rule.
  rx = torsion, ry = minor bending, rz = major bending. Do not swap Y/Z.
- **Sections**: always exported as *parametric* sections (dimensions only) so
  no RFEM library lookup can fail. The section **name encodes the parameters**
  and is parsed by RFEM:
  - I: `I h/b/t_w/t_f/r_1/r_2/H` in mm, r_1 = t_w, r_2 = 0
  - CHS/RHS/SHS: `CHS d/t/C`, `RHS h/b/t/C`, `SHS b/t/C` in metres, C = cold formed
  - U (PFC): `U h/b/t_w/t_f/H` in metres
- **Materials**: all steel, isotropic linear elastic
  (`MATERIAL_MODEL_ISOTROPIC_LINEAR_ELASTIC`). Default S355 synthesised when
  the SG export has no MATERIALS block; material id 1 must always exist.
- **Load axis codes** (4th field of MEMBCONC/MEMBFORCES rows):
  `G` global true length, `A` global projected, `L` member local.
  Spec field (5th): `%` relative distances (0–100), `A` absolute metres.
- **MEMBFORCES row layout**: lc, member, slot, axis, spec, a, b,
  Fx1, Fx2, Fy1, Fy2, Fz1, Fz2 [, cat]
- **MEMBCONC row layout**: lc, member, loadno, axis, spec, a,
  Fx, Fy, Fz, Mx, My, Mz [, cat]
- **Member releases**: SG colour fields c1/c2 are actually release codes
  (6 chars per end, R = released). Written as RFEM MemberHinges referenced by
  `member_hinge_start`/`member_hinge_end`.

## Environment gotchas

- Julia ≥ 1.12, XML.jl **0.4.x** API only: `read(f, XML.Node)`,
  `Node{String}(XML.Element, tag, nothing, nothing, children::Vector)`,
  mutate via `push!`/`empty!` on `.children`. There is no `add_child`,
  `TextNode`, or `XML.read(f, XML.Document)` in 0.4.x.
- `Base.eof` must be qualified in-module (`XML` also exports `eof`).
- New deps must be added to Project.toml AND `Pkg.resolve()` run.
- RFEM enums/tag names must come from the official schema — check the
  dlubal.api wheel (PyPI, gRPC protos) or an RFEM-exported XML before
  inventing tag names. Never guess enum strings.

## Testing

- `julia --project=. -e 'using Pkg; Pkg.test()'`
- Tests parse `sg_txt_out/sg_export.TXT` and validate conversion + XML output.
- Test file export goes to `tempdir()` — never write/delete files under
  `sg_txt_out/` from tests.
