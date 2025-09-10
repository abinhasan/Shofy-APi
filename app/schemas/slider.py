from pydantic import BaseModel

class SliderBase(BaseModel):
    title: str
    sub_title: str
    nav_title: str

class SliderCreate(SliderBase):
    pass

class SliderUpdate(SliderBase):
    pass

class SliderOut(SliderBase):
    id: int

    class Config:
        from_attributes = True
