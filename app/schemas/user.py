from pydantic import BaseModel

class UserCreate(BaseModel):
    user_name: str
    password: str

class UserOut(BaseModel):
    id: int
    user_name: str

    class Config:
        from_attributes = True
