from pydantic import BaseModel

class SliderBase(BaseModel):
    title: str
    sub_title: str
    #image: str | None
    nav_title: str
    #nav_icon: str| None

class SliderCreate(SliderBase):
    pass

class SliderUpdate(SliderBase):
    pass

class SliderOut(SliderBase):
    id: int

    class Config:
        from_attributes = True
