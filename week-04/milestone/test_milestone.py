from sklearn.metrics import roc_auc_score

from shoplab import customers


def run(load):
    cm = load("churn_model.py")
    choice, scores = cm.choose(customers.frozen_split()[0])
    return cm, choice, scores


def test_the_choice_is_made_by_cross_validation(load):
    cm, choice, scores = run(load)
    assert set(scores) == {"logistic", "forest", "boosting"}
    assert {k: round(v, 3) for k, v in scores.items()} == \
        {"logistic": 0.835, "forest": 0.813, "boosting": 0.812}
    assert choice == "logistic"


def test_trained_model_saves_loads_and_scores(load, tmp_path):
    cm = load("churn_model.py")
    train_df, test_df = customers.frozen_split()
    name, model = cm.train(train_df)
    path = tmp_path / "m.joblib"
    cm.save(model, path)
    again = cm.load(path)
    auc = roc_auc_score(test_df["churned"], cm.predict_proba(again, test_df))
    assert round(auc, 3) == 0.78, "The reloaded model must score exactly as the one you saved."
    one = cm.predict_one(again, test_df.iloc[0].to_dict())
    assert type(one) is float and 0 <= one <= 1


def test_candidates_are_fresh_each_time(load):
    cm = load("churn_model.py")
    assert cm.candidates()["logistic"] is not cm.candidates()["logistic"], \
        "Build new models on every call, or train() will refit one that choose() already touched."


def test_model_card(source):
    text = source("MODEL_CARD.md")
    assert "<!--" not in text, "Delete the instructions comment in MODEL_CARD.md."
    for heading in ("Intended use", "Data", "How the model was chosen", "Performance",
                    "What drives it", "Limits and risks"):
        assert f"## {heading}" in text, f"MODEL_CARD.md has no '{heading}' section."
        part = text.split(f"## {heading}", 1)[1].split("\n## ")[0]
        assert len(part.split()) >= 50, f"'{heading}' is {len(part.split())} words; write at least 50."
    assert "0.78" in text, "Quote the test AUC."
