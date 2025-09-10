from pydantic import BaseModel

# Common properties
class ImageBase(BaseModel):
    filename: str
    content_type: str
    entity_id: int
    entity_name: str
    is_compressed: bool = False

# For creating an image (client uploads)
class ImageCreate(ImageBase):
    data: bytes  # store as bytes when creating

class ImageUpdate(BaseModel):
    filename: str | None
    content_type: str | None
    data: bytes | None = None
    entity_id: int| None
    entity_name: str| None
    is_compressed: bool| None

# For response (without raw data, to avoid huge payloads)
class ImageOut(ImageBase):
    id: int

    class Config:
        from_attributes = True