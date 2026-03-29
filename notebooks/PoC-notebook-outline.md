\# PoC Notebook Outline (use to create PoC.ipynb)



This file lists the notebook cells and code to paste into a new Jupyter notebook.



\## Cell 1 — Title and short description (Markdown)

Peirce Continuum PoC — Demo notebook

Short description and quick instructions.



\## Cell 2 — Imports (Code)

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from src.dirac\_radial\_solver import compute\_E1s, sweep\_Z



\## Cell 3 — Run a small sweep (Code)

\# Example: run Z=100..200 for sphere model (coarse)

df = sweep\_Z(100, 200, model='sphere', R\_fm=5.0, out\_csv='data/E1s\_sphere\_R5fm.csv', r\_max=300.0)

df.head()



\## Cell 4 — Plot (Code)

plt.figure(figsize=(8,5))

plt.plot(df\['Z'], df\['E1s\_eV'], label='sphere R=5 fm')

plt.axhline(-510998.9461, color='k', linestyle='--', label='E = -m c^2 (eV)')

plt.xlabel('Z')

plt.ylabel('E1s (eV)')

plt.legend()

plt.show()



\## Cell 5 — Table for selected Z (Code)

sel = df\[df\['Z'].isin(\[100,137,170,180,200])]

sel



\## Cell 6 — Short interpretation (Markdown)

Summarize what the plot shows and next steps (Uehling, DF, finer Z).



