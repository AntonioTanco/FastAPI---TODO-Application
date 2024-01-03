from crud import Notes
from crud import UpdateNoteSchema, UpdateNoteStatusSchema
from database import db_dependency

def update_note(request : UpdateNoteSchema, id : int,  db : db_dependency):

    _update_on_requested_note = db.query(Notes).filter(Notes.id == id)\
            .update(values={Notes.note_title : request.note_title, 
                            Notes.note_status : request.note_status, 
                            Notes.note_contents : request.note_contents})
    
    db.commit()
    
    return _update_on_requested_note

def update_note_status(request : UpdateNoteStatusSchema, id : int, db : db_dependency):

    _update_on_requested_note_status = db.query(Notes).filter(Notes.id == id)\
            .update(values={Notes.note_status : request.note_status})
        
    db.commit()

    return _update_on_requested_note_status