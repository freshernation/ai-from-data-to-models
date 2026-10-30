from shoplab import images


def test_dense_net(load):
    st = load("shift_test.py")
    import torch
    assert st.dense_net()(torch.zeros(3, 1, 16, 16)).shape == (3, 4)


def test_finding_move_the_mug_and_the_dense_network_is_lost(load):
    st = load("shift_test.py")
    r = st.compare(images.load())
    assert r["dense"]["params"] == 16708 and r["cnn"]["params"] == 1316
    assert r["dense"]["centred"] > 0.97 and r["cnn"]["centred"] > 0.97, \
        "On photos framed like the training ones, both are near perfect."
    assert r["dense"]["shifted"] < 0.6, (
        "Move the product up to three pixels further than in training and the dense network "
        "drops to about 46%: it learned which PIXELS light up, not what a mug looks like.")
    assert r["cnn"]["shifted"] > 0.97, \
        "The CNN, with a twelfth of the weights, is still near 100%."
