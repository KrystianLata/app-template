from pydantic import BaseModel
from datetime import datetime


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
