import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ✅ Correctly fetch the DATABASE_URL environment variable
DATABASE_URL = os.environ["postgresql://postgres:rZeiafNLJxTNpZQlrinOfcAWnnFzQuOh@metro.proxy.rlwy.net:29641/railway"]

print("DATABASE_URL:", repr(DATABASE_URL))  # You can keep this for debugging.

# ✅ Create the SQLAlchemy engine using the retrieved URL
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
