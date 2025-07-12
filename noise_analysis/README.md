## Noise Perturbation Analysis

This directory contains code and results for analyzing the impact of Gaussian noise perturbations applied to atmospheric variables across all model levels for 1deg GraphGRUNet and WXForrmer. The perturbed variables include:

- **Q**: Specific humidity  
- **T**: Temperature  
- **U**: Zonal wind  
- **V**: Meridional wind

### Folder Structure

Each subfolder is named according to the standard deviation of the Gaussian noise applied. For example:
- `0_1/` → Perturbations applied with a standard deviation of 0.1

### Notebooks

Each Jupyter notebook is suffixed with the name of the variable it analyzes. For example:
- `exploration_Q.ipynb` → Results from perturbing the Q variable  


`no_noise_viz.ipynb` includes unperturbed control runs.