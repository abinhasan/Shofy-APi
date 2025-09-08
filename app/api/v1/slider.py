from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from app.core.database import get_db
from app.schemas.slider import SliderCreate, SliderUpdate, SliderOut
from app.services import slider as service
from app.models.user import User
from app.core.security import decode_access_token

router = APIRouter(prefix="/sliders", tags=["Sliders"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).get(int(payload["sub"]))
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@router.get("/", response_model=list[SliderOut])
async def get_sliders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return service.get_all_sliders(db)

@router.get("/{slider_id}", response_model=SliderOut)
async def get_slider(slider_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return service.get_slider_by_id(db, slider_id)

@router.post("/", response_model=SliderOut)
async def create_slider(slider: SliderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return service.create_new_slider(db, slider)

@router.put("/{slider_id}", response_model=SliderOut)
async def update_slider(slider_id: int, slider: SliderUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return service.update_existing_slider(db, slider_id, slider)

@router.delete("/{slider_id}", status_code=204)
async def delete_slider(slider_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    service.delete_slider_by_id(db, slider_id)
    return JSONResponse (
        status_code=204,
        content={"message" : "Slider deleted successfully !"}
    )
