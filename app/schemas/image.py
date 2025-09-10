from pydantic import BaseModel

# Common properties
class ImageBase(BaseModel):
    filename: str
    content_type: str

# For creating an image (client uploads)
class ImageCreate(ImageBase):
    data: bytes  # store as bytes when creating

class ImageUpdate(BaseModel):
    filename: str | None = None
    content_type: str | None = None
    data: bytes | None = None

# For response (without raw data, to avoid huge payloads)
class ImageOut(ImageBase):
    id: int

    class Config:
        from_attributes = True