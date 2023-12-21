from typing import Union, Annotated, List, Optional
import models

from database import engine, SessionLocal
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.sql.expression import exists, update, values, select
from enum import Enum
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field, ConfigDict

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class ValidationError(BaseModel):
    loc: List[str] = Field(description="Location of the field stated in a list format")
    msg: str = Field(description="A message that tells what the error is about")
    type: str = Field(description="An identifier that categorizes the type of the error")

class HTTPValidationError(BaseModel):
    detail: List[ValidationError] = Field(...)


class NoteEnum(str, Enum):
    new = 'New'
    wip = 'WiP'
    on_hold = 'On Hold'
    completed = 'Completed'

class NotesBase(BaseModel):
    note_title : str = Field(title='Title', description='Title of a note', examples=["12/24 Note", "First Note Of The Day"])
    note_contents : str = Field(description='Contents of the note', examples=["Buy eggs and milk", "Docters appointment today @ 3 PM"])

    model_config = ConfigDict(use_enum_values=True)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "note_tile": "Insert Note Title",
                    "note_contents": "Insert Note Contents",
                }
            ]
        }
    }

class NotesOutputBase(BaseModel):
    note_title : str
    note_status : Optional[NoteEnum] = Field(default=NoteEnum.new, examples=["New", "WiP", "On Hold", "Completed"])
    note_contents : str

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Endpoint /note | Method: POST 
# Create a new note in the 'notes' database 

@app.post("/note", responses={422: {"model": HTTPValidationError}})
async def create_note(request : NotesBase, db : db_dependency) -> NotesOutputBase:
    
    new_note = models.Notes(note_title = request.note_title, note_contents = request.note_contents)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note

# Endpoint /notes | Method: GET
# This endpoint will list all of the notes in the database no matter the status

@app.get("/notes")
async def get_notes(db : db_dependency):

    all_notes = db.query(models.Notes).all()

    return all_notes

# Endpoint /notes/{status} | Method: GET
# This endpoint will return all notes by 'status'.

@app.get('/notes/{status}')
async def get_notes_by_status(status : str , db : db_dependency):

    all_notes_by_status = db.query(models.Notes).filter(models.Notes.note_status == status).all()

    return all_notes_by_status

# Endpoint /notes/{id} | Method: PUT
# This endpoint will update an existing note only if the notes.id cant be found in the db.

@app.put("/notes/{id}")
async def update_notes(request : NotesOutputBase, id : int, db : db_dependency):

    requested_note_id = exists().where(models.Notes.id == id)

    doesNoteExist = db.query(requested_note_id).scalar()

    print(doesNoteExist)

    if not doesNoteExist:

        raise HTTPException(status_code=404, detail="The Note.id you provided is not found.")
    
    elif doesNoteExist:

        db.query(models.Notes).filter(models.Notes.id == id)\
        .update(values={models.Notes.note_title : request.note_title, 
                        models.Notes.note_status : request.note_status, 
                        models.Notes.note_contents : request.note_contents})
        
        db.commit()

        updated_note = db.query(models.Notes).filter(models.Notes.id == id).first()
    
    return updated_note

@app.delete("/note/{id}")
async def delete_note(id : int, db : db_dependency):

    requested_note = exists().where(models.Notes.id == id)

    doesNoteExist = db.query(requested_note).scalar()

    if not doesNoteExist:
       
       raise HTTPException(status_code=404, detail="The Note.id you provided is not found.")
    
    elif doesNoteExist:

        db.query(models.Notes).filter(models.Notes.id == id).delete()

        db.commit()

        all_notes = db.query(models.Notes).all()

        return {f"The note with an id of 'id':{id} was deleted from the database"}, all_notes