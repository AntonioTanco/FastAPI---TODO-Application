from pydantic import BaseModel, Field, ConfigDict
from enum import Enum
from typing import Union, Annotated, List, Optional

class NoteEnum(str, Enum):
    new = 'New'
    wip = 'WiP'
    on_hold = 'On Hold'
    completed = 'Completed'

class CreateNoteSchema(BaseModel):
    note_title : str = Field(title='Title', description='Title of a note', default="Enter Note Title", min_length=6, max_length=64)
    note_contents : str = Field(default="Enter Note Contents", description='Contents of the note', max_length=500)

    model_config = ConfigDict(use_enum_values=True, json_schema_extra = {
            "examples": [
                {
                    "note_tile": "Insert Note Title",
                    "note_contents": "Insert Note Contents",
                }
            ]
        }
        )

    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "note_tile": "Insert Note Title",
    #                 "note_contents": "Insert Note Contents",
    #             }
    #         ]
    #     }
    # }

class CreateNoteResponseSchema(BaseModel):
    note_title : str = Field(default="Enter a note title")
    note_status : Optional[NoteEnum] = Field(default=NoteEnum.new, examples=["New", "WiP", "On Hold", "Completed"])
    note_contents : str = Field(default="Enter the contents of the note")

class UpdateNoteSchema(BaseModel):
    note_title : str = Field(min_length=6,max_length=64)
    note_status : NoteEnum = Field(examples=["New", "WiP", "On Hold", "Completed"])
    note_contents : str = Field(max_length=500)

class UpdateNoteStatusSchema(BaseModel):
    note_status : NoteEnum = Field(examples=["New", "WiP", "On Hold", "Completed"])

    model_config = ConfigDict(use_enum_values=True, json_schema_extra = {
            "examples": [
                {
                    "note_status": "New",
                }
            ]
        })

class UpdateNoteStatusResponseSchema(BaseModel):
    note_status : NoteEnum = Field(examples=["New", "WiP", "On Hold", "Completed"])

class CreateUserSchema(BaseModel):
    username : str = Field(min_length=8, nullable=False, unique=True)
    email_address : str = Field(min_length=6, nullable=False)
    pwd : str = Field(min_length=8)

class CreateUserResponseSchema(BaseModel):
    username : str = Field(min_length=8, nullable=False, unique=True)
    email_address : str = Field(min_length=6, nullable=False)