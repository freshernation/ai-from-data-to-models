import pytest
from pydantic import ValidationError

from shoplab import reviews
from shoplab.llm import Reply, get_llm


def test_parse(load):
    st = load("structured.py")
    assert st.parse('{"label": "negative", "reason": "broken"}').label == "negative"
    with pytest.raises(ValidationError):
        st.parse('{"label": "Positive!", "reason": "x"}')
    with pytest.raises(ValueError):
        st.parse('Sure! {"label": "positive", "reason": "x"}')


def test_retry_sends_the_mistake_back(load):
    st = load("structured.py")
    seen = []

    class Stubborn:
        def complete(self, messages, system=""):
            seen.append(messages)
            return Reply("no", 1, 1, 1, "stub")

    result, calls = st.classify(Stubborn(), "the mug is lovely", retries=2)
    assert result is None and calls == 3
    assert [m["role"] for m in seen[1]] == ["user", "assistant", "user"]
    assert seen[1][1]["content"] == "no", "Show the model its own bad answer."


def test_finding_one_answer_in_five_is_unusable(load):
    st = load("structured.py")
    _, test = reviews.frozen_split()
    once = st.survey(get_llm(), test["text"], retries=0)
    again = st.survey(get_llm(), test["text"], retries=1)
    assert once["failed"] == 192, "With no retry, 192 of 1,000 answers cannot be used."
    assert (again["failed"], again["calls"]) == (0, 1192), \
        "One retry rescues all of them - for 19% more calls, and 19% more cost."
