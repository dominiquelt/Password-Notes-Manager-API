from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Notes
from schemas import NoteCreate, Note
from typing import List



app = FastAPI()

def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/notes", response_model=Note)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = Notes(name=note.name, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@app.get("/notes/", response_model=List[Note])
def read_note(db: Session = Depends(get_db)):
    notes = db.query(models.Notes).all()
    return notes

@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id= int, db: Session = Depends(get_db)):
    note = db.query(models.Notes).filter(models.Notes.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(note)
    db.commit
    return

@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id=int, updated_note= NoteCreate, db: Session = Depends(get_db)):
    note = db.query(models.Notes).filter(models.Notes.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    note.name = updated_note.name
    note.content = updated_note.content
    db.commit()
    db.refresh(note)
    return note



    

