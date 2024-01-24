from index import app
import json

def test_hello():
    client = app.test_client()
    response = client.get("/")
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['message'] == 'Hey there Python'

def test_health():
    client = app.test_client()
    response = client.get("/health")
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['status'] == 'ok'
