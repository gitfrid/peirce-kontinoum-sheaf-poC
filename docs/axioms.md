\# RCSA Operational Axioms



This document records the three operational axioms for the Relational Continuum Sheaf Algebra (RCSA). Each axiom is given in three parts: (1) short statement, (2) precise mathematical translation, (3) operational test and validity scope.



\---



\## Axiom 1 — Iconicity (Ikonizität)



\*\*Statement\*\*  

The periodic table is an iconic diagram of the sheaf structure \\(\\mathcal{E}\_Z\\); magic numbers correspond to points of locally minimal gluing obstruction.



\*\*Mathematical formulation\*\*  





\\\[

\\text{PeriodicTable} \\cong \\text{Icon}(\\mathcal{E}\_Z),

\\qquad

\\text{magic numbers } \\{2,8,18,32,\\dots\\} \\text{ correspond to local minima of } \\dim\_\\varepsilon H^1(\\mathcal{E}\_Z).

\\]







Here \\(\\dim\_\\varepsilon H^1(\\mathcal{E}\_Z)\\) denotes the numerically computed dimension of \\(H^1\\) under tolerance \\(\\varepsilon\\).



\*\*Operational test\*\*  

\- Compute the proxy \\(C(Z)\\) (see `docs/proxy\_spec.md`) across a range of \\(Z\\).  

\- Check whether local minima of \\(C(Z)\\) align with known magic numbers within a tolerance \\(\\Delta Z\\) (default \\(\\Delta Z \\le 1\\)).  

\- Verify stability under refinement (see Lemma A in `docs/lemmas.md`).



\*\*Validity scope\*\*  

Single‑particle Dirac models, spherically symmetric potentials, static nucleus. Not valid without explicit many‑body corrections unless stated.



\*\*Limitations\*\*  

Does not by itself include Dirac‑Fock screening or higher‑order QED corrections; these must be added as model extensions.



\---



\## Axiom 2 — Habits (Stabile relationale Fixpunkte)



\*\*Statement\*\*  

A chemical element (atomic number \\(Z\\)) corresponds to a stable global section of \\(\\mathcal{E}\_Z\\) that is invariant under nilpotent infinitesimal shifts; stability is signaled by minimal local gluing obstruction.



\*\*Mathematical formulation\*\*  





\\\[

\\text{Element with } Z \\iff \\exists\\ \\sigma\_Z \\in \\Gamma(\\mathcal{E}\_Z)\\ \\text{with}\\ D\\sigma\_Z = 0,\\ D^2=0,

\\]





and locally \\(\\dim\_\\varepsilon H^1(\\mathcal{E}\_Z)\\) is minimal.



\*\*Operational test\*\*  

\- For candidate \\(Z\\), compute \\(C(Z)\\). If \\(C(Z)\\) is locally minimal and stable under refinement, label \\(Z\\) as a stable habit.  

\- Compare with experimental stability indicators (ionization energies, closed‑shell signatures).



\*\*Validity scope\*\*  

Same as Axiom 1; explicitly single‑particle unless screening is included.



\*\*Limitations\*\*  

Stability here is relational (cohomological), not solely energetic.



\---



\## Axiom 3 — Continuity (Synechismus)



\*\*Statement\*\*  

The mapping \\(Z \\mapsto \\dim\_\\varepsilon H^1(\\mathcal{E}\_Z)\\) is continuous in the operational sense; transitions between regimes are reflected by continuous changes in the cohomology proxy rather than ontologically sharp jumps.



\*\*Mathematical formulation\*\*  





\\\[

\\text{Periodensystem} = \\text{continuous map } Z \\mapsto \\dim\_\\varepsilon H^1(\\mathcal{E}\_Z),

\\]





with critical thresholds \\(Z\_c\\) where \\(\\dim\_\\varepsilon H^1\\) grows continuously.



\*\*Operational test\*\*  

\- Sweep \\(Z\\) and plot \\(C(Z)\\) vs \\(Z\\). Look for continuous trends and identify critical thresholds \\(Z\_c\\) where \\(C(Z)\\) increases persistently.  

\- Confirm that near thresholds the behavior refines smoothly under mesh/tolerance refinement.



\*\*Validity scope\*\*  

Applies to families of smooth potentials \\(V\_Z\\) and to numerically resolvable regimes.



\*\*Limitations\*\*  

Numerical resolution may blur very sharp theoretical transitions; interpret with convergence diagnostics.



\---



\## Notes



\- Use the notation \\(C(Z; h, \\tau, \\varepsilon)\\) to make explicit dependence on mesh \\(h\\), integrator tolerances \\(\\tau\\), and singular‑value threshold \\(\\varepsilon\\).  

\- For reproducibility, always record commit hash, exact parameters, and output CSV for any figure or claim.



