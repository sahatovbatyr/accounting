from pydantic import BaseModel

class TaskBase(BaseModel):
    description: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    author_id: int
    assigned_to_id: int

    class Config:
        orm_mode = True
