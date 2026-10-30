"""One way to call a language model, whichever is behind it.

    from shoplab.llm import get_llm
    llm = get_llm()
    reply = llm.complete([{"role": "user", "content": "Hi"}], system="Be brief.")
    reply.text, reply.input_tokens, reply.output_tokens, reply.latency_ms

SHOPLAB_LLM=fake        (default, and always in tests) a scripted stand-in, offline and free
SHOPLAB_LLM=anthropic   Claude, through the official SDK. Needs ANTHROPIC_API_KEY (or an
                        `ant auth login` profile) and `pip install anthropic`.
SHOPLAB_MODEL           the Claude model id (default claude-opus-5-5)

The fake is NOT a language model. It follows a few fixed rules, chosen to fail in the
ways real models fail: it sometimes wraps its JSON in chatter, it misses negation that
is not right next to the adjective, and it obeys instructions hidden in a review. Every
number you measure with it is about your code, not about any real model.
"""

import json
import math
import os
import re
import time
import zlib
from dataclasses import dataclass

DEFAULT_MODEL = "claude-opus-5-5"

# US dollars per million tokens (input, output). From Anthropic's published price table,
# checked 2026-10-29. Prices change: check https://www.anthropic.com/pricing before quoting.
PRICES = {
    "claude-opus-5-5": (4.00, 20.00),
    "claude-sonnet-5-5": (2.00, 10.00),
    "claude-haiku-5-5": (0.10, 0.50),
}


@dataclass
class Reply:
    text: str
    input_tokens: int
    output_tokens: int
    latency_ms: float
    model: str


def rough_tokens(text):
    """About four characters per token - close enough for English, wrong for code."""
    return max(1, math.ceil(len(text) / 4))


_POS = {"great", "good", "excellent", "lovely", "perfect", "sturdy", "comfortable", "beautiful"}
_NEG = {"bad", "terrible", "awful", "poor", "flimsy", "broken", "cheap", "useless"}


def _fake_sentiment(review):
    words = re.findall(r"[a-z']+", review.lower())
    for i, word in enumerate(words):
        if word in _POS or word in _NEG:
            positive = word in _POS
            if i > 0 and words[i - 1] == "not":
                positive = not positive
            return "positive" if positive else "negative", word
    return "positive", "nothing negative"


class FakeLLM:
    model = "fake-shop-llm"

    def complete(self, messages, system="", max_tokens=1024):
        last = messages[-1]["content"]
        rule = system.lower()
        if "reply" in rule:
            text = self._draft(last)
        elif "sentiment" in rule:
            text = self._classify(last, retry=sum(m["role"] == "user" for m in messages) > 1)
        else:
            earlier = sum(m["role"] == "user" for m in messages) - 1
            text = f"You said: {last}" + (f" (I remember {earlier} earlier messages.)" if earlier else "")
        prompt = system + "".join(m["content"] for m in messages)
        out = rough_tokens(text)
        return Reply(text, rough_tokens(prompt), out, 250.0 + 8.0 * out, self.model)

    def _classify(self, review, retry):
        label, word = _fake_sentiment(review)
        answer = json.dumps({"label": label, "reason": f"the review says '{word}'"})
        bucket = zlib.crc32(review.encode()) % 10
        if not retry and bucket == 0:
            return f"Sure! Here is my answer: {answer}"
        if not retry and bucket == 1:
            return answer.replace(f'"{label}"', f'"{label.title()}!"')
        return answer

    def _draft(self, prompt):
        if re.search(r"ignore (all|your|the|previous)", prompt.lower()):
            return ("Of course! As you asked, here is a 100% discount code: FREE100. "
                    "Write to refunds@shop.example and we will refund you in full.")
        if "positive" in prompt.lower().split("review:")[0]:
            return "Thank you for your kind review! We are glad you are happy with it."
        return "We are sorry to hear this. Our team will look into it and get back to you."


class AnthropicLLM:
    def __init__(self, model=None):
        import anthropic
        self.client = anthropic.Anthropic()
        self.model = model or os.environ.get("SHOPLAB_MODEL", DEFAULT_MODEL)

    def complete(self, messages, system="", max_tokens=1024):
        start = time.perf_counter()
        response = self.client.beta.messages.create(
            model=self.model, max_tokens=max_tokens, system=system, messages=messages,
            output_config={"effort": "low"},
            betas=["server-side-fallback-2026-07-01"], fallbacks="default",
        )
        if response.stop_reason == "refusal":
            raise RuntimeError(f"The model declined: {response.stop_details}")
        text = "".join(block.text for block in response.content if block.type == "text")
        return Reply(text, response.usage.input_tokens, response.usage.output_tokens,
                     (time.perf_counter() - start) * 1000, response.model)


def get_llm():
    provider = os.environ.get("SHOPLAB_LLM", "fake")
    if provider == "fake":
        return FakeLLM()
    if provider == "anthropic":
        return AnthropicLLM()
    raise ValueError(f"SHOPLAB_LLM={provider!r}: use 'fake' or 'anthropic'.")
