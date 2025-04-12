from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from .models import User
from .schemas import UserCreateModel, UserUpdateModel
from .utilis import hash_password


class UserService:
    async def get_all_user(self, session: AsyncSession):
        statement = select(User)

        result = await session.exec(statement)

        return result.all()

    async def get_user_by_uid(self, user_uid: str, session: AsyncSession):
        statement = select(User).where(User.uid == user_uid)
        result = await session.exec(statement)

        return result.first()

    async def get_user_by_email(self, user_email: str, session: AsyncSession):
        statement = select(User).where(User.email == user_email)
        result = await session.exec(statement)

        return result.first()

    async def user_exists(self, email, session: AsyncSession):
        user = await self.get_user_by_email(email, session)

        return True if user else None

    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):
        user_data_dict = user_data.model_dump()
        new_user = User(**user_data_dict)

        new_user.password = hash_password(user_data_dict["password"])

        session.add(new_user)
        await session.commit()

        return new_user

    async def update_user(
        self, user_uid: str, user_data: UserUpdateModel, session: AsyncSession
    ):
        user_to_update = await self.get_user_by_uid(user_uid, session)
        if user_to_update is not None:
            user_update_dict = user_data.model_dump()

            for k, v in user_update_dict.items():
                if v is not None:
                    if k == "password":
                        v = hash_password(v)
                        print(v)
                    setattr(user_to_update, k, v)

            await session.commit()
            return user_to_update

        return None

    async def delete_user(self, user_uid: str, session: AsyncSession):
        user_to_delete = await self.get_user_by_uid(user_uid, session)

        if user_to_delete is not None:
            await session.delete(user_to_delete)
            await session.commit()

            return ""
        return None
