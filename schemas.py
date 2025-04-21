from pydantic import BaseModel

class NoteCreate(BaseModel):
    name: str
    content: str



class Note(BaseModel):
    id: int
    name: str
    content: str

    class Config:
        orm_mode = True