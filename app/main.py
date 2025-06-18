from fastapi import FastAPI
from app.routes import auth, products
from app.database import base
from app.database.session import engine

base.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(products.router)