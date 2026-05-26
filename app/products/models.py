from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Numeric, Integer

from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    price: Mapped[float] = mapped_column(Numeric(10,2), nullable=False)
    stock: Mapped[int] = mapped_column(Integer, default=0)