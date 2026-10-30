from shoplab import customers


def test_validation_split_comes_from_training_data(load):
    tn = load("tabular_net.py")
    train, test = customers.frozen_split()
    fit_df, val_df = tn.validation_split(train)
    assert (len(fit_df), len(val_df)) == (1200, 300)
    assert set(val_df["customer_id"]) <= set(train["customer_id"])


def test_finding_the_network_ties_the_line(load):
    tn = load("tabular_net.py")
    train, test = customers.frozen_split()
    aucs = []
    for seed in range(3):
        model, mean, std, best_epoch = tn.fit(train, seed=seed)
        aucs.append(tn.test_auc(model, mean, std, test))
        assert best_epoch < 199, "Early stopping should pick an epoch before the end."
    assert all(0.775 < a < 0.795 for a in aucs), (
        "Three seeds land between 0.784 and 0.787. Week 3's line: 0.779. Week 4's forest: "
        "0.765. The network edges ahead by less than its own seed-to-seed spread - with 65 "
        "test leavers, that is a tie.")
