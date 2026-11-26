# Toy: an 8×8 ocean, one time step

An 8×8 doubly periodic, one-layer f-plane ocean (10 km cells, f = 1e-4 s⁻¹) with a uniform northward flow of
0.1 m/s over four blocks of different thickness, run for a single 1 s step. One step is enough to read off the
Coriolis acceleration each scheme computes at every u-point and compare it with the hand formula (check 2b on the page).

Inputs: two 8×8 files, written by `input/make_inputs.py` (no download needed):

```bash
python input/make_inputs.py /scratch/$PROJECT/$USER/mom6/input/coriolis-toy   # <laboratory>/input/coriolis-toy
```
Sweep: `experiment-generator/toy_all.yaml` on `main` (all nine CORIOLIS_SCHEME options).

## Running it

On NCI Gadi with payu (`module use /g/data/vk83/modules && module load payu`):

```bash
payu run        # laboratory defaults to /scratch/$PROJECT/$USER/mom6; set `project:` in config.yaml if needed
```
Executable: `mom6-solo` from the ACCESS-OM3 release `access-om3/2026.05.004` (access-mom6 2026.05.003, MOM6 `d11a149`).
It is built for Sapphire Rapids, so the queue is `normalsr`.

`docs/` holds MOM_parameter_doc.* and available_diags from the archived control run, as in ACCESS-Community-Hub/anu-tub.

## Provenance

The runs on the page were made from commit `e176eb7` of this branch (then in a local repository on Gadi). The commit
after it only removes Gadi-specific paths (laboratory, tm70 storage and project; input is now relative to the laboratory); model settings are unchanged.

Written with Claude Code for the decoding-om3 page "Coriolis in MOM6".
