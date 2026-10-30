import numpy as np
import torch
import torch.nn.functional as F


def qkv(seed=0):
    rng = np.random.default_rng(seed)
    return [rng.normal(size=(2, 5, 8)) for _ in range(3)]


def test_one_query_one_key(load):
    at = load("attention.py")
    out, w = at.attention(np.array([[1.0]]), np.array([[3.0]]), np.array([[7.0, 9.0]]))
    assert w.tolist() == [[1.0]] and out.tolist() == [[7.0, 9.0]], "One key: all the weight goes to it."


def test_weights_are_a_distribution(load):
    at = load("attention.py")
    _, w = at.attention(*qkv())
    assert w.shape == (2, 5, 5) and np.allclose(w.sum(-1), 1) and (w >= 0).all()


def test_matches_pytorch(load):
    at = load("attention.py")
    Q, K, V = qkv()
    ref = F.scaled_dot_product_attention(*(torch.tensor(a) for a in (Q, K, V))).numpy()
    assert np.allclose(at.attention(Q, K, V)[0], ref)


def test_finding_a_mask_decides_what_can_be_seen(load):
    at = load("attention.py")
    Q, K, V = qkv()
    mask = np.tril(np.ones((5, 5), dtype=bool))
    out, w = at.attention(Q, K, V, mask)
    ref = F.scaled_dot_product_attention(*(torch.tensor(a) for a in (Q, K, V)),
                                         attn_mask=torch.tensor(mask)).numpy()
    assert np.allclose(out, ref)
    assert w[0, 0].tolist() == [1, 0, 0, 0, 0], (
        "With a 'look only backwards' mask, the first word can only attend to itself. "
        "That one mask is what turns this encoder into the generator of week 11.")
