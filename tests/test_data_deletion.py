from __future__ import annotations

from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Ensure workspace root is on path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.main import app

client = TestClient(app)


def test_data_deletion_get():
    resp = client.get("/data-deletion", params={"platform": "facebook", "user_id": "123"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "received"
    assert "confirmation_code" in data
    assert "url" in data


def test_data_deletion_post():
    payload = {"platform": "instagram", "user_id": "abc"}
    resp = client.post("/data-deletion", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "received"
    assert "confirmation_code" in data
    assert "url" in data


def test_data_deletion_status():
    # first get a code
    resp = client.get("/data-deletion", params={"platform": "facebook"})
    code = resp.json()["confirmation_code"]
    # check status
    resp2 = client.get(f"/data-deletion/status/{code}")
    assert resp2.status_code == 200
    data = resp2.json()
    assert data["confirmation_code"] == code
    assert data["status"] in {"in_progress", "completed"}
