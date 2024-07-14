from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.db_config import  get_db
from app.models.model import UserRole
from app.repositories.user_role_repository import UserRoleRepository
from app.schemas.user_role_scheme import UserRoleCreateDto


class UserRoleService:

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        self.user_role_repository = UserRoleRepository(db)


    def get_by_id(self, role_id: int):
        self.user_role_repository.get_by_id( role_id)

    def create_user_role(self, role_dto: UserRoleCreateDto):
        role = UserRole(role_name=role_dto.role_name)
        self.user_role_repository.create(role)
        return role



