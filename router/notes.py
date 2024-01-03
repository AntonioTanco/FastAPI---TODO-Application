from fastapi import APIRouter, HTTPException
from database import db_dependency, exists, update, values
from database.models import Notes
from crud.crud import update_note, update_note_status
from schema.schemas import CreateNoteSchema, CreateNoteResponseSchema, UpdateNoteSchema, UpdateNoteStatusSchema, UpdateNoteStatusResponseSchema

router = APIRouter()

# All HTTP GET Methods
#
# This endpoint will list all of the notes in the database no matter the status
@router.get("/notes", tags=["notes"])
async def get_notes(db : db_dependency):

    all_notes = db.query(Notes).all()

    return all_notes

# This endpoint will return all notes by 'status'.
@router.get('/notes/{status}', tags=["notes"])
async def get_notes_by_status(status : str , db : db_dependency):

    all_notes_by_status = db.query(Notes).filter(Notes.note_status == status).all()

    return all_notes_by_status

@router.get('/note/{id}', tags=["notes"])
async def get_note_by_id(id : int, db : db_dependency):

    requested_note_id = exists().where(Notes.id == id)

    doesNoteExist = db.query(requested_note_id).scalar()

    if not doesNoteExist:
       
       raise HTTPException(status_code=404, detail="The Note.id you provided is not found.")
    
    elif doesNoteExist:

        all_notes_by_id = db.query(Notes).filter(Notes.id == id).first()

    return all_notes_by_id

# All HTTP Post Methods

# Create a new note in the 'notes' database 
@router.post("/note", tags=["notes"])
async def create_note(request : CreateNoteSchema, db : db_dependency) -> CreateNoteResponseSchema:
    
    new_note = Notes(note_title = request.note_title, note_contents = request.note_contents)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note

# All HTTP Put Methods

# This endpoint will update an existing note only if the notes.id cant be found in the db.
@router.put("/notes/{id}", tags=["notes"])
async def update_notes(request : UpdateNoteSchema, id : int, db : db_dependency):

    #Checks if note exist
    requested_note_id = exists().where(Notes.id == id)

    doesNoteExist = db.query(requested_note_id).scalar()

    print(doesNoteExist)

    if not doesNoteExist:

        raise HTTPException(status_code=404, detail="The Note.id you provided is not found.")
    
    elif doesNoteExist:
            
            #updates requested note
            update_note(request, id, db)

            #queries the DB for the updated note
            updated_note = db.query(Notes).filter(Notes.id == id).first()
    
    return updated_note

@router.put("/note/{id}/status", tags=["notes"])
async def update_note_status_by_id(request : UpdateNoteStatusSchema, id : int, db : db_dependency):

    requested_note = exists().where(Notes.id == id)

    doesNoteExist = db.query(requested_note).scalar()

    if not doesNoteExist:

        raise HTTPException(status_code=404, detail="The Note.id you provided is not found.")
    
    elif doesNoteExist:

        #updates requested note status
        update_note_status(request, id, db)

        #queries the updated note
        updated_note_status = db.query(Notes).filter(Notes.id == id).first()

    return {f"Successfully Changed the status of Note: {id} to {request.note_status}"}, updated_note_status

# All HTTP Delete Methods

# This endpoint will delete an existing note in the database only if the notes.id exist in the db.
@router.delete("/note/{id}", tags=["notes"])
async def delete_note(id : int, db : db_dependency):

    requested_note = exists().where(Notes.id == id)

    doesNoteExist = db.query(requested_note).scalar()

    if not doesNoteExist:
       
       raise HTTPException(status_code=404, detail="The Note.id you provided is not found.")
    
    elif doesNoteExist:

        db.query(Notes).filter(Notes.id == id).delete()

        db.commit()

        all_notes = db.query(Notes).all()

        return {f"The note with an id of 'id':{id} was deleted from the database"}, all_notes