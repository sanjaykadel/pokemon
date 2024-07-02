from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from config import SessionLocal
import controller

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/api/v1/pokemon/")
def fetch_pokemon(db: Session = Depends(get_db)):
    existing_pokemon = controller.get_all_pokemon(db)
    if existing_pokemon:
        return { "data": existing_pokemon}

    all_pokemon = controller.fetch_pokemon_data(db)
    return {"data": all_pokemon}

@router.get("/api/v1/pokemon/{pokemon_id}")
def get_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    return controller.get_pokemon_by_id(db, pokemon_id)

@router.get("/api/v1/pokemon/search/")
def search_pokemon(name: str = Query(None, min_length=1), db: Session = Depends(get_db)):
    if name is None:
        raise HTTPException(status_code=400, detail="Please provide a valid 'name' parameter.")
    return controller.search_pokemon_by_name(db, name)
