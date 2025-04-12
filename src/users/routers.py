from fastapi import APIRouter, status, Depends
from .schemas import User, UserCreateModel, UserUpdateModel
from .service import UserService
from typing import List
from fastapi.exceptions import HTTPException
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession

user_router = APIRouter()
user_service = UserService()

@user_router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(user_data: UserCreateModel, session: AsyncSession=Depends(get_session))->dict:
    email = user_data.email
    if await user_service.user_exists(email, session):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail= "User already exists"
        )
    return await user_service.create_user(user_data, session)

@user_router.get("/", response_model=List[User])
async def get_all_user(session: AsyncSession=Depends(get_session)):
    return await user_service.get_all_user(session)

@user_router.get("/{user_uid}", response_model=User)
async def get_task(user_uid:str, session: AsyncSession=Depends(get_session))-> dict:
    user = await user_service.get_user_by_uid(user_uid, session)
    if user:
        return user
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User Not Found"
    )

@user_router.patch("/{user_uid}", response_model=User)
async def update_user(user_uid:str, user_update_data:UserUpdateModel, session: AsyncSession=Depends(get_session)):
    user = await user_service.update_user(user_uid, user_update_data, session)
    print(user)
    if user:
        return user
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User Not Found"
    )

@user_router.delete("/{user_uid}",  status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_uid:str, session: AsyncSession=Depends(get_session)):
    user = await user_service.delete_user(user_uid, session)
    if user is not '':
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Not Found"

        )