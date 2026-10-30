import numpy as np
from sklearn.linear_model import LogisticRegression


def test_fit_returns_self_and_records_loss(load):
    mlp = load("mlp.py")
    X, y, _, _ = mlp.moons()
    model = mlp.MLP(epochs=50)
    assert model.fit(X, y) is model and len(model.losses_) == 50
    assert model.predict_proba(X).shape == (450, 2) and np.allclose(model.predict_proba(X).sum(axis=1), 1)


def test_finding_the_hidden_layer_beats_the_line(load):
    mlp = load("mlp.py")
    X, y, Xt, yt = mlp.moons()
    model = mlp.MLP().fit(X, y)
    line = LogisticRegression().fit(X, y).score(Xt, yt)
    assert round(model.score(Xt, yt), 3) == 0.933 and round(line, 3) == 0.9, \
        "16 hidden units: 93.3% on the test moons. A straight line: 90.0%."
    assert round(model.losses_[-1], 3) == 0.119
    assert round(mlp.MLP(hidden=2).fit(X, y).score(Xt, yt), 3) == 0.907, \
        "Two hidden units can only bend the line a little: 90.7%."


def test_by_hand_means_no_library_network(load, source):
    mlp = load("mlp.py")
    code = source("mlp.py", code_only=True)
    assert "MLPClassifier" not in code and "torch" not in code


def test_notes(source):
    text = source("NOTES.md")
    assert "<!--" not in text, "Delete the instructions comment in NOTES.md."
    for heading in ("Why one layer is not enough", "What backpropagation does",
                    "How I know my gradients are right", "Why the starting weights matter",
                    "What the hidden layer bought"):
        assert f"## {heading}" in text, f"NOTES.md has no '{heading}' section."
        part = text.split(f"## {heading}", 1)[1].split("\n## ")[0]
        assert len(part.split()) >= 50, f"'{heading}' is {len(part.split())} words; write at least 50."
        if heading != "What backpropagation does":
            assert any(ch.isdigit() for ch in part), f"'{heading}' needs a number you measured."
