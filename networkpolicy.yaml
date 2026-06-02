from fastapi.testclient import TestClient
from platform_demo.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_ready():
    response = client.get("/ready")
    assert response.status_code == 200
    assert "dependencies" in response.json()


def test_platform_contract():
    response = client.get("/platform-contract")
    assert response.status_code == 200
    assert "required_contracts" in response.json()


def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "platform_demo_http_requests_total" in response.text
