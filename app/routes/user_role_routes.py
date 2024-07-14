from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_role_scheme import UserRoleDto, UserRoleCreateDto
from app.services.user_role_service import UserRoleService
from app.database.db_config import get_db

router = APIRouter()


@router.get("/test/")
def test_user_role():
    return {"data":"success"}

@router.post("/create/", response_model=UserRoleDto)
def create_new_user_role(user_role: UserRoleCreateDto, db: Session = Depends(get_db) ):
    user_role_service = UserRoleService(db)
    return user_role_service.create_user_role(user_role)

    # return create_user_role(db=db, role_name=role_name)

@router.get("/roles/{role_id}", response_model=UserRoleDto)
def read_user_role(role_id: int , db: Session = Depends(get_db) ):
    user_role_service = UserRoleService(db)
    role = user_role_service.get_by_id(role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return role
