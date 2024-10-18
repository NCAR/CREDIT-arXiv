# CREDIT arXiv paper code repository

## About

This repository hosts the data pre-processing and verification works for the arXiv paper of NSF NCAR MILES Community Runnable Earth Digital Intelligence Twin (CREDIT).

## Python environment

Same as the main CREDIT repository.

## Navigaition

* `libs`: A collection of functions/scripts used by this repository.
  * `verif_utils.py`: functions used for forecasts post-processing and verification.
  * `score_utils.py`: function sued for computing certain verification scores.
  * `graph_utils.py`: data visualization functions.

* `verification`: this folder contains verification steps for CREDIT model runs. It can be implemented as follows:
  * Copy `verif_config_template.yml` to `verif_config.yml` and modify it based on your file directories.
  * Go through Jupyter notebooks from `STEP00` to `STEP02`.
  * Access scripts folder for large-scale verification runs.
  * Note: the verification setup was primarily tested on the data analysis server of NSF NCAR: `casper.ucar.edu`.

 * `visualization`: this folder hosts results of the CREDIT arXive paper. It is runable when all verification outputs are prepared.
