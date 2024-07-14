from fastapi import FastAPI
from app.routes import user_routes, user_role_routes, task_routes
# from app.database import engine, Base

# Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(user_role_routes.router, prefix="/roles", tags=["roles"])
app.include_router(task_routes.router, prefix="/tasks", tags=["tasks"])
