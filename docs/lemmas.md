\# Lemmas and technical statements



This file contains two foundational lemmas that support the operational axioms and the numerical proxy.



\## Lemma A — Numerical stability of the cohomology proxy under refinement



\*\*Assumptions\*\*

1\. \\(V\_Z(r)\\) is smooth and spherically symmetric on \\(\[r\_{\\min}, r\_{\\max}]\\) with \\(r\_{\\min}>0\\).  

2\. A family of covers \\(\\mathcal{U}\_h\\) with mesh \\(h\\to0\\) is available.  

3\. Local bases on each cover element are computed by an adaptive integrator with error \\(e\_{\\mathrm{int}}(h,\\tau)\\to0\\) as \\(h,\\tau\\to0\\).  

4\. The gluing matrix \\(A\_h(Z;\\tau)\\) is assembled from numerical traces; its singular values \\(\\sigma\_{i,h}(Z;\\tau)\\) are well defined.



\*\*Statement\*\*  

Let \\(\\varepsilon(h,\\tau)=\\kappa(h,\\tau)\\,\\sigma\_{\\max,h}(Z;\\tau)\\) with \\(\\kappa(h,\\tau)\\to0\\) as \\(h,\\tau\\to0\\). Then there exist \\(h\_0,\\tau\_0>0\\) such that for all \\(0<h<h\_0\\), \\(0<\\tau<\\tau\_0\\) the numerical proxy





\\\[

C\_h(Z;\\tau)=\\#\\{i:\\ \\sigma\_{i,h}(Z;\\tau)<\\varepsilon(h,\\tau)\\}

\\]





is constant and equals a well‑defined integer \\(C(Z)\\). Thus \\(C\_h(Z;\\tau)\\to C(Z)\\) for \\(h,\\tau\\to0\\).



\*\*Sketch of proof\*\*

\- Numerical errors in local bases vanish as \\(h,\\tau\\to0\\).  

\- Singular values depend continuously on matrix entries; hence \\(\\sigma\_{i,h}\\) converge to limiting values.  

\- If the limiting spectrum has a gap at the threshold index, a relative threshold \\(\\varepsilon(h,\\tau)\\) can be chosen so the count of small singular values is stable.



\*\*Practical remark\*\*

\- At critical transitions (no spectral gap) the proxy may require finer analysis (scaling, extrapolation).



\---



\## Lemma B — Monotonicity of critical charge with nuclear radius (sketch)



\*\*Assumptions\*\*

\- Two nucleus models with radii \\(R\_1<R\_2\\) and otherwise identical charge distribution outside the radius.



\*\*Statement\*\*

\- The critical charge \\(Z\_c(R)\\) (first \\(Z\\) with a bound state at \\(E=-m\\)) is nondecreasing in \\(R\\): \\(Z\_c(R\_1)\\le Z\_c(R\_2)\\).



\*\*Sketch of proof\*\*

\- Increasing \\(R\\) weakens the inner Coulomb attraction; by variational/spectral monotonicity arguments for Dirac operators with monotone potentials, bound states cannot deepen when the potential is weakened. Hence \\(Z\_c\\) cannot decrease.



\*\*Practical remark\*\*

\- Numerical verification: compute \\(Z\_c\\) for a small set of radii and check monotonicity.



\---



