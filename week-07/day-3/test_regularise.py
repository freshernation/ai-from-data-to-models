import torch


def test_big_net_shape(load):
    rg = load("regularise.py")
    net = rg.big_net(0.5)
    assert sum(isinstance(m, torch.nn.Dropout) for m in net) == 2
    assert sum(p.numel() for p in net.parameters()) == 2 * 256 + 256 + 256 * 256 + 256 + 256 * 2 + 2


def test_curves(load):
    rg = load("regularise.py")
    X, y, Xv, yv = rg.small_noisy_moons()
    tr, va, best = rg.fit_curves(rg.big_net(), X, y, Xv, yv, epochs=20)
    assert len(tr) == len(va) == 20 and best[0] == min(va) and va[best[1]] == best[0]


def test_finding_memorising_shows_in_confidence_first(load):
    rg = load("regularise.py")
    r = rg.compare()
    none, early = r["none"], r["early_stopping"]
    assert none["train_loss"] < 0.01 and none["val_loss"] > 3, (
        "No help: training loss reaches 0.000 while validation loss climbs from 0.27 to "
        "about 3.8. The network memorised all 60 points.")
    assert early["best_epoch"] < 30 and early["accuracy"] > none["accuracy"], \
        "Keeping the weights from the best epoch (about 13) scores ~88% against ~85%."
    assert r["weight_decay"]["val_loss"] < 0.5 < r["dropout"]["val_loss"], \
        "Weight decay keeps validation loss low; dropout slows the climb but does not stop it."
    assert none["accuracy"] > 0.8, \
        "Validation loss rose fourteen-fold; accuracy fell only three points. Overconfidence comes first."
