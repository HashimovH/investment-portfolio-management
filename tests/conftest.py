import asyncio
from typing import AsyncIterator
import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from app.database.session import make_async_session, ASYNC_ENGINE
from app.models.base import Base

@pytest.fixture
async def create_db():
    async with ASYNC_ENGINE.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def db_session(clean_db) -> AsyncIterator[AsyncSession]:
    async with make_async_session() as session:
        yield session


@pytest.fixture(scope="function")
async def clean_db():
    async with ASYNC_ENGINE.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    async with ASYNC_ENGINE.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    