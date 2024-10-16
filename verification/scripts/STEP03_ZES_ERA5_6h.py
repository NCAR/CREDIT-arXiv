'''
This script computes zonal energy spectrum of kinetic energy and potential temperature
energy from 6 hourly ERA5. It runs with config file `verif_config_6h.yml`. The script 
produces a netCDF4 file on `path_verif`.

Note: the script assumes coordinate names are `latitude` and `longitude`. Potential
temperature is computed using an approximation, but it does not impact the energy
distributions.
'''

import os
import sys
import yaml
import argparse
from glob import glob
from datetime import datetime, timedelta

import numpy as np
import xarray as xr

sys.path.insert(0, os.path.realpath('../../libs/'))
import verif_utils as vu
import score_utils as su

config_name = os.path.realpath('../verif_config_6h.yml')

with open(config_name, 'r') as stream:
    conf = yaml.safe_load(stream)

# parse input
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('verif_ind_start', help='verif_ind_start')
parser.add_argument('verif_ind_end', help='verif_ind_end')
args = vars(parser.parse_args())

path_verif = conf['ERA5_weatherbench']['save_loc_clim']+'combined_zes_clim.nc'

variables_levels = conf['ERA5_ours']['verif_variables']
varnames = list(variables_levels.keys())

# ---------------------------------------------------------------------------------------- #
# ERA5
filename_ERA5 = sorted(glob(conf['ERA5_ours']['save_loc']))

# pick years (use IFS years)
year_range = conf['IFS']['year_range']
years_pick = np.arange(year_range[0], year_range[1]+1, 1).astype(str)
filename_ERA5 = [fn for fn in filename_ERA5 if any(year in fn for year in years_pick)]

# merge yearly ERA5 as one
ds_ERA5 = [vu.get_forward_data(fn) for fn in filename_ERA5]
ds_ERA5_merge = xr.concat(ds_ERA5, dim='time')

# subset merged ERA5 and unify coord names
ds_ERA5_merge = vu.ds_subset_everything(ds_ERA5_merge, variables_levels)
L_time = len(ds_ERA5_merge['time'])

verif_results = []

for i_time in range(L_time):
    ds_ERA5 = ds_ERA5_merge.isel(time=i_time)    
    ds_ERA5 = ds_ERA5.load()

    # -------------------------------------------------------------- #
    # potential temperature
    ds_ERA5['theta'] = ds_ERA5['T500'] * (1000/500)**(287.0/1004)

    # -------------------------------------------------------------- #
    zes_temp = []
    for var in ['U500', 'V500', 'theta']:
        zes = su.zonal_energy_spectrum_sph(ds_ERA5, var)
        zes_temp.append(zes)
        
    verif_results.append(xr.merge(zes_temp))

ds_verif = xr.concat(verif_results, dim='time')

ds_verif.to_netcdf(path_verif)



