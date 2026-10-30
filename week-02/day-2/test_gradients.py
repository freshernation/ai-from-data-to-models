import numpy as np


class TestDerivatives:
    def test_slope_of_a_cube(self, load):
        g = load("gradients.py")
        assert abs(g.numerical_derivative(lambda x: x**3, 2.0) - 12.0) < 1e-6

    def test_mse(self, load):
        g = load("gradients.py")
        assert g.mse([1, 2, 3], [1, 2, 5]) == 4 / 3

    def test_mse_gradient_agrees_with_finite_differences(self, load):
        g = load("gradients.py")
        rng = np.random.default_rng(0)
        X, y = rng.normal(size=(20, 3)), rng.normal(size=20)
        w, b = rng.normal(size=3), 0.4
        dw, db = g.mse_gradient(X, y, w, b)
        for i in range(3):
            def f(v, i=i):
                w2 = w.copy(); w2[i] = v
                return g.mse(y, X @ w2 + b)
            assert abs(dw[i] - g.numerical_derivative(f, w[i])) < 1e-6, \
                f"dw[{i}] disagrees with the finite difference. Check the 2/n and the sign of error."
        assert abs(db - g.numerical_derivative(lambda v: g.mse(y, X @ w + v), b)) < 1e-6


class TestDescent:
    def test_history_length_and_start(self, load):
        g = load("gradients.py")
        xs = g.descend(lambda x: 2 * x, 1.0, 0.1, 5)
        assert len(xs) == 6 and xs[0] == 1.0 and abs(xs[1] - 0.8) < 1e-12


def test_finding_the_learning_rate_decides_everything(load):
    g = load("gradients.py")
    final = {lr: g.descend(lambda x: 2 * x, 1.0, lr, 20)[-1] for lr in (0.1, 1.0, 1.1)}
    assert abs(final[0.1] - 0.0115) < 1e-4, "lr 0.1: twenty steps get within 0.012 of the bottom."
    assert final[1.0] == 1.0, "lr 1.0: every step jumps to the other side, forever (1, -1, 1, ...)."
    assert abs(final[1.1] - 38.34) < 0.01, "lr 1.1: each step overshoots further - 38 after 20 steps."
