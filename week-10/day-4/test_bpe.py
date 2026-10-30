from collections import Counter

from shoplab import reviews


def test_pieces(load):
    bp = load("bpe.py")
    assert bp.split_word("mug") == ("m", "u", "g", "_")
    assert bp.merge(("a", "a", "a"), ("a", "a")) == ("aa", "a")
    counts = bp.pair_counts(Counter({("a", "b", "_"): 3, ("b", "_"): 1}))
    assert counts == Counter({("a", "b"): 3, ("b", "_"): 4})


def test_learn_and_segment(load):
    bp = load("bpe.py")
    merges = bp.learn_merges({"low": 5, "lower": 2, "newest": 6, "widest": 3}, 4)
    assert merges == [("t", "_"), ("s", "t_"), ("e", "st_"), ("o", "w")], (
        "'s t', 'e s' and 't _' all appear 9 times; the tie goes to the largest pair, ('t', '_').")
    assert bp.segment("lowest", merges) == ["l", "ow", "est_"]


def corpus(tx):
    train, _ = reviews.frozen_split()
    return Counter(t for text in train["text"] for t in tx.tokenize(text))


def test_finding_no_word_is_unknown_any_more(load):
    bp = load("bpe.py")
    tx = load("text.py")
    words = corpus(tx)
    per_word = {}
    for n in (0, 60, 200):
        merges = bp.learn_merges(words, n)
        per_word[n] = round(sum(len(bp.segment(w, merges)) * c for w, c in words.items())
                            / sum(words.values()), 2)
    assert per_word == {0: 5.38, 60: 2.43, 200: 1.0}, (
        "No merges: 5.4 symbols per word. Sixty merges: 2.4. Two hundred: every word is "
        "one token. The number of merges trades sequence length against vocabulary size.")
    merges = bp.learn_merges(words, 60)
    assert bp.segment("unbreakable", merges) == ["u", "n", "b", "rea", "k", "a", "ble_"], (
        "A word never seen in a review still splits into known pieces - no <unk>. That is "
        "why every modern language model uses subwords.")
