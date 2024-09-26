from typing import Optional
from pydantic import BaseModel


class ProductListValidate(BaseModel):
    id:int
    product_name: str
    category: str
    price: int
    description: Optional[str] = None
    date: int
    active: int
