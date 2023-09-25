from typing import AsyncIterator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import make_async_session


@Depends
async def get_database_session() -> AsyncIterator[AsyncSession]:
    async with make_async_session() as session:
        yield session
