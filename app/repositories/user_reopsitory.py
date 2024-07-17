from typing import List

from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.model import User, UserRole
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

    def change_password(self, user: User, new_password: str) -> User:
        user_db: User = self.session.query(User).filter(User.id == user.id).first()
        user_db.password = new_password
        self.session.merge(user_db)
        self.session.commit()
        self.session.refresh(user_db)
        return user_db


    def update_roles(self, user: User, new_roles:List[UserRole]) -> User:
        user_db: User = self.session.query(User).filter(User.id == user.id).first()
        user_db.roles = new_roles
        self.session.merge(user_db)
        self.session.commit()
        self.session.refresh(user_db)
        return user_db



