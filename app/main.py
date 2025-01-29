from fastapi import FastAPI, HTTPException
from app import models, schemas, crud, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)


@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate):
    return crud.create_item(item)


@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int):
    item = crud.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemUpdate):
    return crud.update_item(item_id, item)


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return crud.delete_item(item_id)
