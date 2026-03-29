\# Predictions and Measurement Protocols



This document lists three falsifiable predictions derived from the Peirce Continuum PoC and gives concise measurement protocols and acceptance criteria for quick experimental checks.



\## Prediction 1 — K‑Shell Residuals

\*\*Statement\*\*  

For hydrogenic or H‑like ions with effective nuclear charge Z ≳ 150, measured K‑shell binding energies will show systematic residuals relative to high‑precision Dirac‑Fock (DF) predictions. These residuals are expected to grow with Z and show a pattern consistent with a topological/cohomological contribution.



\*\*Expected magnitude\*\*  

Order of 10–200 eV for Z ≈ 150–180 (model dependent).



\*\*Measurement protocol\*\*  

\- Use precision X‑ray or laser spectroscopy on H‑like ions (EBIT or Penning trap).  

\- Measure K‑shell transition energies and compare to the best available DF + QED predictions (including Uehling where available).  

\- Report residuals ΔE = E\_meas − E\_DF with experimental uncertainties and calibration procedure.



\*\*Acceptance criteria\*\*  

\- Residuals that are reproducible across independent setups and exceed combined experimental + theoretical uncertainty by >5σ.  

\- Residuals show monotonic or structured dependence on Z not explained by known QED corrections or calibration systematics.



\## Prediction 2 — Positron Yield and Time Profile in Heavy‑Ion Collisions

\*\*Statement\*\*  

In collisions producing a transient effective charge Z\_eff ≳ 170, positron yields and time‑resolved emission profiles will show excess counts and characteristic temporal signatures beyond standard background and cascade models.



\*\*Expected signature\*\*  

\- Excess positron counts in a narrow time window following closest approach.  

\- Sum‑energy peaks or distortions relative to Monte‑Carlo background models; time profiles with a delayed tail correlated with collision geometry.



\*\*Measurement protocol\*\*  

\- Use heavy‑ion collision setups (GSI/FAIR style) with high‑resolution positron detectors and time stamping.  

\- Record coincident electron/positron events and sum‑energy spectra.  

\- Compare to detailed background simulations (including atomic cascade and pair production channels).



\*\*Acceptance criteria\*\*  

\- Statistically significant excess (Bayes factor >10 or p < 1e‑3) after accounting for known backgrounds.  

\- Reproducible signature across runs with similar Z\_eff and beam parameters.



\## Prediction 3 — Scale‑Proportional Residuals in Precision Fits

\*\*Statement\*\*  

When fitting spectroscopic data across a range of Z, residuals will contain a scale‑proportional component that cannot be removed by standard calibration or QED corrections and correlates with numerically computed indicators (e.g., computed cohomology proxy).



\*\*Expected signature\*\*  

\- Residuals that scale with Z (or a monotone function of Z) and persist under alternative fit models.



\*\*Measurement protocol\*\*  

\- Collect high‑precision spectral fits for a sequence of Z (or effective Z) values.  

\- Fit with standard theoretical models and record residuals.  

\- Test for a Z‑dependent component using regression and correlation with computed PoC indicators.



\*\*Acceptance criteria\*\*  

\- Residual component with effect size >5σ after controlling for known systematic effects.  

\- Correlation with computed PoC indicator (Spearman or Pearson r significant at p < 0.01).



\## Notes on Data Reporting

\- Always include raw spectra, calibration runs, detector response, and analysis scripts.  

\- Provide uncertainties (statistical and systematic) and the theoretical model version used for comparison.  

\- If possible, provide data in machine‑readable CSV format with metadata (beam energy, ion species, trap conditions, detector settings).



\## Quick checklist for submitting a test

\- Raw data files (or links) + analysis script.  

\- Calibration description and reference lines used.  

\- Theoretical DF/QED reference used for comparison (version/citation).  

\- Short README describing run conditions and any pre‑processing.



