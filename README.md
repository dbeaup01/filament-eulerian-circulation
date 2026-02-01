[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18371283.svg)](https://doi.org/10.5281/zenodo.18371283)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/dbeaup01/filament-eulerian-circulation/blob/main/Filament_Eulerian_Circulation_V3.ipynb
)

# Filament-Scale Eulerian Circulation

This repository accompanies the paper  
**“Filament-Scale Eulerian Circulation in the Cosmic Velocity Field”**.

It provides reproducible notebooks and supporting code used to analyze
the Cosmicflows-4 reconstructed velocity field and to measure
filament-scale Eulerian circulation around cosmic filaments.

## Paper

The manuscript associated with this repository is available on Zenodo:

- **Filament-Scale Eulerian Circulation in the Cosmic Velocity Field**
- Latest version (V2): https://doi.org/10.5281/zenodo.18443025


## Contents

- `notebooks/filament_eulerian_circulation_reproducible.ipynb`  
  Main reproducible notebook implementing the circulation estimator,
  null tests, and figures presented in the paper.

- `notebooks/filament_finding.ipynb`  
  Supporting notebook demonstrating filament spine handling and geometry.

- `filament_estimator.py`  
  Core routines for computing azimuthal velocity components and
  circulation profiles around filament axes.

## Data availability and inputs

This analysis uses the Cosmicflows-4 reconstructed peculiar velocity field.
Due to size and licensing constraints, the velocity grids and filament catalogs
are not included in this repository.

To reproduce the analysis, users must provide:
- A Cosmicflows-4 velocity grid (e.g. CF4 reconstructed velocity cube)
- A filament spine catalog (e.g. from DisPerSE)

The notebook `filament_eulerian_circulation_reproducible.ipynb`
contains step-by-step instructions for loading and preprocessing these inputs,
including expected file formats and directory structure.

### Software environment

This analysis was run using:
- Python 3.10
- numpy 1.26
- scipy 1.11
- astropy 6.0
- pandas 2.1
- matplotlib 3.8

Exact versions are not critical to the qualitative results.

## Scope

This repository presents a **purely observational, field-based analysis**.
No assumptions are made regarding the physical origin of the detected
circulation signals.

## License

This code is provided for research and reproducibility purposes.
