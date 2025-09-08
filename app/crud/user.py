from sqlalchemy.orm import Session
from app.models.user import User


async def get_user_by_username(db: Session, user_name: str):
    return db.query(User).filter(User.user_name == user_name).first()

def create_user(db: Session, user_name: str, hashed_password: str):
    db_user = User(user_name = user_name, hashed_password = hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
