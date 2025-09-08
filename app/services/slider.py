from sqlalchemy.orm import Session
from app.crud import slider as crud
from fastapi import HTTPException
from app.schemas.slider import SliderCreate, SliderUpdate


def get_all_sliders(db: Session):
    return crud.get_sliders(db)

def get_slider_by_id(db: Session, slider_id: int):
    slider = crud.get_slider(db, slider_id)
    if not slider:
        raise HTTPException(status_code=404, detail="slider not found")
    return slider

def create_new_slider(db: Session, slider_data: SliderCreate):
    return crud.create_slider(db, slider_data)

def update_existing_slider(db: Session, slider_id: int, updates: SliderUpdate):
    slider = crud.get_slider(db, slider_id)
    if not slider:
        raise HTTPException(status_code=404, detail="slider not found")
    return crud.update_slider(db, slider, updates)

def delete_slider_by_id(db: Session, slider_id: int):
    slider = crud.get_slider(db, slider_id)
    if not slider:
        raise HTTPException(status_code=404, detail="slider not found")
    crud.delete_slider(db, slider)