from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from typing import Dict
from app.core.pagination import pagination_params
from app.schemas.product import Product, ProductList
from app.schemas.product import Product, ProductCreate
from app.models.product import Product as DBProduct
from app.database.session import get_db
from app.core.security import get_current_user

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=Product)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    db_product = db.query(DBProduct).filter(DBProduct.sku == product.sku).first()
    if db_product:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="SKU already exists"
        )
    
    new_product = DBProduct(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.put("/{product_id}/quantity", response_model=Product)
def update_product_quantity(
    product_id: int,
    quantity_data: dict,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    db_product = db.query(DBProduct).filter(DBProduct.id == product_id).first()
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    try:
        new_quantity = quantity_data["quantity"]
        if not isinstance(new_quantity, int) or new_quantity < 0:
            raise ValueError
    except (KeyError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Quantity must be a positive integer"
        )
    
    db_product.quantity = new_quantity
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/", response_model=ProductList)
def get_products(
    pagination: Dict = Depends(pagination_params),
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    skip = pagination["skip"]
    limit = pagination["limit"]
    
    total = db.query(DBProduct).count()
    
    products = db.query(DBProduct).offset(skip).limit(limit).all()
    
    return {
        "products": products,
        "total": total,
        "skip": skip,
        "limit": limit
    }

