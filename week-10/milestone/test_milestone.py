import numpy as np

from shoplab import reviews


def test_shuffled_keeps_the_words(load):
    cp = load("compare.py")
    out = cp.shuffled(["a b c d", "x y"], seed=1)
    assert sorted(out[0].split()) == ["a", "b", "c", "d"] and sorted(out[1].split()) == ["x", "y"]
    assert cp.shuffled(["a b c d"], seed=1) == cp.shuffled(["a b c d"], seed=1)


def test_finding_three_readers(load):
    cp = load("compare.py")
    r = cp.compare(*reviews.frozen_split())
    line, lstm, tf = r["tfidf line"], r["lstm"], r["transformer"]
    assert round(line["all"], 3) == 0.65 and line["negated"] < 0.1 and line["shuffled"] == line["all"]
    assert (line["params"], lstm["params"], tf["params"]) == (52, 7314, 10306)
    assert lstm["all"] > 0.95 and tf["all"] > 0.95
    assert lstm["shuffled"] < 0.8 < 0.95 < tf["shuffled"], (
        "Shuffle every review's words: the LSTM falls to about 65% - it learned 'not, THEN "
        "an adjective'. The transformer stays near 98%: it learned which words go together.")


def test_results_doc(source):
    text = source("RESULTS.md")
    assert "<!--" not in text, "Delete the instructions comment in RESULTS.md."
    for heading in ("The table", "What each model can and cannot see", "The shuffle test",
                    "What I would use, and when I would change my mind"):
        assert f"## {heading}" in text, f"RESULTS.md has no '{heading}' section."
        part = text.split(f"## {heading}", 1)[1].split("\n## ")[0]
        assert len(part.split()) >= 50, f"'{heading}' is {len(part.split())} words; write at least 50."
