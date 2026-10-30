"""Day 2 - talking to a model through a client, and what memory costs.

Use shoplab.llm.get_llm() for the model. Tests always get the scripted fake.
"""

from shoplab.llm import PRICES


def user(text):
    """{"role": "user", "content": text}"""
    raise NotImplementedError


def cost(reply, model):
    """US dollars for one reply at PRICES[model] = (dollars per million input tokens,
    dollars per million output tokens)."""
    raise NotImplementedError


class Chat:
    """A conversation. The model remembers nothing: with memory=True, every send() passes
    the whole history (user and assistant turns) again.

        chat = Chat(llm, system="...", memory=True)
        chat.send("hello")   -> the reply's text
        chat.history          the messages so far (empty when memory=False)
        chat.replies          every Reply, in order
    """

    def __init__(self, llm, system="", memory=True):
        raise NotImplementedError

    def send(self, text):
        raise NotImplementedError


def tokens_sent(chat):
    """The input tokens of each reply, in order."""
    raise NotImplementedError


def per_thousand(replies, model):
    """Average cost of these replies, times 1,000."""
    raise NotImplementedError
