import numpy as np
from sklearn.linear_model import LogisticRegression

from shoplab import customers


class TestValue:
    def test_value_by_hand(self, load):
        th = load("thresholds.py")
        y, s = [1, 0, 1, 0], [0.9, 0.8, 0.3, 0.1]
        assert th.value(y, s, 0.5) == 1 * 0.3 * 200 - 2 * 10
        assert th.value(y, s, 0.99) == 0.0

    def test_best_threshold(self, load):
        th = load("thresholds.py")
        t, v = th.best_threshold([1, 0, 1, 0], [0.9, 0.8, 0.3, 0.1])
        assert (t, v) == (0.15, 90.0), "From 0.15 the top three are flagged: two saves (120) minus three offers (30)."


def test_finding_the_best_threshold_is_far_below_a_half(load):
    th = load("thresholds.py")
    train, test = customers.frozen_split()
    F = customers.FEATURES
    model = LogisticRegression(C=1e10, max_iter=10000).fit(train[F], train["churned"])
    t, _ = th.best_threshold(train["churned"], model.predict_proba(train[F])[:, 1])
    p = model.predict_proba(test[F])[:, 1]
    assert t == 0.1, "Chosen on TRAINING data: 0.10. An offer costs 10; a saved customer is worth 60."
    assert th.value(test["churned"], p, 0.5) == 810.0
    assert th.value(test["churned"], p, t) == 1090.0, (
        "On the test set, 0.10 makes 1,090 against 810 at 0.5 - while accuracy falls "
        "from 88.8% to 71.2%. The right threshold is a business decision.")
