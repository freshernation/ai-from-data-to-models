import re
import shutil
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from shoplab import customers, images

HERE = Path(__file__).parent


def customer_rows(df, n):
    rows = df[["plan"] + customers.FEATURES].head(n).to_dict("records")
    return [{k: (v.item() if hasattr(v, "item") else v) for k, v in r.items()} for r in rows]


def test_project_three(load, tmp_path):
    ta = load("train_all.py")
    sv = load("service.py")
    bundle = tmp_path / "bundle"
    manifest = ta.build(bundle)
    assert set(manifest["files"]) == {"churn.joblib", "reference.csv", "sentiment.pt", "vocab.json", "product.pt"}
    m = manifest["metrics"]
    assert m["churn_auc"] > 0.75 and m["sentiment_accuracy"] > 0.95 and m["product_accuracy_moved"] > 0.95

    c = TestClient(sv.load_service(bundle))
    assert c.get("/health").json()["version"] == "1.0.0" and c.get("/version").json() == manifest
    p = c.post("/churn", json=customer_rows(customers.load(), 1)[0]).json()["probability"]
    assert 0 <= p <= 1
    assert c.post("/sentiment", json={"text": "not really good !"}).json() == {"label": "negative"}
    photos = images.load()
    assert c.post("/product", json={"pixels": photos["X_shifted"][0].tolist()}).json() == \
        {"label": images.CLASSES[photos["y_shifted"][0]]}

    drift = c.post("/drift", json=customer_rows(customers.next_month(), 300)).json()
    assert drift["days_since_last_order"]["verdict"] == "drifted"
    assert all(v["verdict"] != "drifted" for k, v in drift.items() if k != "days_since_last_order")
    assert "error" in c.post("/drift", json=customer_rows(customers.load(), 10)).json()

    tampered = tmp_path / "tampered"
    shutil.copytree(bundle, tampered)
    (tampered / "product.pt").write_bytes((tampered / "product.pt").read_bytes() + b"\0")
    with pytest.raises(RuntimeError, match="product.pt"):
        sv.load_service(tampered)


def test_dockerfile():
    text = (HERE / "Dockerfile").read_text()
    lines = [l.strip() for l in text.splitlines() if l.strip() and not l.strip().startswith("#")]
    assert lines and lines[0] == "FROM python:3.12-slim", "Start from python:3.12-slim."
    joined = "\n".join(lines)
    install = joined.find("pip install")
    assert 0 < install < joined.find("COPY shoplab"), "Install requirements before copying code."
    assert re.search(r"^USER (?!root)\w+", joined, re.M), "Switch to a user who is not root."
    assert "EXPOSE 8000" in joined and "HEALTHCHECK" in joined
    assert 'CMD ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "8000"]' in joined


def test_review(source):
    text = source("REVIEW.md")
    assert "<!--" not in text, "Delete the instructions comment in REVIEW.md."
    for heading in ("What is running", "How fast, and how it fails", "What we watch",
                    "Who it could treat unfairly", "What I would fix first"):
        assert f"## {heading}" in text, f"REVIEW.md has no '{heading}' section."
        part = text.split(f"## {heading}", 1)[1].split("\n## ")[0]
        assert len(part.split()) >= 60, f"'{heading}' is {len(part.split())} words; write at least 60."
        if heading != "What I would fix first":
            assert re.search(r"\d", part), f"'{heading}' needs a number you measured."
