import math

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler

from shoplab import customers

F = customers.FEATURES


def line():
    train, test = customers.frozen_split()
    scaler = StandardScaler().fit(train[F])
    model = LogisticRegression(max_iter=2000).fit(scaler.transform(train[F]), train["churned"])
    return scaler, model, train, test


def test_psi_basics(load):
    mo = load("monitor.py")
    rng = np.random.default_rng(0)
    a = rng.normal(size=5000)
    assert mo.psi(a, a) == 0.0
    assert mo.psi(a, a + 1) > 0.25
    assert [mo.verdict(s) for s in (0.05, 0.2, 0.3)] == ["stable", "watch", "drifted"]


def test_finding_the_email_moved_one_column(load):
    mo = load("monitor.py")
    train, test = customers.frozen_split()
    nm = customers.next_month()
    report = mo.drift_report(train, nm, F)
    assert list(report)[0] == "days_since_last_order" and report["days_since_last_order"] == 0.516, (
        "A reminder email went to silent customers and 70% placed a small order: "
        "days_since_last_order shifted (PSI 0.52). Every other column is below 0.03.")
    assert max(mo.drift_report(train, test, F).values()) < 0.1, "Last month's test set: stable."
    scaler, model, _, _ = line()
    p = lambda df: model.predict_proba(scaler.transform(df[F]))[:, 1]
    flagged = lambda df: (p(df) >= 0.1)[df["churned"].to_numpy() == 1].mean()
    assert round(flagged(test), 2) == 0.72 and round(flagged(nm), 2) == 0.49, (
        "And the model now misses leavers: recall at 0.10 falls from 72% to 49%, while "
        "the churn rate barely moved. The email changed the feature, not who leaves.")


def test_finding_a_fairness_number_from_one_person(load):
    mo = load("monitor.py")
    scaler, model, _, test = line()
    p = model.predict_proba(scaler.transform(test[F]))[:, 1]
    by_plan = mo.recall_by_group(test["churned"], p, test["plan"], 0.1)
    assert by_plan["pro"] == 0.0 and (test[test["churned"] == 1]["plan"] == "pro").sum() == 1, (
        "Pro customers: 0% recall - from ONE pro leaver in the test set. Report the count "
        "beside every group's number, or the number means nothing.")
    assert math.isnan(mo.recall_by_group([0, 1], [0.9, 0.9], ["a", "b"], 0.5)["a"])


def test_contributions_explain_one_customer(load):
    mo = load("monitor.py")
    scaler, model, _, test = line()
    row = test.iloc[0].to_dict()
    parts = mo.contributions(scaler, model, F, row)
    assert list(parts)[0] == "days_since_last_order"
    z = scaler.transform(test[F].iloc[[0]])[0] @ model.coef_[0] + model.intercept_[0]
    assert abs(sum(parts.values()) + model.intercept_[0] - z) < 0.01, \
        "The parts add up to the score: this explanation is exact for a line."
