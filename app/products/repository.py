from __future__ import annotations

from sqlalchemy.orm import Session
from app.products.models import Product

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self) -> list[Product]:
        return self.db.query(Product).all()
    
    def get_by_id(self, product_id: int) -> Product | None:
        return self.db.query(Product).filter(Product.id == product_id).first()
    
    def create(self, name: str, description: str | None, price: float, stock: int) -> Product:
        product = Product(name=name, description=description, price=price, stock=stock)
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product
    
    