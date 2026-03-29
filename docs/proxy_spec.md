# Proxy specification: C(Z)



This file specifies the numerical proxy \\(C(Z)\\) used throughout the project, including default parameters, CSV output format, and recommended diagnostics.



\## Definition (operational)

\- Cover the radial domain \\(\[r\_{\\min}, r\_{\\max}]\\) with overlapping shells \\(I\_j\\).  

\- On each shell compute a basis of local radial solutions for the Dirac ODE.  

\- Assemble the gluing matrix \\(A(Z)\\) from continuity conditions on overlaps.  

\- Compute singular values \\(\\sigma\_i\\) of \\(A(Z)\\).  

\- Choose threshold \\(\\varepsilon = \\kappa \\cdot \\sigma\_{\\max}\\) (default \\(\\kappa = 1\\mathrm{e}{-6}\\)).  

\- Define:

&#x20; 



\\\[

&#x20; C(Z) = \\#\\{i:\\ \\sigma\_i < \\varepsilon\\}.

&#x20; \\]







\## Default numerical parameters (PoC)

\- Integrator: adaptive RK45 (or RKF) with `rtol=1e-8`, `atol=1e-10`.  

\- Radial domain: `r\_min = max(1e-6, R\*1e-3)`, `r\_max = 300`–`600 a0` (increase for high Z).  

\- Cover: 8 overlapping shells (default); refine to 12 for convergence checks.  

\- Threshold: `epsilon = 1e-6 \* sigma\_max`.  

\- Z sweep: coarse ΔZ = 1; refine to ΔZ = 0.1 near suspected transitions.



\## Output CSV format

Columns (one line per Z):

\- `commit\_hash` — git short hash used for run  

\- `Z` — atomic number  

\- `model` — nucleus model (e.g., `sphere`, `point\_reg`)  

\- `R\_param` — radius parameter (fm) or regularization parameter  

\- `E1s\_au` — computed 1s energy in atomic units  

\- `E1s\_eV` — computed 1s energy in eV  

\- `C` — computed proxy integer  

\- `sigma\_min` — smallest singular value  

\- `sigma\_max` — largest singular value  

\- `r\_min`, `r\_max`, `rtol`, `atol`, `cover\_n` — numerical parameters used  

\- `notes` — free text



\## Reproducibility checklist

\- Record commit hash and exact command line.  

\- Save raw singular values and the assembled matrix `A(Z)` for at least one representative Z.  

\- Run convergence notebook (`notebooks/convergence.ipynb`) and attach plots for PR.



\## Sensitivity analysis

\- Vary `r\_max`, `cover\_n`, and `epsilon` and report changes in `C(Z)`.  

\- If `C(Z)` changes under refinement, mark the Z as "near-critical" and refine further.





