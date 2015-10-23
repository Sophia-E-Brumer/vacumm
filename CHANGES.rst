Release notes
#############

Version 3.0.0
=============

- Added font weight change for degrees in labels.
- Added standard_names to names for searching in cf.
- Added showvar.py to quickly display a netcdf variable.
- Added support for min+max+hist and restart to StatAccum.
- Added support for exact and block kriging to OCK.
- Added sill and range to linear variogram model in kriging.
- Added constraints to variogram model fit.
- Added color.discretize_cmap.
- Added Plot.add_water_mark.
- Added units.basic_proj.
- Added systematic cleaning to cache_map().
- Added [vacumm.misc.grid.basemap]max_cache_size config option.
- Added cellerr method to regrid1d.
- Added time arguments support if applicable to Plot.add_point().
- Added dstwgt method for fortran interpolators from gridded to random points.
- Added tuple support for time creation routines of atime.
- New regrid2d with tool and method keywords.
- Fixed range in hlitvs.
- Fixed mixed_layer_depth with kz.
- Fixed: default params in get_proj.
- Fixed names of module attributes which are now upper case.
- Fixed: list_forecast_files, Plot.add_lon/lat, _interp_.linept, Plot2D.fill.
- Fixed: ConfigManager.opt_parse.
- Removed sphinxfortran extension which is now a standalone vacumm project.

Version 2.5.4
=============

- Added "make safedoc" target.
- Fixed: english translations++.
- Fixed: missing test_plot_add_logo.py.
- Fixed: multifit+multiproc in kriging.
- Fixed: ConfigManager.arg_parse helps.
- Fixed: station_info import of oldnumeric.

Version 2.5.1
=============

- Changed: module level config files renamed to vacumm.cfg.
- Fixed: access to vacumm_nice_gfdl and vacumm_ssec colormaps.
- Fixed: Logger and specs for Profile.
- Fixed: add_logo.
- Fixed: removed dependency to pytz, which must now be installed
  to add time zone support to vacumm.

Version 2.5.0
==============

- Added: camp_nice_gfdl colormap.
- Added: Plot.add_annotation.
- Added: misc.plot.advanced.add_things tutorial.
- Fixed: gen_gallery.

Version 2.4.2
==============

- Added: misc.isempty.
- Fixed: cfg2rst, ConfigManager, StepsNorm.

Version 2.4.1
==============

- Upgraded: Logger.
- Added: docversions sphinx extension.
- Fixed: ConfigManager.opt_parse/arg_parse, Shapes, get_proj, get_xy,
  seawater import, are_good_units, Shapes.__init__/plot.

Version 2.4.0
==============

- Added: Added fp + th1p + some wind variables to cf.
- Added: add_arrow method to Plot2D.
- Added: add_map_places plot function.
- Improved: In curve2, an array can be passed to fill_between keyword.
- Fixed: ConfigManager, polygon_select, polygon_mask, coord2slice, sigma,
  tide.filters, StepsNorm, list_forecast_files, NEMO.

Version 2.3.1
=============

- Fortran regrid1d routines work directly with missing values.
- Unit tests save outputs in scripts directory.
- Fixed installation issue with setup.*.
- Fixed bugs: list_forecast_files, filter_selector, NEMO, coord2slice.

Version 2.3.0
=============

- Added the new CurvedInterpolator based on some fortran code
  primarily used for computing transects.
- New regrid1dnew that can regrid from a variable 1D axis to another
  variable 1D axis, like for instance from sigma to sigma coordinates.
  It will later replace regrid1d. Extrapolation in regrid1dnew is
  now available for all methods.
- Improvements for staggered grids in Dataset.
- minimap can now display background data instead of ocean color.
- cf: added wspd and wdir for wind.
- Smaller data samples.
- Better management of staggering in Dataset and arakawa (still experimental).
- Removed setup.cfg and added two templates, with a simple one and
  another one for OpenMP parallelisation.
- Fixed issues: vacumm config, sigma2depth, grid2xy, format_var,
  fortran_domain, etc.



