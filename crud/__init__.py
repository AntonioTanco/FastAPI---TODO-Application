import sqlalchemy
from database import engine
from database.models import Notes
from schema.schemas import CreateNoteSchema, CreateNoteResponseSchema, UpdateNoteSchema, UpdateNoteStatusSchema

if sqlalchemy.inspect(engine).has_table(Notes.__tablename__) == True:

    log = f"The engine has checked that the {Notes.__tablename__} exist."

    print(log)

