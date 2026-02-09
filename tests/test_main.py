from fastapi.testclient import TestClient
from myapp.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Status": "OK"}

def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

