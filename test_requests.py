import requests

BASE_URL = "http://127.0.0.1:8000/api"

def test_get_user_valid():
    user_id = 1
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == user_id
    assert "email" in data["data"]
    assert "first_name" in data["data"]
    assert "last_name" in data["data"]
    assert "avatar" in data["data"]

def test_get_user_invalid_id_type():
    response = requests.get(f"{BASE_URL}/users/abc")
    assert response.status_code == 422

def test_get_user_not_found():
    user_id = 99
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User not found"

def test_user_data_fields():
    user_id = 1
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    data = response.json()["data"]
    expected_fields = {"id", "email", "first_name", "last_name", "avatar"}
    assert expected_fields.issubset(data.keys())