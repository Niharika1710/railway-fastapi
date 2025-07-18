import os

DATABASE_URL = os.getenv("postgresql://postgres:rZeiafNLJxTNpZQlrinOfcAWnnFzQuOh@metro.proxy.rlwy.net:29641/railway")
print("DATABASE_URL:", DATABASE_URL)  # Add this line

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
