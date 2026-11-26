"""Write the two input files of the toy (8x8, doubly periodic, one layer) into <dir>.

h = bottom depth = layer thickness (flat sea surface, so no pressure force), index i west->east, j south->north:
    j <= 4: 1200 m (i <= 4), 800 m (i >= 5);   j >= 5: 600 m (i <= 4), 400 m (i >= 5)
Velocity is set in MOM_input (VELOCITY_CONFIG = "uniform", v = 0.1 m/s): reading it from a file failed with the
release executable's symmetric memory.
Usage: python input/make_inputs.py <laboratory>/input/coriolis-toy
"""
import sys
from pathlib import Path
import numpy as np
import netCDF4

N = 8
out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
h = np.empty((N, N))
h[:4, :4], h[:4, 4:] = 1200.0, 800.0
h[4:, :4], h[4:, 4:] = 600.0, 400.0
for name, var, arr, dims in (("topog.nc", "depth", h, ("ny", "nx")), ("h_ic.nc", "h", h[None], ("Layer", "ny", "nx"))):
    with netCDF4.Dataset(out / name, "w") as d:
        d.createDimension("Layer", 1); d.createDimension("ny", N); d.createDimension("nx", N)
        d.createDimension("nyq", N + 1); d.createDimension("nxq", N + 1)
        d.createVariable(var, "f8", dims)[:] = arr
    print("wrote", out / name)
