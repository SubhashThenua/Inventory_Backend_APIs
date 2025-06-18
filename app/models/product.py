from sqlalchemy import Column, Integer, String, Float, Text
from app.database.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50))
    sku = Column(String(50), unique=True)
    image_url = Column(String(255))
    description = Column(Text)
    quantity = Column(Integer, default=0)
    price = Column(Float, nullable=False)