import numpy as np


def setup(load):
    bp = load("backprop.py")
    fw = load("forward.py")
    rng = np.random.default_rng(0)
    X, y = rng.normal(size=(5, 3)), np.array([0, 1, 2, 1, 0])
    params = fw.init_params(3, 4, 3, seed=1)
    probs, cache = fw.forward(params, X)
    return bp, params, X, y, bp.backward(params, cache, y)


def test_shapes(load):
    bp, params, X, y, grads = setup(load)
    assert {k: v.shape for k, v in grads.items()} == {k: v.shape for k, v in params.items()}


def test_numerical_gradient_puts_everything_back(load):
    bp, params, X, y, _ = setup(load)
    before = {k: v.copy() for k, v in params.items()}
    bp.numerical_gradient(params, X, y, "W1")
    assert all((params[k] == before[k]).all() for k in params), "Restore each entry after nudging it."


def test_finding_the_gradient_is_right_to_eleven_places(load):
    bp, params, X, y, grads = setup(load)
    for name in ("W1", "b1", "W2", "b2"):
        err = bp.relative_error(grads[name], bp.numerical_gradient(params, X, y, name))
        assert err < 1e-9, (
            f"{name}: relative error {err:.1e}. A correct backprop agrees with the finite "
            "difference to about 1e-11. Check that dz1 is zeroed where z1 <= 0, and the 1/n.")
