# MOM6 Coriolis-scheme configurations

Model configurations behind the decoding-om3 page **Coriolis in MOM6** (which `CORIOLIS_SCHEME` to use, and does
it matter?). Each config branch is one runnable payu configuration; the scheme tests are made from them with the
[ACCESS Experiment Generator](https://github.com/ACCESS-NRI/access-experiment-generator) using the YAML files in
`experiment-generator/`. The analysis and figure scripts live with the page in
[decoding-om3](https://github.com/ACCESS-Community-Hub/decoding-om3) (`documentation/docs/pages/mom6/coriolis-in-mom6/`).

| Branch / source | What it is | Page section | Sweep |
|---|---|---|---|
| `toy-8x8` (bc3487d) | 8×8 one-layer ocean, one 1 s step | §3 tiny ocean | `toy_all.yaml` |
| `gyre` (4bf7dd0) | wind-driven single gyre, 25 km, 180 days | §4 warm-up | `gyre_schemes.yaml`, `gyre_nodrag.yaml`, `gyre_munk.yaml` |
| `jet` (1946ba7) | Phillips two-layer jet, 10 / 40 km, 400 days | §5 main experiment | `jet.yaml` |
| ACCESS-NRI/access-om3-configs `dev-MC_100km_jra_ryf` @ 6130fff | global ACCESS-OM3, 100 km, RYF | §6 planet | `om3_100km.yaml` |
| ACCESS-Community-Hub/anu-tub @ e413708 | idealised 0.25° sector ocean, 5-yr spin-up then branches | §6 eddies | `anu_tub_spinup.yaml`, then `anu_tub_branches.yaml` (+ `scripts/perturb_restart.py`) |
| Tasman Sea regional 1/4°, 1/10°, 1/20° | regional ACCESS-OM3, RYF | to come | to come; inputs are generated, not stored |

Configurations that already exist elsewhere (100 km, ANU-TUB) are not copied here: the sweep branches from the
upstream repository at a fixed commit and changes only the Coriolis settings (plus, for ANU-TUB, the executable and
run bookkeeping). Runs that branch from a spun-up state take the restart directory as a placeholder in the YAML.

## How to reproduce a sweep

On NCI Gadi (the Experiment Generator needs internet, so use `copyq` or a login node):

```bash
module use /g/data/vk83/modules && module load payu
cd experiment-generator
# 1. set test_path in the YAML to a directory of your own
# 2. generate the branches and start every run (payu submits the model jobs):
qsub -v YAML=$PWD/jet.yaml,NAME=coriolis_jet pbs/gen_and_run.pbs
```
Add `NRUNS=<n>` to run n segments per branch (the 100 km runs used NRUNS=2).

Executable for the MOM6-only cases: `mom6-solo` from `access-om3/2026.05.004` (MOM6 `d11a149`), `normalsr` queue.

Written with Claude Code; hosted on a personal account for now (to move to ACCESS-Community-Hub later).
