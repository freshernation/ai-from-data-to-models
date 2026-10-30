from fastapi.testclient import TestClient

GOOD = {"plan": "basic", "tenure_months": 5, "monthly_spend": 30.0, "orders_90d": 2,
        "days_since_last_order": 40, "support_tickets": 1, "used_discount": 0}


def client(api, calls):
    def churn(customer):
        calls.append(customer)
        return 0.25
    return TestClient(api.create_app(churn, lambda t: "negative", lambda p: "mug", version="9.9"))


def test_health_and_answers(load):
    api = load("api.py")
    calls = []
    c = client(api, calls)
    assert c.get("/health").json() == {"status": "ok", "version": "9.9"}
    assert c.post("/churn", json=GOOD).json() == {"probability": 0.25}
    assert calls == [GOOD], "The model gets the customer as a plain dict."
    assert c.post("/sentiment", json={"text": "not good"}).json() == {"label": "negative"}
    assert c.post("/product", json={"pixels": [[0] * 16] * 16}).json() == {"label": "mug"}


def test_finding_bad_input_never_reaches_a_model(load):
    api = load("api.py")
    calls = []
    c = client(api, calls)
    for bad in ({**GOOD, "tenure_months": 0}, {**GOOD, "plan": "gold"}, {**GOOD, "used_discount": 2},
                {**GOOD, "monthly_spend": -5}, {k: v for k, v in GOOD.items() if k != "plan"}):
        assert c.post("/churn", json=bad).status_code == 422, f"Should be refused: {bad}"
    assert calls == [], (
        "Five broken customers, five 422s, and the model never saw one. A model trained on "
        "tenures of 1 to 60 has no idea what a tenure of 0 means - so it must never be asked.")
    assert c.post("/sentiment", json={"text": ""}).status_code == 422
    assert c.post("/sentiment", json={"text": "x" * 501}).status_code == 422
    assert c.post("/product", json={"pixels": [[0] * 16] * 15}).status_code == 422
    assert c.post("/product", json={"pixels": [[300] * 16] * 16}).status_code == 422
