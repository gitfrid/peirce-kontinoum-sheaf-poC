#!/usr/bin/env python3
"""
dirac_radial_solver.py

Minimal radial Dirac solver (1s, kappa = -1) Proof-of-Concept.

Features
- Two nucleus models: point (regularized) and homogeneous sphere
- Shooting + bisection eigenvalue search for the 1s state
- Sweep over Z and CSV output
- Simple plotting of E1s(Z)

Notes
- Units: atomic units (a0 = 1, m = 1). Energies converted to eV for output.
- This is a minimal, pedagogical implementation intended for PoC use.
- Extensions (Uehling, Dirac-Fock screening, finer numerics) are left as exercises.
"""

import argparse
import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import bisect

# ---------------------------
# Physical constants & utils
# ---------------------------
alpha = 1.0 / 137.035999139
eV_per_au = 27.211386245988
m_e_eV = 510998.9461  # electron rest energy in eV (approx)
a0_m = 0.529177210903e-10  # Bohr radius in meters


def fm_to_a0(fm: float) -> float:
    return fm * 1e-15 / a0_m


# ---------------------------
# Potentials
# ---------------------------
def V_uniform_sphere(r: float, Z: float, R_a0: float) -> float:
    """Electrostatic potential of a uniformly charged sphere (atomic units)."""
    if r <= 0.0:
        # avoid singularity at r=0
        return -Z * alpha / (1e-12)
    if r <= R_a0:
        R = R_a0
        return -Z * alpha * (3.0 * R * R - r * r) / (2.0 * R**3)
    else:
        return -Z * alpha / r


def V_point_regularized(r: float, Z: float, R_cut: float) -> float:
    """Regularized point nucleus using a tiny sphere of radius R_cut."""
    return V_uniform_sphere(r, Z, R_cut)


# ---------------------------
# Radial Dirac system
# ---------------------------
def dirac_rhs(r: float, y: np.ndarray, E: float, kappa: int, V_func) -> list:
    """
    Right-hand side of the radial Dirac equations for scaled components F = r f, G = r g.
    y = [F, G]
    """
    F, G = y
    # Protect against r=0 in the 1/r terms
    if r == 0.0:
        # use limiting form; kappa/r terms vanish in limit if F,G ~ r
        dF = (1.0 + E - V_func(r)) * G
        dG = (1.0 - E + V_func(r)) * F
    else:
        V = V_func(r)
        dF = - (kappa / r) * F + (1.0 + E - V) * G
        dG =   (kappa / r) * G + (1.0 - E + V) * F
    return [dF, dG]


def init_small_r(r0: float) -> list:
    """
    Initial guess near r -> 0. Normalization is arbitrary for shooting.
    Use small positive powers to ensure regularity.
    """
    F0 = r0**1.0
    G0 = r0**1.0
    return [F0, G0]


# ---------------------------
# Shooting and eigenvalue search
# ---------------------------
def shoot_indicator(E: float, kappa: int, r_min: float, r_max: float, V_func) -> float:
    """
    Integrate outward and return the indicator value (G at r_max).
    The sign of G(r_max) is used to bracket eigenvalues.
    """
    y0 = init_small_r(r_min)
    try:
        sol = solve_ivp(
            fun=lambda r, y: dirac_rhs(r, y, E, kappa, V_func),
            t_span=(r_min, r_max),
            y0=y0,
            t_eval=[r_max],
            method='RK45',
            rtol=1e-8,
            atol=1e-10,
            max_step=1.0
        )
    except Exception:
        return None
    if sol.y.shape[1] == 0:
        return None
    F_end, G_end = sol.y[:, -1]
    return float(G_end)


def find_1s_eigenvalue(kappa: int, r_min: float, r_max: float, V_func) -> float:
    """
    Find the 1s eigenvalue by bisection on E in (-1, 1).
    Returns eigenvalue E (atomic units) or None if not found.
    """
    E_low, E_high = -0.999, 0.9
    f_low = shoot_indicator(E_low, kappa, r_min, r_max, V_func)
    f_high = shoot_indicator(E_high, kappa, r_min, r_max, V_func)
    if f_low is None or f_high is None:
        return None

    # If signs are same, scan to find a bracket
    if np.sign(f_low) == np.sign(f_high):
        Es = np.linspace(E_low, E_high, 80)
        signs = []
        for E in Es:
            val = shoot_indicator(E, kappa, r_min, r_max, V_func)
            signs.append(0 if val is None else np.sign(val))
        bracket_found = False
        for i in range(len(signs) - 1):
            if signs[i] != signs[i + 1] and signs[i] != 0 and signs[i + 1] != 0:
                E_low, E_high = Es[i], Es[i + 1]
                bracket_found = True
                break
        if not bracket_found:
            return None

    try:
        E_root = bisect(
            lambda E: shoot_indicator(E, kappa, r_min, r_max, V_func),
            E_low, E_high, xtol=1e-6, maxiter=60
        )
    except Exception:
        return None
    return float(E_root)


# ---------------------------
# High-level compute functions
# ---------------------------
def compute_E1s(Z: int, model: str = 'sphere', R_fm: float = 5.0, R_cut_au: float = 1e-6, r_max: float = 400.0) -> float:
    """
    Compute the 1s eigenvalue (atomic units) for given Z and nucleus model.
    Returns E (a.u.) or None if not found.
    """
    kappa = -1
    if model == 'sphere':
        R_a0 = fm_to_a0(R_fm)
    else:
        R_a0 = R_cut_au

    r_min = max(1e-6, R_a0 * 1e-3)

    if model == 'sphere':
        V_func = lambda r: V_uniform_sphere(r, Z, R_a0)
    else:
        V_func = lambda r: V_point_regularized(r, Z, R_a0)

    E = find_1s_eigenvalue(kappa, r_min, r_max, V_func)
    return E


def sweep_Z(Z_min: int, Z_max: int, model: str, R_fm: float, out_csv: str, r_max: float = 400.0) -> pd.DataFrame:
    """
    Sweep Z from Z_min to Z_max (inclusive) and write results to CSV.
    Returns pandas DataFrame.
    """
    rows = []
    for Z in range(Z_min, Z_max + 1):
        E = compute_E1s(Z, model=model, R_fm=R_fm, r_max=r_max)
        E_eV = None if E is None else E * eV_per_au
        rows.append({
            'Z': int(Z),
            'E1s_au': None if E is None else float(E),
            'E1s_eV': None if E_eV is None else float(E_eV),
            'model': model,
            'R_param': float(R_fm) if model == 'sphere' else float(R_fm)
        })
        print(f"Z={Z:3d}  E1s_au={rows[-1]['E1s_au']}  E1s_eV={rows[-1]['E1s_eV']}")
    df = pd.DataFrame(rows)
    os.makedirs(os.path.dirname(out_csv) or '.', exist_ok=True)
    df.to_csv(out_csv, index=False)
    return df


def plot_results(dfs: dict, out_png: str):
    """
    Plot E1s (eV) vs Z for provided DataFrames.
    dfs: dict of label -> DataFrame
    """
    plt.figure(figsize=(8, 5))
    for label, df in dfs.items():
        if df is None:
            continue
        plt.plot(df['Z'], df['E1s_eV'], label=label)
    plt.axhline(-m_e_eV, color='k', linestyle='--', label='E = -m c^2 (eV)')
    plt.xlabel('Z')
    plt.ylabel('E1s (eV)')
    plt.legend()
    plt.tight_layout()
    os.makedirs(os.path.dirname(out_png) or '.', exist_ok=True)
    plt.savefig(out_png, dpi=200)
    plt.close()


# ---------------------------
# CLI
# ---------------------------
def main():
    parser = argparse.ArgumentParser(description="Minimal radial Dirac solver (PoC)")
    parser.add_argument('--Z_min', type=int, default=1, help='Minimum Z to sweep')
    parser.add_argument('--Z_max', type=int, default=200, help='Maximum Z to sweep')
    parser.add_argument('--model', choices=['sphere', 'point', 'both'], default='sphere', help='Nucleus model')
    parser.add_argument('--R_fm', type=float, default=5.0, help='Radius in fm for sphere model')
    parser.add_argument('--R_cut_au', type=float, default=1e-6, help='Regularization radius (a0) for point model')
    parser.add_argument('--r_max', type=float, default=400.0, help='Maximum radial integration range (a0)')
    parser.add_argument('--out_dir', type=str, default='data', help='Output directory for CSV and plots')
    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    df_point = None
    df_sphere = None

    if args.model in ('point', 'both'):
        out_csv = os.path.join(args.out_dir, 'E1s_point.csv')
        df_point = sweep_Z(args.Z_min, args.Z_max, model='point', R_fm=args.R_cut_au, out_csv=out_csv, r_max=args.r_max)

    if args.model in ('sphere', 'both'):
        out_csv = os.path.join(args.out_dir, f'E1s_sphere_R{args.R_fm}fm.csv')
        df_sphere = sweep_Z(args.Z_min, args.Z_max, model='sphere', R_fm=args.R_fm, out_csv=out_csv, r_max=args.r_max)

    plot_results({'point (reg)': df_point, f'sphere R={args.R_fm} fm': df_sphere}, out_png=os.path.join('results', 'E1s_vs_Z.png'))
    print("Done. CSV(s) and plot written.")


if __name__ == '__main__':
    main()
