from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Pokemon(Base):
    __tablename__ = 'pokemon'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    url = Column(String, unique=True, index=True)



    @classmethod
    def create_from_api(cls, db_session, name, url):
        pokemon = cls(name=name, url=url)
        db_session.add(pokemon)
        db_session.commit()
        db_session.refresh(pokemon)
        return pokemon



class PokemonCreate(BaseModel):
    name: str
    url: str
