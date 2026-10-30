from shoplab import DATA

RAW = DATA / "customers_raw.csv"


class TestExplore:
    def test_load_reads_every_row(self, load):
        ex = load("explore.py")
        df = ex.load(RAW)
        assert df.shape == (2037, 11), "The raw export has 2,037 rows and 11 columns."

    def test_churn_rate(self, load):
        ex = load("explore.py")
        assert round(ex.churn_rate(ex.load(RAW)), 4) == 0.1321, "Raw, duplicates included: 13.21%. Clean, it is 13.05% - tomorrow."

    def test_churn_by_plan_highest_first(self, load):
        ex = load("explore.py")
        rates = ex.churn_by_plan(ex.load(RAW))
        assert list(rates.index) == ["basic", "plus", "pro"], "Sort highest first."
        assert rates.iloc[0] > 3 * rates.iloc[-1], "Basic churns more than three times as often as pro."

    def test_top_spenders(self, load):
        ex = load("explore.py")
        top = ex.top_spenders(ex.load(RAW), n=3)
        assert list(top.columns) == ["customer_id", "plan", "monthly_spend"]
        assert len(top) == 3 and top["monthly_spend"].is_monotonic_decreasing


def test_finding_the_raw_count_is_wrong_in_a_way_you_cannot_see(load):
    ex = load("explore.py")
    df = ex.load(RAW)
    assert ex.count_where(df, "region", "north") == 151, (
        "Only 151 rows say exactly 'north' - but 618 customers live in the north. "
        "'North', 'NORTH' and ' north' are the same place to you and three places to "
        "pandas. Tomorrow you fix it.")
    assert ex.count_where(df, "customer_id", "C00001") >= 1
