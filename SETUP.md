# Day zero

About an hour. Do it before week 1, not on Monday morning.

---

## 1. Python 3.12 or newer

```bash
python3 --version
```

## 2. Your own repository

Make your own copy of this repository on GitHub (**Use this template**), then clone it:

```bash
git clone https://github.com/YOUR-USERNAME/ai-from-data-to-models.git
cd ai-from-data-to-models
```

## 3. The environment

```bash
python3 -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

PyTorch is the big download (a few hundred MB). On an Intel Mac pip picks torch 2.2,
the last release built for it; every lab works on it.

## 4. Check it

```bash
python3 check_setup.py
pytest shoplab -q
```

Every line of `check_setup.py` should say OK except the last, about your baseline. The
`shoplab` tests should pass: they check the shop's data. Everything under `week-01/`
fails until you write it, which is how it should be.

## 5. Your baseline interview

Open a fresh chat with any capable AI. Paste the whole of `ai/advisor.md`. Answer its
questions honestly. At the end it prints a `BASELINE` block. Paste it into
`logs/baseline.md`, replacing the bracketed lines, and push.

## 6. Accounts and keys

None until week 11. Then, optionally, a free-tier key for any LLM provider, in a `.env`
file that git ignores. Week 12 needs Docker Desktop (free for personal use); install it
before that Monday.
