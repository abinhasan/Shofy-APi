from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.slider import SliderCreate, SliderUpdate, SliderOut
from app.services import slider as service

router = APIRouter(prefix="/sliders", tags=["Sliders"])

@router.get("/", response_model=list[SliderOut])
async def get_sliders(db: Session = Depends(get_db)):
    return service.get_all_sliders(db)

@router.get("/{slider_id}", response_model=SliderOut)
async def get_slider(slider_id: int, db: Session = Depends(get_db)):
    return service.get_slider_by_id(db, slider_id)

@router.post("/", response_model=SliderOut)
async def create_slider(slider: SliderCreate, db: Session = Depends(get_db)):
    return service.create_new_slider(db, slider)

@router.put("/{slider_id}", response_model=SliderOut)
async def update_slider(slider_id: int, slider: SliderUpdate, db: Session = Depends(get_db)):
    return service.update_existing_slider(db, slider_id, slider)

@router.delete("/{slider_id}", status_code=204)
async def delete_slider(slider_id: int, db: Session = Depends(get_db)):
    service.delete_slider_by_id(db, slider_id)
    return JSONResponse (
        status_code=204,
        content={"message" : "Slider deleted successfully !"}
    )
