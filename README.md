[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18371283.svg)](https://doi.org/10.5281/zenodo.18371283)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/dbeaup01/filament-eulerian-circulation/blob/main/SFH_Filament_Rotation_CF4_Reproducible.ipynb
)

# Filament-Scale Eulerian Circulation

This repository accompanies the paper  
**“Filament-Scale Eulerian Circulation in the Cosmic Velocity Field”**.

It provides reproducible notebooks and supporting code used to analyze
the Cosmicflows-4 reconstructed velocity field and to measure
filament-scale Eulerian circulation around cosmic filaments.

## Contents

- `paper/`  
  PDF of the manuscript describing the observational analysis and results.

- `notebooks/filament_eulerian_circulation_reproducible.ipynb`  
  Main reproducible notebook implementing the circulation estimator,
  null tests, and figures presented in the paper.

- `notebooks/filament_finding.ipynb`  
  Supporting notebook demonstrating filament spine handling and geometry.

- `src/filament_estimator.py`  
  Core routines for computing azimuthal velocity components and
  circulation profiles around filament axes.

## Data

The analysis uses the publicly available **Cosmicflows-4**
reconstructed velocity field.
Due to data size and licensing considerations, the full velocity grids
are not included in this repository.
Instructions for obtaining the required inputs are provided in the
main notebook.

## Scope

This repository presents a **purely observational, field-based analysis**.
No assumptions are made regarding the physical origin of the detected
circulation signals.

## License

This code is provided for research and reproducibility purposes.
