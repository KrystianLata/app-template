from fastapi import APIRouter
from app.models.item import Item, ItemCreate
from datetime import datetime

router = APIRouter()

# Simulated database
items_db = []


@router.get("/items/", response_model=list[Item])
async def get_items():
    """
    Get all items from the database.
    """
    return items_db


@router.post("/items/", response_model=Item)
async def create_item(item: ItemCreate):
    """
    Create a new item.
    """
    new_item = Item(id=len(items_db) + 1, **item.model_dump(), created_at=datetime.now())
    items_db.append(new_item)
    return new_item
