from sqlmodel import SQLModel, Field, Column, Relationship
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid
from enum import Enum
from typing import Optional

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETE = "complete"

class Task(SQLModel, table=True):
    __tablename__ = "tasks"

    uid: uuid.UUID = Field(
        sa_column= Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    name: str
    description: str
    status: TaskStatus = Field(
        sa_column=Column(
            pg.ENUM(TaskStatus, name="task_status_enum"),
            default=TaskStatus.PENDING
        )
    )
    user_id: uuid.UUID = Field(foreign_key="users.uid")
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))


    def __repr__(self):
        return f"Task => {self.name}"