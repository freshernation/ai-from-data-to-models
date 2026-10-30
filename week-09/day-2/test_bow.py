import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from shoplab import reviews


def test_counts(load):
    bow = load("bow.py")
    v = bow.word_vocab(["not bad", "bad bad"])
    assert v == {"bad": 0, "not": 1}
    assert bow.count_matrix(["not bad", "bad bad", "great"], v).tolist() == [[1, 1], [2, 0], [0, 0]]


def test_tfidf_matches_scikit_learn(load):
    bow = load("bow.py")
    tx = load("text.py")
    train, test = reviews.frozen_split()
    v = bow.word_vocab(train["text"])
    counts = bow.count_matrix(train["text"], v)
    mine = bow.tfidf(bow.count_matrix(test["text"], v), bow.idf(counts))
    ref = TfidfVectorizer(tokenizer=tx.tokenize, lowercase=False, token_pattern=None).fit(train["text"])
    assert np.allclose(mine, ref.transform(test["text"]).toarray())


def test_finding_word_counts_read_not_bad_as_bad(load):
    bow = load("bow.py")
    train, test = reviews.frozen_split()
    vocab, weights, model = bow.fit_sentiment(train["text"], train["positive"])
    s = bow.scores(test["positive"], bow.predict(vocab, weights, model, test["text"]), test["negated"])
    assert round(s["plain"], 3) == 0.986, "On reviews with no negation: 98.6%."
    assert round(s["negated"], 3) == 0.026, (
        "On negated reviews: 2.6% - worse than a coin. 'Not bad at all' is mostly the "
        "word 'bad' to a model that cannot see order.")
    assert round(s["all"], 3) == 0.65
