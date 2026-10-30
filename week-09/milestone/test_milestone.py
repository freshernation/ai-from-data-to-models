import numpy as np
import pandas as pd

from shoplab import reviews


def test_breakdown_and_errors_by_hand(load):
    se = load("sentiment.py")
    df = pd.DataFrame({"review_id": ["a", "b", "c", "d"],
                       "text": ["good !", "not bad", "not really bad", "bad"],
                       "positive": [1, 1, 1, 0], "negated": [0, 1, 1, 0]})
    pred = np.array([1, 1, 0, 1])
    assert se.breakdown(pred, df) == {"all": 0.5, "plain": 0.5, "near negation": 1.0, "far negation": 0.0}
    assert se.errors(pred, df)["review_id"].tolist() == ["c", "d"]
    assert list(se.errors(pred, df).columns) == ["review_id", "text", "positive"]


def test_finding_most_mistakes_are_the_labels(load):
    se = load("sentiment.py")
    em = load("embeddings.py")
    train, test = reviews.frozen_split()
    model, vocab = se.train(train)
    pred = em.predict(model, test["text"], vocab)
    b = se.breakdown(pred, test)
    assert b["all"] > 0.95 and b["far negation"] > 0.9
    wrong = se.errors(pred, test)
    assert 5 <= len(wrong) <= 50, "About 18 mistakes in the reference run."


def test_errors_doc(source):
    text = source("ERRORS.md")
    assert "<!--" not in text, "Delete the instructions comment in ERRORS.md."
    for heading in ("The numbers", "What the mistakes have in common",
                    "Which mistakes are the model's fault", "What I would do next"):
        assert f"## {heading}" in text, f"ERRORS.md has no '{heading}' section."
        part = text.split(f"## {heading}", 1)[1].split("\n## ")[0]
        assert len(part.split()) >= 50, f"'{heading}' is {len(part.split())} words; write at least 50."
    assert "label" in text.lower(), "Did you check whether the labels were right?"
