from sqlalchemy.orm import Session
from app.models.model import User
from app.schemas.user_scheme import UserCreateDto

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreateDto):
    db_user = User(username=user.username, password=user.password)

    db_user = User()

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
