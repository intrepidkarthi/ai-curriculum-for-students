import os, sys
from fastapi.testclient import TestClient

# Make app importable when running from repo root
CURRENT_DIR = os.path.dirname(__file__)
APP_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "app"))
sys.path.append(APP_DIR)

from main import app  # noqa: E402

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_sum_ok():
    r = client.get("/sum", params={"a": 2, "b": 5})
    assert r.status_code == 200
    assert r.json() == {"sum": 7}


def test_sum_missing_param():
    r = client.get("/sum", params={"a": 1})
    assert r.status_code == 422
    assert "Missing query params" in r.json()["detail"]
