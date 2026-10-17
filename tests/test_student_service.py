import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Enterprise Student Record" in response.data

def test_get_students(client):
    response = client.get('/students')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) >= 2

def test_add_student(client):
    new_data = {"name": "Charlie Brown", "course": "Cloud Computing", "gpa": 3.9}
    response = client.post('/students', json=new_data)
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Charlie Brown"
