from pydantic import BaseModel, ConfigDict
from typing import List
from enum import Enum


class State(Enum):
    available: str = 'available'
    pending: str = 'pending'
    sold: str = 'sold'


class Category(BaseModel):
    id: int
    name: str


class Tag(BaseModel):
    id: int
    name: str


class Item(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    id: int
    category: Category
    name: str
    photoUrls: List[str]
    tags: List[Tag]
    status: State









