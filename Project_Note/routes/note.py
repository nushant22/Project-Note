from fastapi import APIRouter, Request, Form, Depends, Query, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import or_
from pathlib import Path
from typing import List

from Project_Note.database.db import SessionLocal
from Project_Note.database.models import Note
from Project_Note.schemas.note import NoteCreate, NoteUpdate, NoteResponse


router = APIRouter(prefix="/notes", tags=["Notes"])
templates_dir = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_notes(request: Request, search: str = None, category: str = None, db: Session = Depends(get_db)):
    query = db.query(Note)
    
    if search:
        query = query.filter(or_(
            Note.title.ilike(f"%{search}%"),
            Note.content.ilike(f"%{search}%")
        ))
    
    if category:
        query = query.filter(Note.category == category)
    
    notes = query.order_by(Note.updated_at.desc()).all()
    categories = db.query(Note.category).distinct().all()
    categories = [cat[0] for cat in categories if cat[0]]
    
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request, 
            "notes": notes,
            "categories": categories,
            "search": search,
            "selected_category": category
        }
    )

@router.post("/add")
def add_note(
    title: str = Form(...),
    content: str = Form(...),
    category: str = Form("General"),
    db: Session = Depends(get_db)
):
    note = Note(title=title, content=content, category=category)
    db.add(note)
    db.commit()
    return RedirectResponse(url="/notes/", status_code=303)

@router.get("/edit/{note_id}")
def edit_note_page(note_id: int, request: Request, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        return RedirectResponse(url="/notes/", status_code=303)
    categories = db.query(Note.category).distinct().all()
    categories = [cat[0] for cat in categories if cat[0]]
    return templates.TemplateResponse(
        "edit.html",
        {"request": request, "note": note, "categories": categories}
    )

@router.post("/update/{note_id}")
def update_note(
    note_id: int,
    title: str = Form(...),
    content: str = Form(...),
    category: str = Form("General"),
    db: Session = Depends(get_db)
):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        return RedirectResponse(url="/notes/", status_code=303)
    note.title = title
    note.content = content
    note.category = category
    db.commit()
    return RedirectResponse(url="/notes/", status_code=303)

@router.get("/delete/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        db.delete(note)
        db.commit()
    return RedirectResponse(url="/notes/", status_code=303)

# API Routes (JSON)
@router.get("/api/all", response_model=List[NoteResponse])
def api_get_all_notes(db: Session = Depends(get_db)):
    return db.query(Note).order_by(Note.updated_at.desc()).all()

@router.get("/api/search")
def api_search_notes(q: str = Query(...), db: Session = Depends(get_db)):
    notes = db.query(Note).filter(or_(
        Note.title.ilike(f"%{q}%"),
        Note.content.ilike(f"%{q}%")
    )).all()
    return notes

@router.get("/api/{note_id}", response_model=NoteResponse)
def api_get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.post("/api/create", response_model=NoteResponse)
def api_create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = Note(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@router.put("/api/update/{note_id}", response_model=NoteResponse)
def api_update_note(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    update_data = note.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_note, key, value)
    db.commit()
    db.refresh(db_note)
    return db_note

@router.delete("/api/delete/{note_id}")
def api_delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"message": "Note deleted successfully"}
