import numpy as np
from sklearn.metrics import roc_auc_score

from shoplab import customers

Y = [1, 1, 0, 0, 0, 1]
YH = [1, 0, 0, 1, 0, 1]


class TestCounts:
    def test_confusion(self, load):
        m = load("metrics.py")
        assert m.confusion(Y, YH) == {"tp": 2, "fp": 1, "tn": 2, "fn": 1}

    def test_precision_recall_f1(self, load):
        m = load("metrics.py")
        assert m.precision(Y, YH) == 2 / 3 and m.recall(Y, YH) == 2 / 3
        assert abs(m.f1(Y, YH) - 2 / 3) < 1e-12

    def test_nobody_flagged_is_zero_not_a_crash(self, load):
        m = load("metrics.py")
        assert m.precision([1, 0], [0, 0]) == 0.0 and m.f1([1, 0], [0, 0]) == 0.0


class TestAUC:
    def test_matches_scikit_learn_with_ties(self, load):
        m = load("metrics.py")
        y, s = [0, 0, 1, 1, 1, 0], [0.1, 0.4, 0.35, 0.8, 0.4, 0.2]
        assert abs(m.roc_auc(y, s) - roc_auc_score(y, s)) < 1e-12

    def test_by_hand(self, load, source):
        m = load("metrics.py")
        assert m.roc_auc([0, 1], [0.2, 0.9]) == 1.0
        assert "sklearn" not in source("metrics.py", code_only=True)


def test_finding_accuracy_moves_two_points_recall_tells_the_truth(load):
    from sklearn.linear_model import LogisticRegression
    m = load("metrics.py")
    train, test = customers.frozen_split()
    F = customers.FEATURES
    p = LogisticRegression(C=1e10, max_iter=10000).fit(train[F], train["churned"]).predict_proba(test[F])[:, 1]
    y, y_hat = test["churned"].to_numpy(), (p >= 0.5).astype(int)
    assert m.confusion(y, y_hat) == {"tp": 18, "fp": 9, "tn": 426, "fn": 47}, (
        "88.8% accurate against an 87.0% baseline looks fine - but it catches 18 of 65 "
        "leavers. Recall 27.7%.")
    assert round(m.recall(y, y_hat), 3) == 0.277 and round(m.roc_auc(y, p), 3) == 0.779
