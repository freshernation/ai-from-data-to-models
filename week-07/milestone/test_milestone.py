import torch
from sklearn.datasets import make_moons
from sklearn.metrics import roc_auc_score

from shoplab import customers


def moons():
    X, y = make_moons(n_samples=1060, noise=0.35, random_state=0)
    t = lambda a: torch.as_tensor(a, dtype=torch.float32)
    return t(X[:60]), torch.as_tensor(y[:60]), t(X[60:]), torch.as_tensor(y[60:])


def big_net():
    return torch.nn.Sequential(torch.nn.Linear(2, 256), torch.nn.ReLU(),
                               torch.nn.Linear(256, 256), torch.nn.ReLU(), torch.nn.Linear(256, 2))


def test_trainer_stops_early_and_restores_the_best(load):
    tr = load("trainer.py")
    X, y, Xv, yv = moons()
    torch.manual_seed(0)
    model = big_net()
    history = tr.fit(model, torch.nn.CrossEntropyLoss(), X, y, Xv, yv, epochs=300, patience=20)
    assert history["stopped_epoch"] == history["best_epoch"] + 20 < 299, \
        "Stop exactly `patience` epochs after the best one."
    assert len(history["val"]) == history["stopped_epoch"] + 1
    with torch.no_grad():
        now = torch.nn.CrossEntropyLoss()(model(Xv), yv).item()
    assert abs(now - min(history["val"])) < 1e-6, "Load the best state before returning."
    assert not model.training, "Leave the model in eval mode."


def test_finding_the_churn_network_ties_the_line(load):
    cn = load("churn_net.py")
    train_df, test_df = customers.frozen_split()
    model, mean, std, history = cn.train(train_df)
    auc = roc_auc_score(test_df["churned"], cn.predict_proba(model, mean, std, test_df))
    assert 0.775 < auc < 0.795, f"Test AUC {auc:.3f}; the reference run gave 0.785. The line gives 0.779."
    assert history["stopped_epoch"] == history["best_epoch"] + 30


def test_comparison(source):
    text = source("COMPARISON.md")
    assert "<!--" not in text, "Delete the instructions comment in COMPARISON.md."
    for heading in ("The candidates", "The numbers", "How much of the difference is noise",
                    "What I would ship, and why"):
        assert f"## {heading}" in text, f"COMPARISON.md has no '{heading}' section."
        part = text.split(f"## {heading}", 1)[1].split("\n## ")[0]
        assert len(part.split()) >= 50, f"'{heading}' is {len(part.split())} words; write at least 50."
    assert "0.779" in text, "Put week 3's number beside this week's."
