import os
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.base import Engine


DB_CREDENTIALS = json.loads(os.getenv("DB_CREDENTIALS"))

def connect_with_connector() -> Engine:
    engine = create_engine(f"postgresql://{DB_CREDENTIALS['db_user']}:{DB_CREDENTIALS['db_pass']}@{DB_CREDENTIALS['db_host']}:5432/postgres")
    return engine

SessionLocal = sessionmaker(bind=connect_with_connector())

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()