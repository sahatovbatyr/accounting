from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.db_config import  get_db
from app.models.model import UserRole
from app.repositories.user_role_repository import UserRoleRepository
from app.schemas.user_role_scheme import UserRoleCreateDto


class UserRoleService:

    def __init__(self, session:Session = None):
        self.session =  session if session is not None else next(get_db())
        self.user_role_repository = UserRoleRepository(self.session)


    def get_by_id(self, role_id: int) -> UserRole:
        return self.user_role_repository.get_by_id( role_id)

    def get_by_id_list(self, roles: List[UserRole]):
        role_id_list = [ role.id for role in roles]
        return self.user_role_repository.get_all_by_list_id( role_id_list)

    def create_user_role(self, role_dto: UserRoleCreateDto):
        role = self.user_role_repository.create(role_dto)
        return role


