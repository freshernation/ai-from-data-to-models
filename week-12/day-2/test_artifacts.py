import json


def bundle(tmp_path):
    (tmp_path / "model.bin").write_bytes(b"weights")
    (tmp_path / "vocab.json").write_text('{"not": 2}')
    return tmp_path


def test_fingerprint(load, tmp_path):
    ar = load("artifacts.py")
    f = tmp_path / "x"
    f.write_bytes(b"abc")
    assert ar.fingerprint(f) == "ba7816bf8f01cfea"


def test_manifest_round_trip(load, tmp_path):
    ar = load("artifacts.py")
    m = ar.write_manifest(bundle(tmp_path), "1.2.0", {"auc": 0.78})
    assert set(m["files"]) == {"model.bin", "vocab.json"} and m["version"] == "1.2.0"
    assert ar.read_manifest(tmp_path) == m == json.loads((tmp_path / "manifest.json").read_text())
    assert ar.verify(tmp_path) == []


def test_finding_one_changed_byte_is_caught(load, tmp_path):
    ar = load("artifacts.py")
    ar.write_manifest(bundle(tmp_path), "1.0.0", {})
    (tmp_path / "model.bin").write_bytes(b"weightz")
    (tmp_path / "extra.pt").write_bytes(b"?")
    (tmp_path / "vocab.json").unlink()
    assert ar.verify(tmp_path) == ["extra.pt", "model.bin", "vocab.json"], (
        "One changed byte, one stray file, one missing file - all three named. A service "
        "that checks this at start-up can never run weights nobody evaluated.")
