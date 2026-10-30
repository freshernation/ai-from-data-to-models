import pandas as pd

from shoplab import DATA, customers


def test_prepare_writes_a_trainable_file(load, tmp_path):
    prep = load("prepare.py")
    out = tmp_path / "prepared.csv"
    df, report = prep.prepare(DATA / "customers_raw.csv", out)
    written = pd.read_csv(out)
    assert len(written) == 2000, "One row per customer."
    assert "Unnamed: 0" not in written.columns, "Write with index=False."
    assert written.isna().sum().sum() == 0
    assert sorted(written["region"].unique()) == ["east", "north", "south", "west"]
    assert set(written["customer_id"]) == set(customers.load()["customer_id"])


def test_the_leak_is_found_not_named(load, tmp_path, source):
    prep = load("prepare.py")
    df, report = prep.prepare(DATA / "customers_raw.csv", tmp_path / "p.csv")
    assert report["leaks"] == ["cancel_reason"] and "cancel_reason" not in df.columns
    assert "cancel_reason" not in source("prepare.py", code_only=True), \
        "Drop what find_leaks returns. Next month's export may leak a different column."


def test_report(source):
    text = source("DATA_REPORT.md")
    assert "<!--" not in text, "Delete the instructions comment in DATA_REPORT.md."
    for heading in ("The data", "What was wrong", "The leak", "What I would ask the data owner"):
        assert f"## {heading}" in text, f"DATA_REPORT.md has no '{heading}' section."
        part = text.split(f"## {heading}", 1)[1].split("\n## ")[0]
        assert len(part.split()) >= 40, f"'{heading}' is {len(part.split())} words; write at least 40."
    assert "37" in text and "2,000" in text.replace("2000", "2,000"), \
        "Quote your own numbers: the duplicates and the customers left."
