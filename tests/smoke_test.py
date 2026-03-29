def test_smoke_runs():
    from src.dirac_radial_solver import compute_E1s
    # basic smoke checks: function returns a numeric energy
    e1_1 = compute_E1s(1, model='sphere', R_fm=2.5, r_max=200.0)
    e1_50 = compute_E1s(50, model='sphere', R_fm=5.0, r_max=300.0)
    assert e1_1 is not None
    assert e1_50 is not None
