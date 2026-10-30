import numpy as np

from shoplab import customers

COLS = ["orders_90d", "tenure_months"]


def data():
    df = customers.load()
    return df[COLS].to_numpy(dtype=float), df["monthly_spend"].to_numpy()


class TestPieces:
    def test_bias(self, load):
        r = load("regression.py")
        assert r.add_bias([[2], [3]]).tolist() == [[1, 2], [1, 3]]

    def test_normal_equation_recovers_a_known_line(self, load):
        r = load("regression.py")
        X = np.arange(10.0).reshape(-1, 1)
        w, b = r.normal_equation(X, 3 * X[:, 0] + 2)
        assert np.allclose(w, [3]) and abs(b - 2) < 1e-9

    def test_standardise(self, load):
        r = load("regression.py")
        Xs, mu, sd = r.standardise([[1.0, 10.0], [3.0, 30.0]])
        assert np.allclose(Xs, [[-1, -1], [1, 1]]) and np.allclose(mu, [2, 20])

    def test_descent_reaches_the_exact_answer(self, load):
        r = load("regression.py")
        X, y = data()
        Xs, mu, sd = r.standardise(X)
        w, b, _ = r.gradient_descent(Xs, y, lr=0.1, steps=5000, tol=1e-8)
        w_exact, b_exact = r.normal_equation(Xs, y)
        assert np.allclose(w, w_exact, atol=1e-6) and abs(b - b_exact) < 1e-6


def test_finding_scale_costs_a_thousand_times_the_steps(load):
    r = load("regression.py")
    X, y = data()
    w, b, raw_steps = r.gradient_descent(X, y, lr=0.0005, steps=70000, tol=1e-3)
    _, _, blown = r.gradient_descent(X, y, lr=0.001, steps=70000, tol=1e-3)
    Xs, _, _ = r.standardise(X)
    _, _, scaled_steps = r.gradient_descent(Xs, y, lr=0.1, steps=70000, tol=1e-3)
    assert not np.isfinite(r.gradient_descent(X, y, lr=0.001, steps=blown)[0]).all(), \
        "Unscaled, lr 0.001 already diverges: tenure (up to 60) dwarfs orders (around 3)."
    assert raw_steps == 58384, "Unscaled at lr 0.0005: 58,384 steps."
    assert scaled_steps == 52, "Standardised at lr 0.1: 52 steps, to the same answer."
