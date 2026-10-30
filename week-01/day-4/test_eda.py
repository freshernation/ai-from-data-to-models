import numpy as np
import pandas as pd

from shoplab import customers


class TestPlots:
    def test_histogram_file_and_counts(self, load, tmp_path):
        eda = load("eda.py")
        out = tmp_path / "spend.png"
        counts = eda.save_histogram([1, 2, 2, 3, 3, 3], out, bins=3)
        assert out.exists() and out.stat().st_size > 1000, "Save the figure with fig.savefig(path)."
        assert list(counts) == [1, 2, 3]


class TestBuckets:
    def test_rate_by_bucket(self, load):
        eda = load("eda.py")
        df = pd.DataFrame({"days": [1, 2, 10, 11], "churned": [0, 0, 1, 0]})
        rates = eda.rate_by_bucket(df, "days", [0, 5, 20])
        assert list(rates) == [0.0, 0.5]

    def test_finding_silence_predicts_leaving(self, load):
        eda = load("eda.py")
        rates = eda.rate_by_bucket(customers.load(), "days_since_last_order", [0, 15, 30, 60, 181])
        assert [round(r, 3) for r in rates] == [0.064, 0.109, 0.155, 0.480], \
            "Customers silent for 60+ days churn at 48% - over seven times the 0-15 day rate."


class TestLeaks:
    def test_a_column_that_is_the_answer(self, load):
        eda = load("eda.py")
        df = pd.DataFrame({"why": ["price", None, "slow", None], "x": [1, 1, 2, 2],
                           "churned": [1, 0, 1, 0]})
        assert eda.leak_score(df, "why") == 1.0
        assert eda.leak_score(df, "x") == 0.5
        assert eda.find_leaks(df) == ["why"]


def test_finding_the_export_contains_the_answer(load):
    eda = load("eda.py")
    raw = customers.load_raw()
    assert eda.find_leaks(raw) == ["cancel_reason"], (
        "cancel_reason is only filled in AFTER a customer leaves. A model given it "
        "scores 100% and is useless on the day you need it.")
    assert round(eda.leak_score(raw, "plan"), 4) == round(1 - raw["churned"].mean(), 4), \
        "An honest column on its own does no better than the baseline."
