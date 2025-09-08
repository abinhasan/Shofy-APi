from sqlalchemy.orm import Session
from app.models.slider import Slider
from app.schemas.slider import SliderCreate, SliderUpdate


def get_sliders(db: Session):
    return db.query(Slider).all()

def get_slider(db: Session, slider_id: int):
    return db.query(Slider).filter(Slider.id == slider_id).first()

def create_slider(db: Session, slider: SliderCreate):
    db_slider = Slider(**slider.model_dump())
    db.add(db_slider)
    db.commit()
    db.refresh(db_slider)
    return db_slider

def update_slider(db: Session, db_slider: Slider, updates: SliderUpdate):
    for field, value in updates.dict().items():
        setattr(db_slider, field, value)
    db.commit()
    db.refresh(db_slider)
    return db_slider

def delete_slider(db: Session, db_slider: Slider):
    db.delete(db_slider)
    db.commit()