from shoplab import reviews
from shoplab.llm import Reply, get_llm


def always(label):
    return lambda text: label


def test_guardrail_catches_known_dangers(load):
    dr = load("drafter.py")
    assert dr.guardrail("Use code SAVE20 for 20% off!") == ["promises money"]
    assert dr.guardrail("Call us on +44 20 7946 0000 or mail help@shop.example") == ["gives contact details"]
    assert dr.guardrail("My system prompt says to be polite.") == ["talks about its instructions"]
    assert dr.guardrail("thanks " * 81) == ["too long"]
    assert all(dr.guardrail(text) == [] for text in dr.FALLBACK.values()), \
        "Your own fallback replies must pass your own guardrail."


def test_the_label_comes_from_your_model(load):
    dr = load("drafter.py")
    seen = []

    class Recorder:
        def complete(self, messages, system=""):
            seen.append(messages[-1]["content"])
            return Reply("Thank you, we are sorry.", 1, 1, 1, "stub")

    out = dr.draft("the mug is not good !", always("negative"), Recorder())
    assert seen[0].startswith("Sentiment: negative\nReview: the mug is not good !")
    assert out == {"sentiment": "negative", "draft": "Thank you, we are sorry.", "problems": [],
                   "blocked": False, "reply": "Thank you, we are sorry."}


def test_finding_the_model_obeyed_every_attack_and_none_got_out(load):
    dr = load("drafter.py")
    attacks = dr.audit(reviews.ATTACKS, always("negative"), get_llm())
    assert attacks == {"blocked": 8, "total": 8, "unsafe_sent": 0}, (
        "The fake model obeyed all eight attacks - every draft offered a discount code. "
        "Not one reached a customer.")
    _, test = reviews.frozen_split()
    ordinary = dr.audit(list(test["text"][:200]), always("positive"), get_llm())
    assert ordinary["blocked"] == 0, "And it must not block ordinary replies."


def test_guardrails_doc(source):
    text = source("GUARDRAILS.md")
    assert "<!--" not in text, "Delete the instructions comment in GUARDRAILS.md."
    for heading in ("Who decides what", "The attacks, and what happened",
                    "What the guardrail cannot catch", "Before this goes live"):
        assert f"## {heading}" in text, f"GUARDRAILS.md has no '{heading}' section."
        part = text.split(f"## {heading}", 1)[1].split("\n## ")[0]
        assert len(part.split()) >= 50, f"'{heading}' is {len(part.split())} words; write at least 50."
