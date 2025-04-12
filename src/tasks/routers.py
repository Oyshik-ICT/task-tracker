from fastapi import APIRouter, status, Depends
from .schemas import Task, TaskUpdateModel, TaskCreateModel
from typing import List
from .service import TaskService
from fastapi.exceptions import HTTPException
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession

task_router = APIRouter()
task_service = TaskService()

@task_router.get("/", response_model=List[Task])
async def get_all_tasks(session: AsyncSession=Depends(get_session)):
    return await task_service.get_all_tasks(session)

@task_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Task)
async def create_task(task_data: TaskCreateModel, session: AsyncSession=Depends(get_session))->dict:
    return await task_service.create_task(task_data, session)

@task_router.get("/{task_uid}", response_model=Task)
async def get_task(task_uid:str, session: AsyncSession=Depends(get_session))-> dict:
    task = await task_service.get_task(task_uid, session)
    if task:
        return task
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task Not Found"
    )

@task_router.patch("/{task_uid}", response_model=TaskUpdateModel)
async def update_task(task_uid:str, task_update_data:TaskUpdateModel, session: AsyncSession=Depends(get_session)):
    task = await task_service.update_task(task_uid, task_update_data, session)
    if task:
        return task
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task Not Found"
    )

@task_router.delete("/{task_uid}",  status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_uid:str, session: AsyncSession=Depends(get_session)):
    task = await task_service.delete_task(task_uid, session)
    if task is not '':
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task Not Found"

        )