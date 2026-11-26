# Gyre: wind-driven single gyre (warm-up rung)

Closed 2000 km square basin, 25 km grid, one layer, beta-plane, MOM6's built-in single-gyre wind, 180 days.
Horizontal viscosity KH = 67200 m²/s (Munk width 150 km = 6 cells), with momentum-budget diagnostics for the
vorticity balance across the western boundary current. No input files: grid, depth and wind are analytic.

Sweeps on `main`: `gyre_schemes.yaml` (six schemes + no rotation + uniform rotation), `gyre_nodrag.yaml`
(bottom-friction test), `gyre_munk.yaml` (boundary-current width tests; branches from the earlier KH = 8400 commit 6da4ead).

## Running it

On NCI Gadi with payu (`module use /g/data/vk83/modules && module load payu`):

```bash
payu run        # laboratory defaults to /scratch/$PROJECT/$USER/mom6; set `project:` in config.yaml if needed
```
Executable: `mom6-solo` from the ACCESS-OM3 release `access-om3/2026.05.004` (access-mom6 2026.05.003, MOM6 `d11a149`).
It is built for Sapphire Rapids, so the queue is `normalsr`.

`docs/` holds MOM_parameter_doc.* and available_diags from the archived control run, as in ACCESS-Community-Hub/anu-tub.

## Provenance

The runs on the page were made from commit `7f9d411` of this branch (then in a local repository on Gadi). The commit
after it only removes Gadi-specific paths (laboratory, tm70 storage and project); model settings are unchanged.

Written with Claude Code for the decoding-om3 page "Coriolis in MOM6".
