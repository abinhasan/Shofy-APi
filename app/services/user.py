from sqlalchemy.orm import Session
from app.crud import user as crud
from app.schemas.user import UserCreate, UserOut
from app.core.security import hash_password, verify_password, create_access_token

def register_user(db: Session, user_data: UserCreate):
    if crud.get_user_by_username(db, user_data.user_name):
        raise ValueError("Username already exists")

    hashed_password = hash_password(user_data.password)

    return crud.create_user(db, user_data.user_name, hashed_password)


async def authenticate_user(db: Session, user_name: str, password: str):
    user = await crud.get_user_by_username(db, user_name)
    if not user or not verify_password(password, user.hashed_password):
        return None
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}