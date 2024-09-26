from database import Base
from typing import Optional
from sqlalchemy import String, Integer,Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column


class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_name: Mapped[str] = mapped_column(String(32))
    category: Mapped[str] = mapped_column(String(16))
    price: Mapped[int] = mapped_column(Integer, default=0)
    description: Mapped[Optional[str]]
    date: Mapped[int] = mapped_column(Integer,default=0)
    active: Mapped[bool] = mapped_column(Boolean, default=0)