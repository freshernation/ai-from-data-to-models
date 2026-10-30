import warnings

import numpy as np
from sklearn.linear_model import LogisticRegression

from shoplab import customers


class TestPieces:
    def test_sigmoid_values(self, load):
        lg = load("logistic.py")
        assert np.allclose(lg.sigmoid(np.array([0.0, 2.0])), [0.5, 1 / (1 + np.exp(-2))])

    def test_sigmoid_does_not_overflow(self, load):
        lg = load("logistic.py")
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            out = lg.sigmoid(np.array([-1000.0, 1000.0]))
        assert np.allclose(out, [0, 1]), "Large |z| must not warn: use e^z / (1 + e^z) when z < 0."

    def test_log_loss(self, load):
        lg = load("logistic.py")
        assert abs(lg.log_loss([1, 0], [0.8, 0.2]) + np.log(0.8)) < 1e-12
        assert np.isfinite(lg.log_loss([1], [0.0])), "Clip p, or a confident wrong answer is infinite."


def fitted(load):
    lg = load("logistic.py")
    train, test = customers.frozen_split()
    model = lg.LogisticRegressionGD().fit(train[customers.FEATURES], train["churned"])
    return lg, model, train, test


def test_matches_scikit_learn(load):
    lg, model, train, test = fitted(load)
    ref = LogisticRegression(C=1e10, max_iter=10000).fit(train[customers.FEATURES], train["churned"])
    gap = np.abs(model.predict_proba(test[customers.FEATURES])
                 - ref.predict_proba(test[customers.FEATURES])[:, 1]).max()
    assert gap < 1e-3, f"Your probabilities differ from scikit-learn's by up to {gap:.4f}."
    assert set(np.unique(model.predict(test[customers.FEATURES]))) <= {0, 1}


def test_finding_better_than_a_constant_guess(load):
    lg, model, train, test = fitted(load)
    mine = lg.log_loss(test["churned"], model.predict_proba(test[customers.FEATURES]))
    constant = lg.log_loss(test["churned"], np.full(len(test), train["churned"].mean()))
    assert (round(mine, 3), round(constant, 3)) == (0.319, 0.386), \
        "Log loss 0.319 against 0.386 for guessing the training churn rate for everyone."
