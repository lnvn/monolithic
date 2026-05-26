from __future__ import annotations

from pydantic import BaseModel
from decimal import Decimal
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    stock: int = 0

class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: Decimal
    stock: int

    model_config = {"from_attributes": True}
