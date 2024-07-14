from pydantic import BaseModel
from typing import Set

# class UserDto(BaseModel):
#     id:int
#     username: str
#     password: str

class UserCreateDto(BaseModel):
    username: str
    password: str
    password_confirmation: str
    roles: Set[int]

class UserShowDto(BaseModel):
    id:int
    username: str
    password: str


# class User(BaseModel):
#     id: int
#     roles: Set[int]
#
#     class Config:
#         orm_mode = True
