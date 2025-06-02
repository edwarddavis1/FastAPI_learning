from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)


def test_get_fruits_empty():
    """Test getting fruits when the database is empty."""
    # Reset the database
    from main import memory_db

    memory_db["fruits"] = []

    response = client.get("/fruits")
    assert response.status_code == 200
    assert response.json() == {"fruits": []}


def test_add_fruit():
    """Test adding a fruit to the database."""
    # Reset the database
    from main import memory_db

    memory_db["fruits"] = []

    fruit_data = {"name": "apple", "color": "green", "weight": 150.5}
    response = client.post("/fruits", json=fruit_data)
    assert response.status_code == 200
    assert response.json() == {"fruits": [fruit_data]}


def test_add_multiple_fruits():
    """Test adding multiple fruits to the database."""
    # Reset the database
    from main import memory_db

    memory_db["fruits"] = []

    fruits = [
        {"name": "apple", "color": "red", "weight": 150.0},
        {"name": "banana", "color": "yellow", "weight": 120.0},
        {"name": "orange", "color": "orange", "weight": 170.0},
    ]

    for fruit in fruits:
        response = client.post("/fruits", json=fruit)
        assert response.status_code == 200

    response = client.get("/fruits")
    assert response.status_code == 200
    assert response.json() == {"fruits": fruits}


def test_invalid_fruit_data():
    """Test adding a fruit with invalid data."""
    invalid_fruit = {
        "name": "apple",
        "color": "red",
        # Missing weight field
    }

    response = client.post("/fruits", json=invalid_fruit)
    assert response.status_code == 422  # Validation error
