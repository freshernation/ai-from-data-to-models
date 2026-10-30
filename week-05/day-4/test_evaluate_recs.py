import pandas as pd

from shoplab import orders


def test_leave_last_out(load):
    ev = load("evaluate_recs.py")
    rows = pd.DataFrame({"customer_id": ["a", "a", "a", "b", "b"],
                         "item_id": ["x", "y", "z", "x", "w"], "seq": [1, 3, 2, 1, 2]})
    history, held = ev.leave_last_out(rows)
    assert held.to_dict() == {"a": "y", "b": "w"} and len(history) == 3


def test_finding_item_similarity_beats_popularity(load):
    ev = load("evaluate_recs.py")
    o = orders.load()
    assert ev.hit_rate(o, 10) == 0.7325, "73% of customers find their next purchase in the top 10."
    assert ev.hit_rate(o, 10, "popular") == 0.3125, "'Most popular' finds it for 31%."
    assert (ev.hit_rate(o, 5), ev.hit_rate(o, 5, "popular")) == (0.527, 0.17), \
        "With five slots the gap grows: 52.7% against 17%."
