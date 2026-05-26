from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.products.schemas import ProductCreate, ProductResponse
from app.products.service import ProductService
from app.dependencies import get_db, get_current_user

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=list[ProductResponse])
def get_all(db: Session = Depends(get_db)):
    return ProductService(db).get_all()

@router.get("/{product_id}", response_model=ProductResponse)
def get_one(product_id: int, db: Session = Depends(get_db)):
    try:
        return ProductService(db).get_by_id(product_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", response_model=ProductResponse)
def create(
    data: ProductCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    return ProductService(db).create(data)