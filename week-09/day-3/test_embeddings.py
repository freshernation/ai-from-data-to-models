import torch

from shoplab import reviews

POS = ["great", "good", "excellent", "lovely", "perfect", "sturdy", "comfortable", "beautiful"]
NEG = ["bad", "terrible", "awful", "poor", "flimsy", "broken", "cheap", "useless"]


def test_mean_ignores_padding(load):
    em = load("embeddings.py")
    torch.manual_seed(0)
    model = em.MeanEmbedding(5, dim=4)
    a = model(torch.tensor([[2, 3]]))
    b = model(torch.tensor([[2, 3, 0, 0, 0]]))
    assert torch.allclose(a, b), "Padding must not change the average."


def test_tensorise_and_mask(load):
    em = load("embeddings.py")
    v = {"<pad>": 0, "<unk>": 1, "not": 2, "bad": 3}
    assert em.tensorise(["not bad", "bad"], v).tolist() == [[2, 3], [3, 0]]
    assert em.split_validation(10).sum() == 2


def trained(em, tx):
    train, test = reviews.frozen_split()
    v = tx.build_vocab(train["text"])
    torch.manual_seed(0)
    model = em.MeanEmbedding(len(v))
    em.train_text_model(model, train["text"], train["positive"], v)
    return model, v, test


def test_finding_it_learned_what_words_mean_but_not_what_not_does(load):
    em = load("embeddings.py")
    tx = load("text.py")
    model, v, test = trained(em, tx)
    s = em.sentiment_scores(model, v)
    assert min(s[w] for w in POS) > 0 > max(s[w] for w in NEG), \
        "Nobody told it which words are positive. Every positive adjective ended up on one side."
    assert s["not"] > 0, (
        "And 'not' ended up mildly POSITIVE: it mostly appears in 'not bad', 'not awful'. "
        "An average cannot know what 'not' is next to.")
    accuracy = (em.predict(model, test["text"], v) == test["positive"].to_numpy()).mean()
    assert accuracy < 0.75, "So it fails negation just like the word counts did (about 65%)."
    assert len(em.nearest(model, v, "great")) == 5
