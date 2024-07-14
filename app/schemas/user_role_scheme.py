from pydantic import BaseModel


class UserRoleDto(BaseModel):
    id: int
    role_name: str

class UserRoleCreateDto(BaseModel):
    role_name: str



    # class Config:
    #     orm_mode = True
