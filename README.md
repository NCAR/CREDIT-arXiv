# CREDIT arXiv Paper Code Repository

## About

This repository hosts the main results of the Community Research Earth Digital Intelligence Twin (CREDIT).  
* Preprint: https://arxiv.org/abs/2411.07814

## Python Environment

The Python environment is the same as in the main CREDIT repository.

## Navigation

* `data_preprocessing`: This folder contains scripts and Jupyter notebooks for the computation of z-score and residual normalization. Follow these steps:
  * Copy `data_config_6h_template.yml` to `data_config_6h.yml` (similarly for `1h`) and modify it based on your file directories.
  * Run through the Jupyter notebooks from `STEP00` to `STEP03`.
  * Access the `scripts` folder for large-scale verification runs.
    
* `verification`: This folder contains verification steps for CREDIT model runs. Follow these steps:
  * Copy `verif_config_6h_template.yml` to `verif_config_6h.yml` (similarly for `1h`) and modify it based on your file directories.
  * Run through the Jupyter notebooks from `STEP00` to `STEP05`.
  * Access the `scripts` folder for large-scale verification runs.

* `visualization`: This folder hosts the results of the CREDIT arXiv paper. It is runnable once all verification outputs are prepared.

* `libs`: A collection of functions/scripts used by this repository.
  * `preprocess_utils.py`: Functions for z-score and residual normalization calculations.
  * `verif_utils.py`: Functions for forecast post-processing and verification.
  * `score_utils.py`: Functions for bootstrapping and computing the zonal energy spectrum.
  * `graph_utils.py`: Functions for data visualization.

## Production File Storage

If you have access to NCAR/UCAR HPCs, you can access production output files at the following locations:

```bash
/glade/campaign/cisl/aiml/ksha/CREDIT_arXiv/GATHER/fuxi_6h_20241029/
/glade/campaign/cisl/aiml/ksha/CREDIT_arXiv/GATHER/wxformer_6h_20241029/
/glade/campaign/cisl/aiml/wchapman/CREDIT_arXiv/GATHER/wxformer_1h_20241228/
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

Model weights are not stored in this repository. They can be found at the following locations:

```bash
/glade/campaign/cisl/aiml/ksha/CREDIT_runs/arXiv_project/fuxi_6h/model_checkpoint.pt
/glade/campaign/cisl/aiml/ksha/CREDIT_runs/arXiv_project/wxformer_6h/model_checkpoint.pt
/glade/campaign/cisl/aiml/ksha/CREDIT_runs/arXiv_project/wxformer_1h/model_checkpoint.pt
```

We will upload the model weights online soon. Stay tuned.

## Contact
* John Schreck schreck@ucar.edu
* Yingkai Sha ksha@ucar.edu
* William Chapman wchapman@ucar.edu
* David John Gagne II dgagne@ucar.edu

