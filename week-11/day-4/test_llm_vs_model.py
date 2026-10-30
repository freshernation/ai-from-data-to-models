from shoplab import reviews
from shoplab.llm import get_llm


def test_break_even(load):
    lv = load("llm_vs_model.py")
    assert lv.break_even(2.0, 100) == 50_000


def test_wrapping_is_undone(load):
    lv = load("llm_vs_model.py")
    llm = get_llm()
    before = llm.complete
    labels, replies = lv.llm_labels(llm, ["not bad at all !", "Sure thing"])
    assert llm.complete == before, "Put the original complete back."
    assert len(labels) == 2 and len(replies) >= 2


def test_finding_the_comparison(load):
    lv = load("llm_vs_model.py")
    r = lv.compare(get_llm(), *reviews.frozen_split())
    assert r["llm"]["calls"] == 1192, "Every retry is a call you pay for."
    assert round(r["llm"]["dollars_per_1000"], 2) == 0.65
    assert r["own"]["all"] > 0.95 and r["own"]["dollars_per_1000"] == 0.0
    assert r["own"]["ms_per_review"] < 5, "Your LSTM classifies a review in well under a millisecond."
    assert r["llm"]["far negation"] < 0.5, (
        "The FAKE misses 'not really good' by design. That says nothing about Claude - run "
        "it live to find out - but it shows why you measure on YOUR hard cases.")
