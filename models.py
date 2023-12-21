from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, literal
from database import Base
from typing import Literal

#Note_Status = Literal["WiP", "On Hold", "Completed", "New"]
#Note_Status_Enum = Enum(*Note_Status, name="note_status")

class Notes(Base):
    
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    note_title = Column(String(64))
    note_status = Column(Enum("New", "WiP", "On Hold", "Completed", name="note_status"), nullable=False, default="New")
    note_contents = Column(String(500))