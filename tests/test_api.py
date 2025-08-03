import pytest
from fastapi.testclient import TestClient
import requests

BASE_URL = "https://reqres.in/api"
HEADERS = {"x-api-key": "reqres-free-v1"}

def test_root():
    response = requests.get(f"{BASE_URL}/users", headers=HEADERS)
    assert response.status_code == 200

def test_post_endpoint():
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
    assert response.status_code == 201

def test_not_found():
    response = requests.get(f"{BASE_URL}/nonexistent", headers=HEADERS)
    assert response.status_code == 404

def test_invalid_method():
    response = requests.put(f"{BASE_URL}/users/2", headers=HEADERS)
    # PUT is allowed on /users/2, but not on /users, so let's test /users
    response_invalid = requests.put(f"{BASE_URL}/users", headers=HEADERS)
    assert response_invalid.status_code in (405, 404)