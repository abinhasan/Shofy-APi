from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.image import ImageCreate, ImageUpdate, ImageOut
from app.services import image as service
from fastapi.responses import StreamingResponse
import io

router = APIRouter(prefix="/image", tags=["Images"])


@router.post("/images/", response_model=ImageOut)
async def create_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    image = ImageCreate(filename=file.filename, content_type=file.content_type, data=contents)
    return service.create_new_image(db=db, image=image)


# READ metadata
@router.get("/images/{image_id}", response_model=ImageOut)
def read_image(image_id: int, db: Session = Depends(get_db)):
    return service.get_image_by_id(db, image_id=image_id)


# READ actual file
@router.get("/images/{image_id}/file")
def read_image_file(image_id: int, db: Session = Depends(get_db)):
    db_image = service.get_image_by_id(db, image_id=image_id)
    return StreamingResponse(io.BytesIO(db_image.data), media_type=db_image.content_type)


# LIST
@router.get("/images/", response_model=list[ImageOut])
def list_images(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return service.get_all_images(db, skip=skip, limit=limit)


# UPDATE
@router.put("/images/{image_id}", response_model=ImageOut)
async def update_image(image_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    update_data = ImageUpdate(
        filename=file.filename,
        content_type=file.content_type,
        data=contents
    )
    return service.update_existing_image(db=db, image_id=image_id, image=update_data)


# DELETE
@router.delete("/images/{image_id}", response_model=ImageOut)
def delete_image(image_id: int, db: Session = Depends(get_db)):
    return service.delete_image_by_id(db, image_id=image_id)
