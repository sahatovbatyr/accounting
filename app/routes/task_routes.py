from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task_scheme import Task, TaskCreate
from app.services.task_service import create_task, get_task
from app.database.db_config import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks/", response_model=Task)
def create_new_task(task: TaskCreate, author_id: int, assigned_to_id: int, db: Session = Depends(get_db)):
    return create_task(db=db, task=task, author_id=author_id, assigned_to_id=assigned_to_id)

@router.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
