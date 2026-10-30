import numpy as np

from shoplab import reviews


def test_counts(load):
    g = load("generate.py")
    vocab, counts = g.fit_bigram(["not bad", "not good"])
    assert vocab == ["<s>", "</s>", "bad", "good", "not"]
    i = {w: k for k, w in enumerate(vocab)}
    assert counts[i["<s>"], i["not"]] == 2 and counts[i["not"], i["bad"]] == 1
    assert counts[i["good"], i["</s>"]] == 1 and counts.sum() == 6


def test_temperature_and_top_k(load):
    g = load("generate.py")
    counts = np.array([[0.0, 3.0, 1.0]])
    assert np.allclose(g.next_probs(counts, 0), [0, 0.75, 0.25], atol=1e-9)
    assert np.allclose(g.next_probs(counts, 0, top_k=1), [0, 1, 0])
    cold, hot = g.next_probs(counts, 0, 0.5), g.next_probs(counts, 0, 2.0)
    assert cold[1] > 0.75 > hot[1], "Low temperature sharpens the distribution; high flattens it."


def test_finding_greedy_is_boring_sampling_copies(load):
    g = load("generate.py")
    train, _ = reviews.frozen_split()
    greedy = g.survey(train["text"], top_k=1)
    assert greedy["distinct"] == 0.005 and greedy["copied"] == 0.0, (
        "Always taking the likeliest word: 200 samples, ONE sentence - "
        "'arrived on time this shop honestly not very terrible' - and not a real review.")
    warm = g.survey(train["text"], temperature=1.0)
    assert (warm["distinct"], warm["copied"]) == (0.97, 0.31), \
        "Sampling at temperature 1: 97% different from each other, and 31% copied word for word."
    hot = g.survey(train["text"], temperature=1.5)
    assert hot["copied"] < warm["copied"], "Hotter: fewer copies, and odder sentences."
