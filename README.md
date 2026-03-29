# Peirce Continuum PoC — Relational Sheaf Algebra as an operational model for spectroscopy and overcriticality

**Short pitch**  
Peirce’s Continuum interprets measurement outcomes as local sections of relational sheaves. This PoC presents reproducible numerical examples for K‑shell binding energies in two nucleus models, provides three precise, falsifiable predictions, and supplies minimal code that allows experimental groups and numerical researchers to quickly check whether the proposed signatures appear in real data.

## Objective
This project demonstrates how a relational, topologically informed perspective on spectroscopy and overcriticality can be computed and tested in practice. It documents initial numerical findings and provides reproducible tools to experimentally test the proposed signatures.

## Repository contents
- src/dirac_radial_solver.py — Minimal radial Dirac solver (1s, κ = −1) with two nucleus models: point‑regularized and homogeneous sphere  
- notebooks/PoC.ipynb — Demo notebook for quick visualization of results  
- data/ — Example CSV format for result data  
- results/ — Example plots (E₁s vs Z)  
- predictions.md — Three falsifiable predictions with short measurement protocols  
- OUTREACH.md — Templates for outreach and short descriptions  
- requirements.txt — Dependencies for local reproduction

## Quick start (short)
1. Clone the repository.  
2. Install dependencies with: pip install -r requirements.txt  
3. Run a minimal sweep with: python src/dirac_radial_solver.py --model sphere --R_fm 5.0 --Z_max 200  
4. Results: CSV files in data/ and the plot in results/E1s_vs_Z.png. Open notebooks/PoC.ipynb for interactive analysis.

## Core results of this PoC
- The point nucleus (numerically regularized) reproduces the formal appearance at **Z ≈ 137**.  
- A homogeneous sphere with R = 5 fm shows no diving of the 1s state up to **Z = 200**; the critical charge is model dependent and lies well above 137.  
- Vacuum polarization (Uehling term) acts stabilizing and shifts the critical charge further upward.

## Three concise predictions (summary)
1. **K‑shell residual** — Systematic deviation from Dirac‑Fock values for K‑shell energies at Z ≳ 150; expected magnitude 10–200 eV.  
2. **Positron time profile** — For temporarily overcritical heavy‑ion collisions, characteristic positron time profiles and sum‑energy peaks are expected.  
3. **Scale‑proportional residuals** — Non‑eliminable, scale‑proportional residuals in precision fits across different Z scales, correlatable with numerically computed cohomology.  
Details on measurement protocols and signature tests are in predictions.md.

## Reproducibility and extension possibilities
- The minimal script is intentionally simple; planned extensions include the Uehling potential (vacuum polarization), Dirac‑Fock screening, finer Z resolution, and alternative nucleus models (e.g., Fermi distribution).  
- Convergence tests and numerical notes are documented in the notebook; the scripts are structured so that adjustments can be made quickly.

## Project structure (overview)
peirce-continuum-poc/  
├─ README.md  
├─ requirements.txt  
├─ src/  
│  └─ dirac_radial_solver.py  
├─ notebooks/  
│  └─ PoC.ipynb  
├─ data/  
│  └─ example_E1s_sphere.csv  
├─ results/  
│  └─ E1s_vs_Z.png  
├─ predictions.md  
└─ OUTREACH.md

## License
This project is released under the MIT License. See LICENSE for details.

## Usage notes
The calculations presented here are a proof of concept. The numerical results are model dependent and serve as a starting point for more precise calculations and experimental tests. The reproduction scripts and notebooks are designed to be quickly adapted and extended.

## Next sensible steps
- Systematically include the Uehling potential for Z in [150, 210] with fine resolution.  
- Implement a simple Dirac‑Fock screening to estimate many‑body effects.  

## Contributing
Issues and pull requests are welcome. For reproducibility questions, please attach relevant log output and the parameters used.
