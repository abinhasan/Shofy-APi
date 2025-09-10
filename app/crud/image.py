from sqlalchemy.orm import Session
from app.models.image import Image
from app.schemas.image import ImageCreate, ImageUpdate


def create_image(db: Session, image: ImageCreate):
    db_image = Image(
        filename=image.filename,
        content_type=image.content_type,
        data=image.data
    )
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

def get_image(db: Session, image_id: int):
    return db.query(Image).filter(Image.id == image_id).first()

def get_images(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Image).offset(skip).limit(limit).all()

def update_image(db: Session, image_id: int, image: ImageUpdate):
    db_image = db.query(Image).filter(Image.id == image_id).first()
    if not db_image:
        return None
    if image.filename is not None:
        db_image.filename = image.filename
    if image.content_type is not None:
        db_image.content_type = image.content_type
    if image.data is not None:
        db_image.data = image.data
    db.commit()
    db.refresh(db_image)
    return db_image

def delete_image(db: Session, image_id: int):
    db_image = db.query(Image).filter(Image.id == image_id).first()
    if db_image:
        db.delete(db_image)
        db.commit()
    return db_image