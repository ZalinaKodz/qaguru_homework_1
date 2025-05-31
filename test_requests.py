import requests

BASE_URL = "http://127.0.0.1:8000/api"
headers = {'x-api-key': 'reqres-free-v1'}

def test_create_user():
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(f"{BASE_URL}/users", headers=headers, json=payload)
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    data = response.json()
    assert data["name"] == payload["name"], f"Expected name {payload['name']}, but got {data['name']}"
    assert data["job"] == payload["job"], f"Expected job {payload['job']}, but got {data['job']}"
    assert "id" in data, "Expected 'id' in response data"
    assert "createdAt" in data, "Expected 'createdAt' in response data"

def test_update_user_put():
    user_id = 2
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put(f"{BASE_URL}/users/{user_id}", headers=headers, json=payload)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    data = response.json()
    assert data["name"] == payload["name"], f"Expected name {payload['name']}, but got {data['name']}"
    assert data["job"] == payload["job"], f"Expected job {payload['job']}, but got {data['job']}"
    assert "updatedAt" in data, "Expected 'updatedAt' in response data"

def test_update_user_patch():
    user_id = 2
    payload = {
        "job": "rebel leader"
    }
    response = requests.patch(f"{BASE_URL}/users/{user_id}", headers=headers, json=payload)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    data = response.json()
    assert data["job"] == payload["job"], f"Expected job {payload['job']}, but got {data['job']}"
    assert "updatedAt" in data, "Expected 'updatedAt' in response data"

def test_delete_user():
    user_id = 2
    response = requests.delete(f"{BASE_URL}/users/{user_id}", headers=headers)
    assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"
    assert response.text == "", "Expected empty response text"