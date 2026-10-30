import torch

from shoplab import reviews

FAR = r"not (?:really|very|that) "


def test_reads_the_last_real_token(load):
    ls = load("lstm.py")
    torch.manual_seed(0)
    model = ls.LSTMClassifier(6).eval()
    a = model(torch.tensor([[2, 3, 4]]))
    b = model(torch.tensor([[2, 3, 4, 0, 0]]))
    assert torch.allclose(a, b, atol=1e-6), \
        "Padding at the end must not change the answer: read the output at the last real token."


def test_finding_order_fixes_negation(load):
    ls = load("lstm.py")
    em = load("embeddings.py")
    tx = load("text.py")
    train, test = reviews.frozen_split()
    v = tx.build_vocab(train["text"])
    torch.manual_seed(0)
    model = ls.LSTMClassifier(len(v))
    em.train_text_model(model, train["text"], train["positive"], v)
    right = em.predict(model, test["text"], v) == test["positive"].to_numpy()
    far = test["text"].str.contains(FAR).to_numpy()
    negated = test["negated"].to_numpy() == 1
    assert right.mean() > 0.95 and right[negated].mean() > 0.95, (
        "Reading in order: about 98% overall, and about 98% on negated reviews - against "
        "2.6% for the word counts.")
    assert right[far].mean() > 0.9, \
        "Even 'not really excellent', where 'not' is two words from its adjective: about 97%."
