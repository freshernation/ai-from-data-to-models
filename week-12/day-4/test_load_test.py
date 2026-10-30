import re

from fastapi.testclient import TestClient


def test_percentile(load):
    lt = load("load_test.py")
    assert lt.percentile([5, 1, 3, 2, 4], 50) == 3
    assert lt.percentile(list(range(1, 101)), 95) == 95 and lt.percentile([7], 99) == 7


def test_timing_a_real_app(load):
    lt = load("load_test.py")
    api = load("api.py")
    client = TestClient(api.create_app(lambda c: 0.1, lambda t: "positive", lambda p: "mug"))
    times = lt.time_requests(client, "/sentiment", {"text": "lovely"}, n=50)
    s = lt.summary(times)
    assert len(times) == 50 and s["p50"] <= s["p95"] <= s["p99"] <= s["max"]


def test_portfolio(source):
    text = source("PORTFOLIO.md")
    assert "<!--" not in text, "Delete the instructions comment in PORTFOLIO.md."
    for heading in ("What I built", "Results", "The decision I am proudest of",
                    "What went wrong, and what I learned", "How to run it"):
        assert f"## {heading}" in text, f"PORTFOLIO.md has no '{heading}' section."
    for heading in ("What I built", "The decision I am proudest of", "What went wrong, and what I learned"):
        part = text.split(f"## {heading}", 1)[1].split("\n## ")[0]
        assert len(part.split()) >= 60, f"'{heading}' is {len(part.split())} words; write at least 60."
    table = text.split("## Results", 1)[1].split("\n## ")[0]
    rows = [r for r in table.splitlines() if r.startswith("|") and re.search(r"\d", r)]
    assert len(rows) >= 5, "The results table needs at least five rows with your numbers."
