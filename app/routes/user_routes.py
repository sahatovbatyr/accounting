from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.model import User
from app.schemas.user_scheme import UserShowDto, UserCreateDto
# from app.services.user_service import cr
from app.database.db_config import SessionLocal
from app.services.user_service import UserService


# router = APIRouter()


class UserRouter:
    def __init__(self):
        self.router = APIRouter();
        self.user_service = UserService()

        @self.router.post("/create/")
        def create_user( userCreateDto: UserCreateDto):
            user: User = self.user_service.create( userCreateDto )
            return user

        @self.router.get("/get-by-id/{id}")
        def get_by_id(id: int):
            user: User = self.user_service.get_by_id(id)
            return user



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
