from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from shoplab import customers


def data():
    train, test = customers.frozen_split()
    F = customers.FEATURES
    return train[F], train["churned"], test[F], test["churned"]


def test_auc_is_a_float(load):
    en = load("ensembles.py")
    X, y, _, _ = data()
    model = LogisticRegression(max_iter=2000).fit(X, y)
    assert type(en.auc(model, X, y)) is float


def test_finding_a_deep_tree_memorises(load):
    en = load("ensembles.py")
    rows = {d: (round(a, 3), round(b, 3)) for d, a, b in en.depth_curve(*data())}
    assert rows[None][0] == 1.0, "Unlimited depth: a perfect score on the customers it memorised."
    assert rows[5][1] == 0.691 and rows[None][1] == 0.653, (
        "On new customers it peaks at depth 5 (0.691) and falls back to 0.653 unlimited. "
        "The gap between the columns is overfitting, measured.")


def test_finding_the_line_is_hard_to_beat(load):
    en = load("ensembles.py")
    X, y, Xt, yt = data()
    forest, boost = en.fit_forest(X, y), en.fit_boosting(X, y)
    line = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000)).fit(X, y)
    assert round(en.auc(forest, X, y), 3) == 0.968 and round(en.auc(forest, Xt, yt), 3) == 0.765
    assert round(en.auc(boost, Xt, yt), 3) == 0.777
    assert en.auc(line, Xt, yt) > en.auc(boost, Xt, yt), (
        "Week 3's logistic regression (0.779) beats both ensembles here. Trees are the "
        "strongest tabular models in general - not on every table. Tomorrow: how to find "
        "out without touching the test set.")
