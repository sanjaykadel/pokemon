from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Pokemon
import requests

def get_all_pokemon(db: Session):
    return db.query(Pokemon).all()

def fetch_pokemon_data(db: Session):
    url = "https://pokeapi.co/api/v2/pokemon?limit=1000"
    all_pokemon = []
    next_url = url

    # Iterate through paginated results until all Pokémon are fetched
    while next_url:
        response = requests.get(next_url)
        if response.status_code == 200:
            pokemon_data = response.json()
            results = pokemon_data.get('results', [])

            for result in results:
                name = result['name']
                url = result['url']
                pokemon = Pokemon(name=name, url=url)
                db.add(pokemon)
                all_pokemon.append(pokemon)

            # Check if there is another page of results
            next_url = pokemon_data.get('next')
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch Pokemon data")

    db.commit()

    return get_all_pokemon(db)

def get_pokemon_by_id(db: Session, pokemon_id: int):
    pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()
    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

def search_pokemon_by_name(db: Session, name: str):
    pokemon = db.query(Pokemon).filter(Pokemon.name.ilike(f"%{name}%")).all()
    if not pokemon:
        raise HTTPException(status_code=404, detail=f"No Pokémon found with name containing '{name}'")
    return pokemon
