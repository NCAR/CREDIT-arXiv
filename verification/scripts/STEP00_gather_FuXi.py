'''
This script collects 6 hourly FuXi forecast (trained using CREDIT) and combines
predicitons from the same initialization.

The script runs with config file `verif_config_6h.yml` and produces netCDF4 files
with one file per initialization on a given range:
```
python STEP00_gather_fuxi.py 0 365
```
where 0 and 365 are the first and the last initialization.

Note: `vu.process_file_group` uses `xr.open_mfdataset`, which can cause some 
multi-thread issues if memory allocation is too small. Users can switch to 
`vu.process_file_group_safe` in case.
'''

import os
import sys
import yaml
from glob import glob
from datetime import datetime

import numpy as np
import xarray as xr

import warnings
warnings.filterwarnings('ignore')

sys.path.insert(0, os.path.realpath('../../libs/'))
import verif_utils as vu

config_name = os.path.realpath('../verif_config_6h.yml')

with open(config_name, 'r') as stream:
    conf = yaml.safe_load(stream)

# parse input
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('verif_ind_start', help='verif_ind_start')
parser.add_argument('verif_ind_end', help='verif_ind_end')
args = vars(parser.parse_args())

verif_ind_start = int(args['verif_ind_start'])
verif_ind_end = int(args['verif_ind_end'])

# ======================= #
model_name = 'fuxi'
# ======================= #

variables_levels = None

base_dir = conf[model_name]['save_loc_rollout']
output_dir = conf[model_name]['save_loc_gather']
time_intervals = None

# Get list of NetCDF files
all_files_list = vu.get_nc_files(base_dir)

ind_start = verif_ind_start
ind_end = verif_ind_end

flag_overall = False

while flag_overall is False:
    
    flag_overall = True
    
    for i in range(ind_start, ind_end):
        file_list = all_files_list[i]
        
        if len(file_list) >= 40:
            flag = vu.process_file_group(file_list, output_dir, variables_levels, size_thres=9306171909)
            flag_overall = flag_overall and flag
            