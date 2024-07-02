import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# PostgreSQL database URL from environment variable
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)
