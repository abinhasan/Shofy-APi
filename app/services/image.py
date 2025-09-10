from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.crud import image as crud
from app.schemas.image import ImageCreate, ImageUpdate
from app.models.image import Image

def create_new_image(db: Session, image: ImageCreate) -> Image:
    return crud.create_image(db, image)

def get_image_by_id(db: Session, image_id: int) -> Image:
    db_image = crud.get_image(db, image_id=image_id)
    if not db_image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image not found")
    return db_image

def get_all_images(db: Session, skip: int = 0, limit: int = 10):
    return crud.get_images(db, skip=skip, limit=limit)

def update_existing_image(db: Session, image_id: int, image: ImageUpdate) -> Image:
    db_image = crud.update_image(db, image_id=image_id, image=image)
    if not db_image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image not found")
    return db_image

def delete_image_by_id(db: Session, image_id: int) -> Image:
    db_image = crud.delete_image(db, image_id=image_id)
    if not db_image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image not found")
    return db_image
