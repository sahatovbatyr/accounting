from sqlalchemy.orm import Session

from app.models.model import UserRole
from app.schemas.user_role_scheme import UserRoleDto, UserRoleCreateDto


class UserRoleRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, roleCreateDto: UserRoleCreateDto ) -> UserRole:
        new_role = UserRole(None, roleCreateDto.role_name)
        self.db.add(new_role)
        self.db.commit()
        self.db.refresh(new_role)
        return new_role


    def get_by_id(self, id: int ) -> UserRole:
        return self.db.query(UserRole).filter(UserRole.id == id).first()


    def update(self, user_role: UserRoleDto ) -> UserRole:
        new_role = user_role
        self.db.add(new_role)
        self.db.commit()
        self.db.refresh(new_role)
        return new_role

