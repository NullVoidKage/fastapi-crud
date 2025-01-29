import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Item
from app.database import SessionLocal, engine

# Create the database tables for testing
Item.metadata.create_all(bind=engine)

# Initialize the TestClient
client = TestClient(app)

# Dependency override to use the test database
@pytest.fixture
def db_session():
    db = SessionLocal()
    yield db
    db.close()

# Test for Create Item
def test_create_item(db_session):
    item_data = {"name": "Test Item", "description": "This is a test item"}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]

# Test for Read Item
def test_read_item(db_session):
    item_data = {"name": "Test Item", "description": "This is a test item"}
    response = client.post("/items/", json=item_data)
    item_id = response.json()["id"]

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]

# Test for Update Item
def test_update_item(db_session):
    item_data = {"name": "Test Item", "description": "This is a test item"}
    response = client.post("/items/", json=item_data)
    item_id = response.json()["id"]

    updated_data = {"name": "Updated Item", "description": "Updated description"}
    response = client.put(f"/items/{item_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == updated_data["name"]
    assert data["description"] == updated_data["description"]

# Test for Delete Item
def test_delete_item(db_session):
    item_data = {"name": "Test Item", "description": "This is a test item"}
    response = client.post("/items/", json=item_data)
    item_id = response.json()["id"]

    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Item deleted"

    # Ensure the item doesn't exist anymore
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 404
