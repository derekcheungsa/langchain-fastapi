import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

_host = os.getenv('DB_HOST', 'localhost')
_port = os.getenv('DB_PORT', '3306')
_user = os.getenv('DB_USER', 'root')
_password = os.getenv('DB_PASSWORD', '')
_schema = os.getenv('DB_SCHEMA', 'academy')

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{_user}:{_password}@{_host}:{_port}/{_schema}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
