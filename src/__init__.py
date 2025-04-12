from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.db.main import db_init

from .tasks.routers import task_router
from .users.routers import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_init()
    yield
    print("Sever is stop.....")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router, prefix="/tasks", tags=["tasks"])
app.include_router(user_router, prefix="/users", tags=["users"])
