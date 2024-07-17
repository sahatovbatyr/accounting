from pydantic import BaseModel
from typing import Set, List

from app.models.model import UserRole
from app.schemas.user_role_scheme import UserRoleDto


# class UserDto(BaseModel):
#     id:int
#     username: str
#     password: str

class UserCreateDto(BaseModel):
    username: str
    password: str
    password_confirmation: str
    roles: List[UserRoleDto]

class UserShowDto(BaseModel):
    id:int
    username: str
    class Config:
        from_attributes = True

class UserChangePasswordDto(BaseModel):
    id:int
    username: str
    password: str
    new_password: str
    new_password_confirmation: str

    class Config:
        from_attributes = True


class UserChangeRoleDto(BaseModel):
    id:int
    username: str
    roles: List[UserRoleDto]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True





# class User(BaseModel):
#     id: int
#     roles: Set[int]
#
#     class Config:
#         orm_mode = True
