from shoplab import reviews


def test_clean_and_tokenize(load):
    tx = load("text.py")
    assert tx.clean("Not BAD!! at   all.") == "not bad at all"
    assert tx.tokenize("I bought this last week . the lamp is not excellent !") == \
        ["i", "bought", "this", "last", "week", "the", "lamp", "is", "not", "excellent"]


def test_vocab_order(load):
    tx = load("text.py")
    v = tx.build_vocab(["b a", "a c", "a b"])
    assert v == {"<pad>": 0, "<unk>": 1, "a": 2, "b": 3, "c": 4}
    assert tx.build_vocab(["a a b"], min_count=2) == {"<pad>": 0, "<unk>": 1, "a": 2}


def test_encode_and_pad(load):
    tx = load("text.py")
    v = {"<pad>": 0, "<unk>": 1, "not": 2, "bad": 3}
    assert tx.encode("Not bad, honestly!", v) == [2, 3, 1]
    assert tx.pad([[2, 3, 1], [2]]) == [[2, 3, 1], [2, 0, 0]]
    assert tx.pad([[2, 3, 1]], length=2) == [[2, 3]]


def test_finding_the_shop_speaks_fifty_words(load):
    tx = load("text.py")
    train, _ = reviews.frozen_split()
    v = tx.build_vocab(train["text"])
    assert len(v) == 53 and list(v)[2:6] == ["this", "is", "not", "honestly"], (
        "Three thousand reviews, 51 distinct words - real reviews have tens of thousands. "
        "And 'not' is the third most common word: a model that ignores it ignores a lot.")
