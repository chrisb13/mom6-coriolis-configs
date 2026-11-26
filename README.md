# Jet: Phillips two-layer jet (main experiment)

Re-entrant 640 km channel, 10 km grid, two layers, an unstable Phillips jet that breaks into eddies, 400 days,
SPLIT = False. No input files: everything is analytic.

Sweep on `main`: `jet.yaml`: version A (10 km), B (40 km) and S (fast barotropic solver on, incl. the OM3-like
SADOURNY / BOUND_CORIOLIS combinations).

## Running it

On NCI Gadi with payu (`module use /g/data/vk83/modules && module load payu`):

```bash
payu run        # laboratory defaults to /scratch/$PROJECT/$USER/mom6; set `project:` in config.yaml if needed
```
Executable: `mom6-solo` from the ACCESS-OM3 release `access-om3/2026.05.004` (access-mom6 2026.05.003, MOM6 `d11a149`).
It is built for Sapphire Rapids, so the queue is `normalsr`.

`docs/` holds MOM_parameter_doc.* and available_diags from the archived control run, as in ACCESS-Community-Hub/anu-tub.

## Provenance

The runs on the page were made from commit `6a80bda` of this branch (then in a local repository on Gadi). The commit
after it only removes Gadi-specific paths (laboratory, tm70 storage and project); model settings are unchanged.

Written with Claude Code for the decoding-om3 page "Coriolis in MOM6".
