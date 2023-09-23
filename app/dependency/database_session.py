from fastapi import Depends
from app.database.session import make_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncIterator

@Depends
async def get_database_session()->AsyncIterator[AsyncSession]:
    async with make_async_session() as session:
        yield session