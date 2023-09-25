from sqlalchemy import select, update

from app.models.models import Client
from app.repository.base import Repository
from app.schemas.user import UserCreate
from app.utils.auth import hash_password


class UserRepository(Repository):
    async def create(self, user: UserCreate) -> Client:
        db_user = Client(**user.model_dump())
        db_user.password = hash_password(db_user.password)
        self._session.add(db_user)
        await self._session.commit()
        await self._session.refresh(db_user)
        return db_user

    async def get_user_by_username(self, username: str) -> Client:
        stmt = select(Client).where(Client.username == username)
        result = await self._session.execute(stmt)
        return result.scalars().first()

    async def decrease_balance(self, client_id, new_balance):
        stmt = update(Client).where(Client.id == client_id).values(balance=new_balance)
        await self._session.execute(stmt)
        await self._session.commit()
