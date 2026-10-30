import numpy as np
import pandas as pd

from shoplab import customers


def tiny():
    return pd.DataFrame({
        "customer_id": ["A", "B", "A", "C"],
        "region": [" North", "north", " North", "WEST"],
        "plan": ["basic", "basic", "basic", "pro"],
        "monthly_spend": [10.0, np.nan, 10.0, -1.0],
    })


class TestEachStep:
    def test_duplicates(self, load):
        cl = load("clean.py")
        out, dropped = cl.drop_duplicates(tiny())
        assert dropped == 1 and list(out["customer_id"]) == ["A", "B", "C"]
        assert list(out.index) == [0, 1, 2], "Reset the index after dropping rows."

    def test_region(self, load):
        cl = load("clean.py")
        assert list(cl.normalise_region(tiny()["region"])) == ["north", "north", "north", "west"]

    def test_impossible_becomes_missing_not_zero(self, load):
        cl = load("clean.py")
        out, changed = cl.fix_impossible(tiny())
        assert changed == 1
        assert np.isnan(out["monthly_spend"].iloc[3]), \
            "A 0 is a real spend. An impossible value is unknown: NaN."

    def test_fill_uses_the_plans_median(self, load):
        cl = load("clean.py")
        df = pd.DataFrame({"plan": ["basic", "basic", "basic", "pro"],
                           "monthly_spend": [10.0, 30.0, np.nan, 90.0]})
        out, filled = cl.fill_missing(df)
        assert filled == 1 and out["monthly_spend"].iloc[2] == 20.0, \
            "The missing basic customer gets the basic median (20), not the overall one."

    def test_never_changes_the_input(self, load):
        cl = load("clean.py")
        df = tiny()
        cl.clean(df)
        assert df["monthly_spend"].iloc[3] == -1.0 and len(df) == 4, \
            "Work on a copy - the caller's frame must be untouched."


def test_finding_what_was_wrong_with_the_export(load):
    cl = load("clean.py")
    df, report = cl.clean(customers.load_raw())
    assert report["duplicates"] == 37
    assert report["region_spellings"] == (12, 4), "Twelve spellings of four regions."
    assert report["impossible"] == 12
    assert report["filled"] == 72, "60 gaps plus the 12 impossible values you made missing."
    assert len(df) == 2000 and df["monthly_spend"].isna().sum() == 0
