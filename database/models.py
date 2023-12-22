from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, literal
from database import Base
from typing import Literal

class Notes(Base):
    
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    note_title = Column(String(64), nullable=False)
    note_status = Column(Enum("New", "WiP", "On Hold", "Completed", name="note_status"), nullable=False, default="New")
    note_contents = Column(String(500))