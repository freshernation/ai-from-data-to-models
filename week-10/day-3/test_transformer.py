import numpy as np
import torch

from shoplab import reviews


def test_shapes_and_padding(load):
    tf = load("transformer.py")
    torch.manual_seed(0)
    model = tf.TinyTransformer(10).eval()
    assert sum(p.numel() for p in model.parameters()) == 10 * 32 + 8610
    a, b = model(torch.tensor([[2, 3, 4]])), model(torch.tensor([[2, 3, 4, 0, 0]]))
    assert torch.allclose(a, b, atol=1e-5), "Padding must be masked out and left out of the mean."
    assert tf.sinusoidal(3, 4).dtype == torch.float32


def test_without_position_order_cannot_matter(load):
    tf = load("transformer.py")
    torch.manual_seed(0)
    model = tf.TinyTransformer(10, use_position=False).eval()
    assert torch.allclose(model(torch.tensor([[2, 3, 4, 5]])), model(torch.tensor([[5, 4, 3, 2]])), atol=1e-5)


def test_finding_this_data_needs_combinations_not_order(load):
    tf = load("transformer.py")
    em = load("embeddings.py")
    tx = load("text.py")
    train, test = reviews.frozen_split()
    v = tx.build_vocab(train["text"])
    y = test["positive"].to_numpy()
    for use_position in (True, False):
        torch.manual_seed(0)
        model = tf.TinyTransformer(len(v), use_position=use_position)
        em.train_text_model(model, train["text"], train["positive"], v, lr=0.005)
        accuracy = (em.predict(model, test["text"], v) == y).mean()
        assert accuracy > 0.95, (
            f"use_position={use_position}: about 98% either way. In these reviews the label "
            "depends on WHICH words appear together - 'not' with 'bad' - never on their order. "
            "The word-count line failed because it could only add words, not combine them.")
