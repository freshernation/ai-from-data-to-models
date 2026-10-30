# Day 2 — Which model is running?

> **By the end of today** you can fingerprint every model file, write a manifest, refuse
> to run anything that has changed, and explain what a container adds.

---

## Read first

- [ ] FastAPI — [FastAPI in containers](https://fastapi.tiangolo.com/deployment/docker/) — up to "Docker image with Poetry" · 20 min
- [ ] Docker — [Building best practices](https://docs.docker.com/build/building/best-practices/) — "Leverage build cache" and "User" · 10 min

---

## What you need to know

### A fingerprint

SHA-256 of a file's bytes: change one byte and it changes completely. The manifest lists
every model file with its fingerprint, the version and the test metrics. A service that
checks it at start-up can never run weights nobody evaluated.

### The finding

Change one byte of a model, add a stray file, delete another: `verify` names all three.
Without it, the first sign of a half-copied model file is a customer getting nonsense.

### A container

A Dockerfile is a recipe for an image: a base system, the dependencies, your code and
your model files, and the command that starts the service. The same image runs on your
laptop and on any server. Two rules matter most: install dependencies *before* copying
code (so changing code does not reinstall torch), and never run as root. You write the
Dockerfile in the milestone.

---

## Exercises

```bash
pytest week-12/day-2 -v
```

Write the four functions in `artifacts.py`. Then run `docker run hello-world`.

---

## Predict-then-run

If you re-save the same trained model with `torch.save`, will its fingerprint change?
Try it.

---

## Before you close the laptop

Commit, push, fill in the signal log.
