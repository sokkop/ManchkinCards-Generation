from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from backend.app.core.config import get_settings

settings = get_settings()
DATABASE_URL = settings.database_url

print(DATABASE_URL)
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the .env file")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()