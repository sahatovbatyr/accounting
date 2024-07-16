from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.model import User
from app.repositories.user_role_repository import UserRoleRepository
from app.schemas.user_scheme import UserCreateDto


class UserRepository:
    def __init__(self, session: Session):
        self.session = session
        # self.user_role_repository = UserRoleRepository(session)

    def create(self, user:User) -> User:
        try:
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
        except Exception as exc:
            raise HTTPException(500, exc)

        return user


    def get_by_id(self, user_id: int) -> User:
        user: User = self.session.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(400, f"User not found by id:{user_id}")
        return user

    def is_username_exist(self, username: str) -> bool:
        user: User = self.session.query(User).filter(User.username == username).first()
        return True if user else False

