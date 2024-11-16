# CREDIT arXiv paper code repository

## About

This repository hosts the main results of Community Research Earth Digital Intelligence Twin (CREDIT). 
* Pre-print: https://arxiv.org/abs/2411.07814

## Python environment

Same as the main CREDIT repository.

## Navigaition

* `libs`: A collection of functions/scripts used by this repository.
  * `preprocess_utils.py`: functions purposed for the z-score and residual norm calculation.
  * `verif_utils.py`: functions used for forecasts post-processing and verification.
  * `score_utils.py`: function used for boostrapping and computing zonal energy spectrum.
  * `graph_utils.py`: data visualization functions.

* `verification`: this folder contains verification steps for CREDIT model runs. It can be implemented as follows:
  * Copy `verif_config_6h_template.yml` to `verif_config_6h.yml` (same for `1h`) and modify it based on your file directories.
  * Go through Jupyter notebooks from `STEP00` to `STEP05`.
  * Access scripts folder for large-scale verification runs.
  * Note: the verification setup was primarily tested on the data analysis server of NSF NCAR: `casper.ucar.edu`.

 * `visualization`: this folder hosts results of the CREDIT arXive paper. It is runable when all verification outputs are prepared.

## Production file storage
If you have access to NCAR/UCAR HPCs. You may visit production output files at:
```bash
/glade/campaign/cisl/aiml/ksha/CREDIT_arXiv/GATHER/fuxi_6h_20241029/
/glade/campaign/cisl/aiml/ksha/CREDIT_arXiv/GATHER/wxformer_6h_20241029/
/glade/campaign/cisl/aiml/ksha/CREDIT_arXiv/GATHER/wxformer_1h_20241029/
/glade/campaign/cisl/aiml/ksha/CREDIT_arXiv/GATHER/IFS/
```
Verification results are available at:
```bash
/glade/campaign/cisl/aiml/ksha/CREDIT_arXiv/VERIF/
```
The pre-processed ERA5 and solar irradiance data (i.e., training and verification target) are available at:
```bash
/glade/derecho/scratch/ksha/CREDIT_data/ERA5_mlevel_arXiv/SixHourly_y*
/glade/campaign/cisl/aiml/wchapman/MLWPS/STAGING/y_TOTAL*
```
## Model weights
Model weights are not stored in this repo, they can found at:
```bash
/glade/campaign/cisl/aiml/ksha/CREDIT_runs/arXiv_project/fuxi_6h/model_checkpoint.pt
/glade/campaign/cisl/aiml/ksha/CREDIT_runs/arXiv_project/wxformer_6h/model_checkpoint.pt
/glade/campaign/cisl/aiml/ksha/CREDIT_runs/arXiv_project/wxformer_1h/model_checkpoint.pt
```
We will upload model weights online soon. Stay tuned.

## Contact
* John Schreck schreck@ucar.edu
* Yingkai Sha ksha@ucar.edu
* William Chapman wchapman@ucar.edu
* David John Gagne II dgagne@ucar.edu

