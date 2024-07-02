# main.py

from fastapi import FastAPI
from route import router as items_router
from config import engine, Base

# Ensure all tables are created
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Mount item routes
app.include_router(items_router)
