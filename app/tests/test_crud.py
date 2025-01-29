# from fastapi.testclient import TestClient
# from app.main import app
# from app import models, schemas
# from app.database import SessionLocal, engine
#
# # Create the database tables
# models.Base.metadata.create_all(bind=engine)
#
# client = TestClient(app)
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
# def test_create_item():
#     item_data = {"name": "Test Item", "description": "A test item"}
#     response = client.post("/items/", json=item_data)
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == item_data["name"]
#     assert data["description"] == item_data["description"]
#
# def test_read_item():
#     item_data = {"name": "Test Item", "description": "A test item"}
#     response = client.post("/items/", json=item_data)
#     item_id = response.json()["id"]
#     response = client.get(f"/items/{item_id}")
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == item_data["name"]
#     assert data["description"] == item_data["description"]
#
# def test_update_item():
#     item_data = {"name": "Test Item", "description": "A test item"}
#     response = client.post("/items/", json=item_data)
#     item_id = response.json()["id"]
#     updated_data = {"name": "Updated Item", "description": "An updated test item"}
#     response = client.put(f"/items/{item_id}", json=updated_data)
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == updated_data["name"]
#     assert data["description"] == updated_data["description"]
#
# def test_delete_item():
#     item_data = {"name": "Test Item", "description": "A test item"}
#     response = client.post("/items/", json=item_data)
#     item_id = response.json()["id"]
#     response = client.delete(f"/items/{item_id}")
#     assert response.status_code == 200
#     response = client.get(f"/items/{item_id}")
#     assert response.status_code == 404
