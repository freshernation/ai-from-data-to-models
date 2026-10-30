import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

from shoplab import customers


def pure_noise():
    rng = np.random.default_rng(2)
    return rng.normal(size=(300, 500)), rng.integers(0, 2, 300)


class TestPieces:
    def test_folds(self, load):
        tu = load("tuning.py")
        f = tu.folds(3)
        assert f.get_n_splits() == 5 and f.shuffle and f.random_state == 3

    def test_noise_columns(self, load):
        tu = load("tuning.py")
        out = tu.add_noise_columns(np.ones((4, 2)), n=3)
        assert out.shape == (4, 5) and (out[:, :2] == 1).all()

    def test_cv_auc_returns_mean_and_spread(self, load):
        tu = load("tuning.py")
        train, _ = customers.frozen_split()
        mean, std = tu.cv_auc(Pipeline([("s", StandardScaler()), ("m", SVC())]),
                              train[customers.FEATURES], train["churned"])
        assert round(mean, 3) == 0.691 and 0 < std < 0.1 and type(mean) is float, \
            "A default RBF SVM, untuned: 0.691 - below a plain line. Settings matter."


def test_finding_selection_outside_the_folds_invents_a_signal(load):
    tu = load("tuning.py")
    X, y = pure_noise()
    leaky, honest = tu.leaky_selection_auc(X, y), tu.honest_selection_auc(X, y)
    assert round(leaky, 3) == 0.741, (
        "500 columns of pure noise and a coin-flip label - and cross-validation reports "
        "AUC 0.74, because the columns were chosen by looking at every fold's answers.")
    assert round(honest, 3) == 0.468, "Inside the pipeline: 0.47 - a coin, give or take noise. The truth."


def test_tune_a_forest(load):
    tu = load("tuning.py")
    train, _ = customers.frozen_split()
    params, score, best = tu.tune(
        Pipeline([("model", RandomForestClassifier(n_estimators=200, random_state=0))]),
        {"model__min_samples_leaf": [1, 5, 20], "model__max_features": ["sqrt", None]},
        train[customers.FEATURES], train["churned"])
    assert params == {"model__max_features": "sqrt", "model__min_samples_leaf": 20}
    assert round(score, 3) == 0.811 and hasattr(best, "predict_proba")
