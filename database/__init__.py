
from fastapi import Depends
from typing import Annotated
from .database import engine, SessionLocal
from .models import Base
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import exists, update, values, select


Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]