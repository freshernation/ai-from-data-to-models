import numpy as np
from sklearn.linear_model import LinearRegression

from shoplab import customers

COLS = ["orders_90d", "tenure_months", "days_since_last_order"]


def fitted(load):
    lr = load("linreg.py")
    train, test = customers.frozen_split()
    return lr.LinearRegressionGD().fit(train[COLS], train["monthly_spend"]), train, test


def test_matches_scikit_learn(load):
    model, train, test = fitted(load)
    ref = LinearRegression().fit(train[COLS], train["monthly_spend"])
    assert np.allclose(model.coef_, ref.coef_, atol=1e-3), \
        "Weights must be converted back to original units: coef_ = w / std."
    assert abs(model.intercept_ - ref.intercept_) < 1e-3
    assert type(model.intercept_) is float


def test_fit_returns_self_and_predicts(load):
    model, _, test = fitted(load)
    assert model.predict(test[COLS]).shape == (500,)
    assert model.steps_taken_ < 5000, "With standardising, it should stop long before 5000 steps."


def test_finding_held_out_r_squared(load):
    model, _, test = fitted(load)
    assert round(model.score(test[COLS], test["monthly_spend"]), 3) == 0.760, \
        "Three columns explain 76% of the variation in spend on customers the model never saw."


def test_notes(source):
    text = source("MATHS_NOTES.md")
    assert "<!--" not in text, "Delete the instructions comment in MATHS_NOTES.md."
    for heading in ("What a gradient is", "Why the learning rate matters",
                    "What a 90% alarm is worth", "Why the slope is not 4.5"):
        assert f"## {heading}" in text, f"MATHS_NOTES.md has no '{heading}' section."
        part = text.split(f"## {heading}", 1)[1].split("\n## ")[0]
        assert len(part.split()) >= 50, f"'{heading}' is {len(part.split())} words; write at least 50."
        assert any(ch.isdigit() for ch in part), f"'{heading}' needs a number you computed."
