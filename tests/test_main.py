from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chat_endpoint_works():
    response = client.post("/chat", json={"message": "Qual o presságio de um eclipse?"})
    assert response.status_code == 200
    data = response.json()
    assert "response" in data or "error" in data