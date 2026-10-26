import pytest
from fastapi.testclient import TestClient
from app import app, ORDERS

@pytest.fixture(autouse=True)
def reset_orders():
    ORDERS.clear()
    ORDERS["4500012345"] = {"status": "OPEN", "delivery_date": None}

client = TestClient(app)

def test_iso_confirmation():
    response = client.post("/confirmations", json={
        "po_number": "4500012345", "delivery_date": "2026-11-15"
    })
    assert response.status_code == 200
    assert response.json() == {
        "po_number": "4500012345", "status": "CONFIRMED",
        "delivery_date": "2026-11-15"
    }

def test_unknown_order():
    response = client.post("/confirmations", json={
        "po_number": "unknown", "delivery_date": "2026-11-15"
    })
    assert response.status_code == 404
