from fastapi.testclient import TestClient
from src.main import app
from datetime import datetime

client = TestClient(app)

def test_post_sensor_dados():
    payload = {
        "sensor_id": "SENSOR_MUCURIPE_01",
        "chuva_mm": 60,
        "data_hora": datetime.now().isoformat()
    }
    response = client.post("/sensores/dados", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["alerta"] == "risco_alagamento"

def test_get_alertas():
    response = client.get("/alertas/SENSOR_MUCURIPE_01")
    assert response.status_code == 200
    data = response.json()
    assert "alertas" in data
