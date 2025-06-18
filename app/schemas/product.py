from typing import List, Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    type: str
    sku: str
    image_url: Optional[str] = None
    description: Optional[str] = None
    quantity: int
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class ProductList(BaseModel):
    products: List[Product]
    total: int
    skip: int
    limit: int

    class Config:
        orm_mode = True