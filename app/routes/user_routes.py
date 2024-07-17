from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.model import User, UserRole
from app.schemas.user_scheme import UserShowDto, UserCreateDto, UserChangePasswordDto, UserChangeRoleDto
# from app.services.user_service import cr
from app.database.db_config import SessionLocal
from app.services.user_service import UserService


# router = APIRouter()


class UserRouter:
    def __init__(self):
        self.router = APIRouter()
        self.user_service = UserService()

        @self.router.post("/create/")
        def create_user( userCreateDto: UserCreateDto):
            user: User = self.user_service.create( userCreateDto )
            return user

        @self.router.get("/get-by-id/{id}")
        def get_by_id(id: int):
            user: User = self.user_service.get_by_id(id)
            return user

        @self.router.post("/change-password/")
        def user_change_password( userChangePasswordDto: UserChangePasswordDto):

            if userChangePasswordDto.new_password != userChangePasswordDto.new_password_confirmation:
                raise HTTPException(400, "Passwords not match")

            user: User = User()
            user.id = userChangePasswordDto.id
            user.username = userChangePasswordDto.username
            user.password = userChangePasswordDto.password
            new_password = userChangePasswordDto.new_password
            user = self.user_service.change_password(user, new_password)
            return UserShowDto.model_validate( user)

        @self.router.post("/update-roles/")
        def user_update_roles(userChangeRoleDto: UserChangeRoleDto):
            user: User = User()
            user.id = userChangeRoleDto.id
            user.username = userChangeRoleDto.username
            roles = [ UserRole( id = r.id, role_name= r.role_name)  for r in userChangeRoleDto.roles ]
            user = self.user_service.update_roles(user, roles )
            return UserShowDto.model_validate(user)



    def get_router(self):
        return self.router

#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# @router.get("/test/" )
# def test_hello():
#     return {"det":"success"}
#
# @router.post("/create", response_model=UserShowDto)
# def create_new_user(user: UserCreateDto, db: Session = Depends(get_db)):
#     return create_user(db=db, user=user)
#
# @router.get("/users/{user_id}", response_model=UserShowDto)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
