from sqlalchemy import select, update

from app.models.models import Client
from app.repository.base import Repository


class UserRepository(Repository):
    async def get_user_by_username(self, username: str) -> Client:
        stmt = select(Client).where(Client.username == username)
        result = await self._session.execute(stmt)
        return result.scalars().first()
