"""Test :func:`~vacumm.misc.grid.regridding.transect` with interpolation in both time and space"""

# Inits
ncfile = "mars2d.xyt.nc"
lon0 = -5.4
lon1 = -4.7
lat0 = 48.1
lat1 = 48.6
time0 = "2008-08-15 07:00"
time1 = "2008-08-15 16:00"
splits = [None, 3, -3, (3, 'hour'), 3600*3.]


# Imports
from vcmq import (cdms2, data_sample, N, transect, stick2, code_file_name, os,
    transect_specs, add_map_lines, create_time, IterDates, P)

# Read data
f = cdms2.open(data_sample(ncfile))
u = f('u')
v = f('v')
f.close()

# Transect specs
tlons, tlats = transect_specs(u.getGrid(), lon0, lat0, lon1, lat1)
ttimes = create_time(IterDates((time0, time1), len(tlons), closed=True))

# Compute reference transect
tt = [transect(u, tlons, tlats, times=ttimes, split=split) for split in splits]

# Unittest
for ts in tt[1:]:
    N.testing.assert_allclose(tt[0], ts)

