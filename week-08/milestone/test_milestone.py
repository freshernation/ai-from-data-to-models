import functools

import numpy as np

from shoplab import images


@functools.lru_cache(maxsize=None)
def _data():
    return images.load()


def trained(load):
    pc = load("product_classifier.py")
    model, history = pc.train(_data())
    return pc, model


def test_project_two(load, tmp_path):
    pc, model = trained(load)
    d = _data()
    r = pc.report(model, d)
    assert r["centred"] > 0.97 and r["shifted"] > 0.97
    assert np.trace(np.array(r["confusion"])) == round(r["shifted"] * 500)

    path = tmp_path / "model.pt"
    pc.save(model, path)
    again = pc.load(path)
    assert pc.predict(again, d["X_test"][:20]) == pc.predict(model, d["X_test"][:20]), \
        "The reloaded model must give exactly the same answers."
    assert set(pc.predict(model, d["X_test"][:50])) <= set(images.CLASSES)

    errors = pc.error_gallery(model, d["X_shifted"], d["y_shifted"], tmp_path / "errors.png")
    assert type(errors) is int and (tmp_path / "errors.png").exists()

    s = pc.stress(model, d["X_test"], d["y_test"])
    assert set(s) == {"noise 0.0", "noise 0.2", "noise 0.4", "noise 0.6",
                      "brightness 1.0", "brightness 0.5", "brightness 0.3"}
    assert s["noise 0.2"] > 0.9 and s["brightness 0.5"] > 0.85
    assert s["noise 0.6"] < 0.75 and s["brightness 0.3"] < 0.75, (
        "Perfect on photos like its training data; about 50% with heavy noise or at 30% "
        "brightness. A 100% test score says nothing about conditions it never saw.")


def test_model_card(source):
    text = source("MODEL_CARD.md")
    assert "<!--" not in text, "Delete the instructions comment in MODEL_CARD.md."
    for heading in ("Intended use", "Data", "The model, and why a CNN", "Performance",
                    "Where it breaks", "Limits and risks"):
        assert f"## {heading}" in text, f"MODEL_CARD.md has no '{heading}' section."
        part = text.split(f"## {heading}", 1)[1].split("\n## ")[0]
        assert len(part.split()) >= 50, f"'{heading}' is {len(part.split())} words; write at least 50."
    breaks = text.split("## Where it breaks", 1)[1].split("\n## ")[0]
    assert any(ch.isdigit() for ch in breaks), "Say where it breaks with numbers."
