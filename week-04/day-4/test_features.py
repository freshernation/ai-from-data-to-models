import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from shoplab import customers


def test_add_features(load):
    fe = load("features.py")
    df = pd.DataFrame({"monthly_spend": [30.0], "orders_90d": [2], "plan": ["basic"],
                       "days_since_last_order": [60]})
    out = fe.add_features(df)
    assert out.loc[0, "spend_per_order"] == 10.0
    assert (out.loc[0, "on_basic"], out.loc[0, "on_pro"], out.loc[0, "silent_60"]) == (1, 0, 1)
    assert "spend_per_order" not in df.columns, "Return a copy."


def test_finding_one_column_carries_the_model(load):
    fe = load("features.py")
    train, test = customers.frozen_split()
    F = customers.FEATURES + fe.ENGINEERED
    tr, te = fe.add_features(train), fe.add_features(test)
    boost = GradientBoostingClassifier(n_estimators=150, max_depth=2, learning_rate=0.05,
                                       random_state=0).fit(tr[F], train["churned"])
    drops = fe.permutation_importance(boost, te[F], test["churned"])
    assert drops.index[0] == "days_since_last_order" and round(drops.iloc[0], 3) == 0.139, \
        "Shuffle days-since-last-order and AUC falls by 0.139: more than all the others together."
    assert drops["silent_60"] == 0.0, \
        "Your engineered 'silent_60' adds nothing: the trees already split on the raw column."
    line = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
    before = roc_auc_score(test["churned"], line.fit(train[customers.FEATURES], train["churned"])
                           .predict_proba(test[customers.FEATURES])[:, 1])
    after = roc_auc_score(test["churned"], line.fit(tr[F], train["churned"]).predict_proba(te[F])[:, 1])
    assert (round(before, 3), round(after, 3)) == (0.779, 0.78), \
        "Four new features move the line from 0.779 to 0.780. Features are cheap; evidence is not."
