[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18527812.svg)](https://doi.org/10.5281/zenodo.18527812)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/dbeaup01/filament-eulerian-circulation/blob/main/Filament_Eulerian_Circulation_G3_N1500.ipynb
)

# Filament-Scale Eulerian Circulation — Gate 3 (N = 1500)

This notebook implements the frozen Gate 3 analysis used in Version 3 of the paper
“Filament-Scale Eulerian Circulation in the Cosmic Velocity Field”.

All subset definitions, sampling radii, null tests, and robustness procedures
are fixed a priori. Exploratory analyses and earlier pilot studies (e.g. N = 21)
are not used to define any results presented here.

---

## Paper and citation

The authoritative version of the manuscript associated with this repository is:

- **Filament-Scale Eulerian Circulation in the Cosmic Velocity Field**
- **Version 3 (current, peer-review ready)**  
  https://doi.org/10.5281/zenodo.18527812

Earlier exploratory versions (e.g. V2 and prior) are superseded by V3 and are
retained on Zenodo for record-keeping only.

If you use this code or analysis, please cite the Zenodo V3 DOI above.

---

## What’s new in Version 3 (V3)

Version 3 represents a **substantial methodological upgrade** over earlier
exploratory releases. Key changes include:

- Expansion from a small exploratory filament set to a **large, deterministic
  filament sample (~63,000 filaments)**.
- Introduction of **frozen analysis gates (Gate 3A / Gate 3B)** with all
  subsets, radii, and null procedures fixed *a priori*.
- Explicit separation of **geometry-destroying** (axis randomization) and
  **environment-destroying** (far-position relocation) null hypotheses.
- Comprehensive **velocity-field robustness tests**, including resolution
  perturbation and Gaussian smoothing.
- Conservative framing of results as **heterogeneous, non-universal empirical
  phenomenology**, without physical mechanism claims.

All figures and conclusions in the V3 paper are derived exclusively from these
frozen procedures.

---

## Repository contents

- `Filament_Eulerian_Circulation_V3.ipynb`  
  Main reproducible notebook implementing the circulation estimator,
  frozen null tests, robustness checks, and figures presented in the paper.

- `filament_finding.ipynb`  
  Supporting notebook demonstrating filament spine geometry handling
  and coordinate conventions.

- `filament_estimator.py`  
  Core routines for computing azimuthal velocity components and
  circulation profiles around filament axes.

Exploratory notebooks and early-phase diagnostic cells are clearly labeled
within the notebooks and are **not used** to define the V3 detection results.

---

## Data availability and inputs

This analysis uses the **Cosmicflows-4 (CF4)** reconstructed peculiar velocity
field and filament spine catalogs derived from spectroscopic galaxy surveys.

Due to size and licensing constraints, the velocity grids and filament catalogs
are **not included** in this repository.

To reproduce the analysis, users must supply:

- A Cosmicflows-4 reconstructed velocity grid (3D Cartesian cube)
- A filament spine catalog (e.g. DisPerSE output in 3D comoving coordinates)

The main notebook contains step-by-step instructions for loading these inputs,
including required formats and directory structure.

---

## Software environment

The analysis was developed and tested using:

- Python 3.10
- numpy 1.26
- scipy
- pandas
- matplotlib

Exact package versions and runtime notes are documented in the notebook headers.

---

## Scope and limitations

This repository supports an **empirical detection study** only.
It does **not** attempt physical interpretation, simulation validation,
or mechanism discrimination.

Future work will address:
- comparisons with independent velocity reconstructions,
- application to cosmological simulations,
- and physical interpretation of filament-scale circulation.

---

## Contact

Daniel Beaupré  
Independent Researcher  
ORCID: (add if/when available)- scipy 1.11
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
