This project provides a FastAPI-based RESTful API for managing Pokémon data, integrating with the PokeAPI for data retrieval.

Features

    GET /api/v1/pokemon/: Retrieves a list of all Pokémon stored in the database.
    GET /api/v1/pokemon//{id}: Retrieves a specific Pokémon by its ID.
    GET /api/v1/pokemon//search/{name} .
Installation

    Clone the repository:

    bash

git clone https://github.com/sanjaykadel/pokemon.git
cd pokemon

Install dependencies:

#bash

pip install -r requirements.txt

Set up the PostgreSQL database:

    Create a .env file and define your PostgreSQL database URL:


DATABASE_URL=postgresql://username:password@localhost/dbname
