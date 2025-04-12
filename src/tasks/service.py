from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import TaskCreateModel, TaskUpdateModel
from sqlmodel import select
from .models import Task

class TaskService:
    async def get_all_tasks(self, session:AsyncSession):
        statement = select(Task).order_by(Task.created_at)

        result = await session.exec(statement)

        return result.all()

    async def get_task(self, task_uid:str, session:AsyncSession):
        statement = select(Task).where(Task.uid==task_uid)

        result = await session.exec(statement)

        return result.first()

    async def create_task(self, task_data: TaskCreateModel, session:AsyncSession):
        task_data_dict = task_data.model_dump()
        new_task = Task(
            **task_data_dict
        )

        session.add(new_task)
        await session.commit()

        return new_task

    async def update_task(self, task_uid:str, task_data: TaskUpdateModel, session:AsyncSession):
        task_to_update = await self.get_task(task_uid, session)
        if task_to_update is not None:
            task_update_dict = task_data.model_dump()

            for k, v in task_update_dict.items():
                if v is not None:
                    setattr(task_to_update, k, v)

            await session.commit()
            return task_to_update
        
        return None

    async def delete_task(self, task_uid:str, session:AsyncSession):
        task_to_delete = await self.get_task(task_uid, session)

        if task_to_delete is not None:
            await session.delete(task_to_delete)
            await session.commit()

            return ''
        return None
