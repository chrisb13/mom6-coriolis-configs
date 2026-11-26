"""Copy a MOM6 restart directory and add a tiny, reproducible perturbation to potential temperature.

Usage: python perturb_restart.py <restart dir in> <restart dir out>
Adds N(0, 1e-6 degC) noise (seed 17112026) to every 'Temp' value in MOM.res*.nc where |Temp| < 1e20 (skips fill),
the 'noise floor' member: same model, same scheme, initial state different by far less than anything measurable.
"""
import shutil, sys
from pathlib import Path
import numpy as np
import netCDF4

src, dst = Path(sys.argv[1]), Path(sys.argv[2])
if dst.exists():
    sys.exit(f"{dst} exists; not overwriting")
shutil.copytree(src, dst)
rng = np.random.default_rng(17112026)
n = 0
for f in sorted(dst.glob("MOM.res*.nc")):
    with netCDF4.Dataset(f, "r+") as ds:
        if "Temp" in ds.variables:
            v = ds["Temp"]; a = v[:]
            mask = np.ma.getmaskarray(a) | (np.abs(np.ma.filled(a, 0)) >= 1e20)
            noise = rng.normal(0.0, 1e-6, a.shape)
            v[:] = np.where(mask, a, np.ma.filled(a, 0) + noise)
            n += 1
            print(f"perturbed Temp in {f.name}: shape {a.shape}, max |noise| {np.abs(noise[~mask]).max():.2e}")
if n == 0:
    sys.exit("no Temp variable found in MOM.res*.nc")
