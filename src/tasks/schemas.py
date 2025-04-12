from pydantic import BaseModel
from typing import Optional
import uuid
from .models import TaskStatus
from datetime import datetime


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