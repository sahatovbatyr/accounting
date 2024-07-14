from sqlalchemy.orm import Session
from app.models.model import Task
from app.schemas.task_scheme import TaskCreate

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def create_task(db: Session, task: TaskCreate, author_id: int, assigned_to_id: int):
    db_task = Task(description=task.description, author_id=author_id, assigned_to_id=assigned_to_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
