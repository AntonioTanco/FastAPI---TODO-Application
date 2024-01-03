import router.notes as notes

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from database.models import Notes
from database import db_dependency

app = FastAPI()
app.include_router(notes.router)

templates = Jinja2Templates(directory="./templates")

@app.get("/")
def read_root(request : Request, db : db_dependency):

    all_notes = db.query(Notes).all()

    
    return templates.TemplateResponse("index.html", {"request" : request, "name" : "Antonio T", "notes" : all_notes})

# Endpoint /note | Method: POST 
# Create a new note in the 'notes' database 

# @app.post("/note")
# async def create_note(request : NotesBase, db : db_dependency) -> NotesOutputBase:
    
#     new_note = models.Notes(note_title = request.note_title, note_contents = request.note_contents)
#     db.add(new_note)
#     db.commit()
#     db.refresh(new_note)

#     return new_note

# Endpoint /notes | Method: GET
# This endpoint will list all of the notes in the database no matter the status

# @app.get("/notes")
# async def get_notes(db : db_dependency):

#     all_notes = db.query(models.Notes).all()

#     return all_notes

# # Endpoint /notes/{status} | Method: GET
# # This endpoint will return all notes by 'status'.

# @app.get('/notes/{status}')
# async def get_notes_by_status(status : str , db : db_dependency):

#     all_notes_by_status = db.query(models.Notes).filter(models.Notes.note_status == status).all()

#     return all_notes_by_status

# # Endpoint /notes/{id} | Method: PUT
# # This endpoint will update an existing note only if the notes.id cant be found in the db.

# @app.put("/notes/{id}")
# async def update_notes(request : NotesOutputBase, id : int, db : db_dependency):

#     requested_note_id = exists().where(models.Notes.id == id)

#     doesNoteExist = db.query(requested_note_id).scalar()

#     print(doesNoteExist)

#     if not doesNoteExist:

#         raise HTTPException(status_code=404, detail="The Note.id you provided is not found.")
    
#     elif doesNoteExist:

#         db.query(models.Notes).filter(models.Notes.id == id)\
#         .update(values={models.Notes.note_title : request.note_title, 
#                         models.Notes.note_status : request.note_status, 
#                         models.Notes.note_contents : request.note_contents})
        
#         db.commit()

#         updated_note = db.query(models.Notes).filter(models.Notes.id == id).first()
    
#     return updated_note

# @app.delete("/note/{id}")
# async def delete_note(id : int, db : db_dependency):

#     requested_note = exists().where(models.Notes.id == id)

#     doesNoteExist = db.query(requested_note).scalar()

#     if not doesNoteExist:
       
#        raise HTTPException(status_code=404, detail="The Note.id you provided is not found.")
    
#     elif doesNoteExist:

#         db.query(models.Notes).filter(models.Notes.id == id).delete()

#         db.commit()

#         all_notes = db.query(models.Notes).all()

#         return {f"The note with an id of 'id':{id} was deleted from the database"}, all_notes