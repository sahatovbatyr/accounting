from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db_config import get_db
from app.models.model import User, UserRole
from app.repositories.user_reopsitory import UserRepository
from app.schemas.user_scheme import UserCreateDto, UserShowDto
from app.services.user_role_service import UserRoleService


class UserService:

    def __init__(self ):
        self.session = next(get_db())
        self.user_repository = UserRepository(self.session)
        self.user_role_service = UserRoleService( self.session )

    def get_by_id(self, user_id: int):
        # user: User = self.session.query(User).filter(User.id == user_id).first()
        user: User = self.user_repository.get_by_id(user_id)
        return UserShowDto.model_validate(user)

    def create(self, userCreateDto: UserCreateDto) -> User:

        if userCreateDto.password != userCreateDto.password_confirmation:
            raise HTTPException(400, "Password and confirmation not match!")

        if len(userCreateDto.roles) == 0:
            raise HTTPException(400, "User must have at least one role.")

        user_is_exists = self.user_repository.is_username_exist(userCreateDto.username)

        if user_is_exists:
            raise HTTPException(400, f"User with username: {userCreateDto.username} already exists.")

        roles = self.user_role_service.get_by_id_list(userCreateDto.roles)

        user: User = User()
        user.roles = roles
        user.password = userCreateDto.password
        user.username = userCreateDto.username
        user = self.user_repository.create( user )
        return user


    def change_password(self, user: User, new_password: str):
        user_db = self.user_repository.get_by_id(user.id)

        if user_db.password != user.password:
            raise HTTPException(400, "Username or password is wrong.")

        user_db = self.user_repository.change_password( user, new_password)
        return user_db

    def update_roles(self, user: User, new_roles:List[UserRole]):
        new_roles = self.user_role_service.get_by_id_list(new_roles)

        if len(new_roles) == 0:
            raise HTTPException(400, "Users must have at  least one role.")
        user_db = self.user_repository.update_roles( user, new_roles)
        return user_db




