import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import (ResponseValidationError,
                                RequestValidationError
                                )
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from starlette.responses import PlainTextResponse
from app.routes import user_routes, user_role_routes, task_routes
from app.routes.user_role_routes import UserRoleRouter
from app.routes.user_routes import UserRouter

app = FastAPI()

my_user_role_routes = UserRoleRouter().get_router()
my_user_routes = UserRouter().get_router()

# app.include_router(user_routes.router, prefix="/users", tags=["users"])
# app.include_router(user_role_routes.router, prefix="/roles", tags=["roles"])

app.include_router(my_user_role_routes, prefix="/roles", tags=["roles"])
app.include_router(my_user_routes, prefix="/users", tags=["users"])

app.include_router(task_routes.router, prefix="/tasks", tags=["tasks"])

@app.exception_handler(IntegrityError)
async def sql_alchemy_exception_handler( request, exc:IntegrityError):
    return PlainTextResponse(f"IntegrityError: The value already exist in table: {exc}", status_code=400)

@app.exception_handler(SQLAlchemyError)
async def sql_alchemy_exception_handler( request, exc):
    return PlainTextResponse(str(exc.__class__.__name__), status_code=400)

@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

@app.exception_handler(ResponseValidationError)
async def response_validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

@app.exception_handler(ValidationError)
async def pydantic_validation_exception_handler(request, exc):
    message = f"ValidationError. {exc}"
    return PlainTextResponse(message, status_code=400)

@app.exception_handler(HTTPException)
async def response_validation_exception_handler(request, exc:HTTPException):
    return PlainTextResponse(str(exc), status_code=exc.status_code)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True,   port=8000)
