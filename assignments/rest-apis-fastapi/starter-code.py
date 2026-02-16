"""
FastAPI REST API Starter Code

This is a starter template for building a REST API with FastAPI.
Complete the TODO sections to implement CRUD operations for items.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from uvicorn import run

# Initialize the FastAPI application
app = FastAPI(title="Item Store API", version="1.0.0")

# TODO: Define a Pydantic model for Item validation
# The model should include:
# - id (int): unique identifier (optional in requests, auto-generated)
# - name (str): item name
# - description (str): brief description
# - price (float): item price
# - in_stock (bool): availability status
class Item(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    in_stock: bool = True

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Laptop",
                "description": "High-performance laptop",
                "price": 999.99,
                "in_stock": True
            }
        }


# In-memory storage (for demonstration; replace with database in production)
items_db: List[Item] = []
next_id = 1


# TODO: Implement GET /items endpoint
# Should return all items in the database
@app.get("/items", response_model=List[Item], tags=["Items"])
def get_all_items(skip: int = 0, limit: int = 10) -> List[Item]:
    """Retrieve a list of all items with pagination support."""
    return items_db[skip:skip + limit]


# TODO: Implement GET /items/{item_id} endpoint
# Should return a single item by ID or raise 404 if not found
@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
def get_item(item_id: int) -> Item:
    """Retrieve a specific item by its ID."""
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {item_id} not found"
    )


# TODO: Implement POST /items endpoint
# Should create a new item and return it with status code 201
@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED, tags=["Items"])
def create_item(item: Item) -> Item:
    """Create a new item and store it in the database."""
    global next_id
    new_item = item.copy(update={"id": next_id})
    items_db.append(new_item)
    next_id += 1
    return new_item


# TODO: Implement PUT /items/{item_id} endpoint
# Should update an existing item or raise 404 if not found
@app.put("/items/{item_id}", response_model=Item, tags=["Items"])
def update_item(item_id: int, item_update: Item) -> Item:
    """Update an existing item by its ID."""
    for i, item in enumerate(items_db):
        if item.id == item_id:
            updated_item = item_update.copy(update={"id": item_id})
            items_db[i] = updated_item
            return updated_item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {item_id} not found"
    )


# TODO: Implement DELETE /items/{item_id} endpoint
# Should delete an item or raise 404 if not found
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Items"])
def delete_item(item_id: int) -> None:
    """Delete an item by its ID."""
    for i, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(i)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {item_id} not found"
    )


# Health check endpoint
@app.get("/", tags=["Health"])
def root():
    """Health check endpoint."""
    return {"message": "Item Store API is running", "docs": "/docs"}


if __name__ == "__main__":
    # Run the server with: python3 starter-code.py
    # Or with uvicorn: uvicorn starter-code:app --reload
    run(app, host="0.0.0.0", port=8000)
