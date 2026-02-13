[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18636236.svg)](https://doi.org/10.5281/zenodo.18636236)

[![Open In Colab — CF4](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/dbeaup01/filament-eulerian-circulation/blob/main/Filament_Eulerian_Circulation_G3_N1500.ipynb
)

# Filament-Scale Eulerian Circulation — Gate 3 (N = 1500)

This repository implements the frozen Gate 3 detection and robustness analysis
used in **Version 4 (V4)** of the manuscript:

> *Filament-Scale Eulerian Circulation in the Cosmic Velocity Field*

The analysis measures coherent Eulerian circulation around cosmic filaments
directly in reconstructed three-dimensional peculiar-velocity fields.

All filament subset definitions, sampling radii, null tests, and robustness
procedures are fixed *a priori*. Earlier exploratory analyses (e.g. small-N pilot
studies) are not used to define the reported results.
---
## Repository Contents

- `Filament_Eulerian_Circulation_G3_N1500.ipynb`  
  **Primary analysis notebook.**  
  Implements the frozen Gate 3 (N ≈ 1500) detection and robustness framework
  used in Version 4 (V4) of the manuscript. All figures and statistics reported
  in the paper are generated from this notebook.

- `2M++_reconstruction_Independence_test.ipynb`  
  Reconstruction-independence comparison notebook using the 2M++ velocity field.
  Implements the same frozen subsets, radii, and null procedures.

- `filament_finding.ipynb`  
  Supporting notebook demonstrating filament spine geometry handling,
  coordinate conventions, and cylindrical sampling configuration.

- `filament_estimator.py`  
  Core routines for computing azimuthal velocity components and circulation
  profiles Γ(R) around filament axes.

- `filament_eulerian_circulation_reproducible.ipynb`  
  Early development notebook retained for transparency and historical reference.
  **Not used to generate results in V4.**

  ---

## Data Availability and Inputs

This analysis uses reconstructed large-scale peculiar velocity fields and
three-dimensional filament spine catalogs.

Primary reconstruction:
- **Cosmicflows-4 (CF4)** velocity field

Comparison reconstruction:
- **2M++** density-field–based velocity solution

Filament geometry:
- DisPerSE-derived filament spines in 3D comoving coordinates

Due to size and licensing constraints, velocity grids and filament catalogs
are not included in this repository.

To reproduce the analysis, users must supply:

- A 3D reconstructed velocity grid (Cartesian format)
- A filament spine catalog with consistent coordinate system

The main notebook provides step-by-step input formatting guidance.

---

## Software Environment

Developed and tested using:

- Python 3.10
- numpy 1.26
- scipy 1.11
- pandas 2.1
- matplotlib 3.8
- astropy 6.0

Minor version differences are not expected to alter qualitative results.

---

## Scope and Positioning

This repository supports a **purely empirical, field-based detection study**
of filament-scale Eulerian circulation in reconstructed cosmic velocity fields.

The analysis:

- Does not assume a physical mechanism.
- Does not modify gravity or cosmology.
- Does not rely on halo spins or galaxy morphology proxies.
- Does not claim universality of circulation.

Results are framed conservatively as a heterogeneous,
environment-dependent phenomenology within reconstructed velocity fields.

Interpretation and mechanism discrimination are explicitly deferred to future work.

---

## License

Released under the MIT License for research and reproducibility purposes.

---

## Contact

Daniel Beaupré  
Independent Researcher  
ORCID: (https://orcid.org/0009-0004-5690-7864)
