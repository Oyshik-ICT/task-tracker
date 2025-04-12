from pydantic import BaseModel, Field
from typing import Optional
import uuid
from datetime import datetime

class User(BaseModel):
    uid: uuid.UUID
    email: str
    password: str = Field(exclude=True)
    created_at: datetime

class UserCreateModel(BaseModel):
    email: str
    password: str = Field(min_length=6)

class UserUpdateModel(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = Field(default=None, min_length=6)

