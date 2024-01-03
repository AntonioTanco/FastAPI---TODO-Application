from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, literal, DateTime
from .database import Base
from datetime import datetime
# class Users(Base):

#     __tablename__ = "users"
    
#     id = Column(Integer, primary_key=True)
#     username = Column(String(64), index=True, unique=True)
#     email = Column(String(120), index=True, unique=True)

class Notes(Base):
    
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    note_title = Column(String(64), nullable=False)
    note_status = Column(Enum("New", "WiP", "On Hold", "Completed", name="note_status"), nullable=False, default="New")
    note_contents = Column(String(500))

