from shoplab import customers


def run(load):
    churn = load("churn_v1.py")
    train_df, test_df = customers.frozen_split()
    model, threshold = churn.train(train_df)
    return churn, model, threshold, churn.evaluate(model, threshold, test_df)


def test_threshold_is_chosen_on_training_data(load):
    _, _, threshold, _ = run(load)
    assert threshold == 0.1


def test_report_has_every_number(load):
    _, _, _, r = run(load)
    for key in ("accuracy", "baseline", "precision", "recall", "auc", "value", "value_at_half"):
        assert type(r[key]) is float, f"report['{key}'] should be a plain float."
    assert r["confusion"] == {"tp": 47, "fp": 126, "tn": 309, "fn": 18}


def test_finding_worse_accuracy_more_money(load):
    _, _, _, r = run(load)
    assert (round(r["accuracy"], 3), r["baseline"]) == (0.712, 0.87), \
        "Below the baseline on accuracy - and that is fine. See the next line."
    assert (r["value"], r["value_at_half"]) == (1090.0, 810.0)
    assert round(r["recall"], 3) == 0.723 and round(r["auc"], 3) == 0.779


def test_eval(source):
    text = source("EVAL.md")
    assert "<!--" not in text, "Delete the instructions comment in EVAL.md."
    for heading in ("What the model does", "How it was tested", "The numbers, beside the baseline",
                    "Why the threshold is not 0.5", "What would make me distrust it"):
        assert f"## {heading}" in text, f"EVAL.md has no '{heading}' section."
        part = text.split(f"## {heading}", 1)[1].split("\n## ")[0]
        assert len(part.split()) >= 50, f"'{heading}' is {len(part.split())} words; write at least 50."
    assert "1,090" in text or "1090" in text, "Quote the value your threshold makes."
