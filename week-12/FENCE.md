# Week 12 — Concept fence

## Allowed

**Everything from weeks 1 to 11**, plus:

- FastAPI, `TestClient`, pydantic `Field` and `field_validator`; uvicorn
- `hashlib`; a JSON manifest; `torch.save` / `joblib` bundles
- a Dockerfile; `docker build` and `docker run`
- PSI, recall by group, per-feature contributions of a linear model; percentiles

## Not yet

cloud deployment and CI/CD (the `agent-in-production` course) · Kubernetes · model registries
(MLflow and friends) · SHAP · feature stores · A/B testing · authentication and rate limits

---

## Why no cloud

Deploying to a cloud adds accounts, billing, IAM and networking — a week each, and none of
it about the model. A container that runs on your laptop runs on any cloud; the
`agent-in-production` course takes it there. This week's hard parts are the ones a cloud
does not do for you: knowing which model is running, refusing input it cannot handle, and
noticing when the world has moved.
