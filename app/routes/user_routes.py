from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_scheme import UserShowDto, UserCreateDto
from app.services.user_service import create_user, get_user
from app.database.db_config import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/test/" )
def test_hello():
    return {"det":"success"}

@router.post("/create", response_model=UserShowDto)
def create_new_user(user: UserCreateDto, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=UserShowDto)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
