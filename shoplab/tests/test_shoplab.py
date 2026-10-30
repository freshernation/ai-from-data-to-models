"""The data every week trains on. If one of these fails, the data files changed."""

from shoplab import customers


def test_raw_has_the_faults_week_1_cleans():
    raw = customers.load_raw()
    assert len(raw) == 2037
    assert raw["customer_id"].duplicated().sum() == 37
    assert raw["region"].nunique() == 12
    assert (raw["monthly_spend"] < 0).sum() == 12


def test_clean_copy_has_no_leak_and_no_gaps():
    df = customers.load()
    assert len(df) == 2000 and "cancel_reason" not in df.columns
    assert df.isna().sum().sum() == 0
    assert round(df["churned"].mean(), 4) == 0.1305


def test_frozen_split_is_stratified_and_stable():
    train, test = customers.frozen_split()
    assert (len(train), len(test)) == (1500, 500)
    assert test["churned"].sum() == 65
    assert set(train["customer_id"]).isdisjoint(test["customer_id"])
    again, _ = customers.frozen_split()
    assert train["customer_id"].tolist() == again["customer_id"].tolist()


def test_orders_and_items():
    from shoplab import orders
    o, i = orders.load(), orders.items()
    assert len(i) == 60 and set(i["category"]) == set(orders.CATEGORIES)
    assert len(o) == 15919 and o["customer_id"].nunique() == 2000
    assert not o.duplicated(["customer_id", "item_id"]).any(), "Nobody buys the same item twice."
    shares = orders.category_shares()
    assert shares.shape == (2000, 6) and (shares.sum(axis=1).round(9) == 1).all()
