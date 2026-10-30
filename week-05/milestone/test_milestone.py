from shoplab import orders


def test_three_segments_with_profiles(load):
    sr = load("shop_recs.py")
    labels, profiles = sr.segment_customers()
    assert labels.name == "segment" and len(labels) == 2000
    assert sorted(profiles["customers"]) == [613, 671, 716]
    assert list(profiles.columns) == orders.CATEGORIES + ["customers"]


def test_segments_never_read_the_answer_key(load, source):
    sr = load("shop_recs.py")
    sr.segment_customers()
    assert "hidden_segments" not in source("shop_recs.py", code_only=True)


def test_also_bought(load):
    sr = load("shop_recs.py")
    rec = sr.Recommender()
    assert rec.also_bought("I001") == ["I002", "I003", "I011", "I012", "I004"]
    items = orders.items()
    for _, group in items.groupby("category"):
        ids = group["item_id"].tolist()
        for i, item in enumerate(ids):
            partner = ids[(i + 1) % len(ids)]
            assert partner in rec.also_bought(item, 3), \
                f"{partner} is what {item}'s buyers buy next; it should be in the top three."


def test_for_customer(load):
    sr = load("shop_recs.py")
    assert sr.Recommender().for_customer("C00001", 3) == ["I003", "I012", "I039"]


def test_segments_doc(source):
    text = source("SEGMENTS.md")
    assert "<!--" not in text, "Delete the instructions comment in SEGMENTS.md."
    for heading in ("The segments", "Why three and not four", "What the recommender adds",
                    "How I know it works", "What I would not use it for"):
        assert f"## {heading}" in text, f"SEGMENTS.md has no '{heading}' section."
        part = text.split(f"## {heading}", 1)[1].split("\n## ")[0]
        assert len(part.split()) >= 50, f"'{heading}' is {len(part.split())} words; write at least 50."
    assert "73" in text and "31" in text, "Quote both hit rates."
