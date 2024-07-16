from typing import Set, List, Type
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.model import UserRole
from app.schemas.user_role_scheme import UserRoleDto, UserRoleCreateDto


class UserRoleRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, roleCreateDto: UserRoleCreateDto ) -> UserRole:
        new_role = UserRole(role_name= roleCreateDto.role_name)
        self.db.add(new_role)
        self.db.commit()
        self.db.refresh(new_role)
        return new_role


    def get_by_id(self, id: int ) -> UserRole:
        role = self.db.query(UserRole).filter(UserRole.id == id).first()
        if role is None:
            raise HTTPException(status_code=400, detail=f"Role not found by id: {id}")
        return role


    def update(self, user_role: UserRoleDto ) -> UserRole:
        new_role = user_role
        self.db.add(new_role)
        self.db.commit()
        self.db.refresh(new_role)
        return new_role

    def get_all_by_list_id(self, id_list: List[int] ) -> List[UserRole]:
        roles: List[UserRole] = self.db.query(UserRole).filter(UserRole.id.in_(id_list)).all()
        # converted_users: List[UserRole] = [UserRole(role.id, role.role_name) for role in roles_from_db]
        return roles


