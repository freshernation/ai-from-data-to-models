from shoplab.llm import Reply, get_llm


def ten_questions(ask, memory):
    chat = ask.Chat(get_llm(), "You are the shop's assistant.", memory=memory)
    for i in range(10):
        chat.send(f"Question {i + 1}: where is my order number {1000 + i}? It was a mug and a kettle.")
    return chat


def test_cost(load):
    ask = load("ask.py")
    r = Reply("x", input_tokens=1_000_000, output_tokens=100_000, latency_ms=1, model="m")
    assert ask.cost(r, "claude-opus-5-5") == 4.0 + 2.0
    assert abs(ask.cost(r, "claude-haiku-5-5") - 0.15) < 1e-12


def test_history(load):
    ask = load("ask.py")
    chat = ask.Chat(get_llm())
    chat.send("hello")
    chat.send("again")
    assert [m["role"] for m in chat.history] == ["user", "assistant", "user", "assistant"]
    assert "1 earlier" in chat.history[-1]["content"], "The model only remembers what you send it."
    assert ask.Chat(get_llm(), memory=False).history == []


def test_finding_memory_is_resent_every_turn(load):
    ask = load("ask.py")
    remembering, forgetful = ten_questions(ask, True), ten_questions(ask, False)
    sent = ask.tokens_sent(remembering)
    assert sent[0] == 25 and sent[-1] == 424, "Turn 1 sends 25 tokens; turn 10 sends 424."
    assert (sum(sent), sum(ask.tokens_sent(forgetful))) == (2211, 250), (
        "Ten turns with memory: 2,211 input tokens. Without: 250. The history is paid for "
        "again on every turn, so cost grows with the square of the conversation's length.")
    assert round(ask.per_thousand(remembering.replies, "claude-opus-5-5"), 2) == 1.43
