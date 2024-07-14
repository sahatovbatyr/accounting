import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import DB_DRIVER, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

# DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/db_accounting"
# DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/db_accounting"
DATABASE_URL = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = sqlalchemy.create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

metadata = sqlalchemy.MetaData()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



