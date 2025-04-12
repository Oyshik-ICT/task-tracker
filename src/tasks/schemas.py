import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from .models import TaskStatus


class Task(BaseModel):
    uid: uuid.UUID
    name: str
    description: str
    user_id: uuid.UUID
    status: TaskStatus
    created_at: datetime


class TaskCreateModel(BaseModel):
    name: str
    description: str
    user_id: uuid.UUID


class TaskUpdateModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
