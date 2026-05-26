from __future__ import annotations

from sqlalchemy.orm import Session

from app.products.repository import ProductRepository
from app.products.schemas import ProductCreate
from app.products.models import Product

class ProductService:
    def __init__(self, db: Session):
        self.repo = ProductRepository(db)
    
    def get_all(self) -> list[Product]:
        return self.repo.get_all()
    
    def get_by_id(self, product_id: int) -> Product:
        product = self.repo.get_by_id(product_id)
        if product is None:
            raise ValueError(f"Product {product_id} not found")
        return product
    
    def create(self, data: ProductCreate) -> Product:
        return self.repo.create(
            name=data.name,
            description=data.description,
            price=float(data.price),
            stock=data.stock,
        )