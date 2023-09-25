from sqlalchemy import Engine, create_engine
from sqlalchemy.engine import URL, make_url
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker

from app import settings

DATABASE_URL: URL = make_url(settings.DATABASE_URL)

options = {}
if "sqlite" not in DATABASE_URL.drivername:
    options = {
        "pool_size": 10,
        "pool_pre_ping": True,
    }

ENGINE: Engine = create_engine(DATABASE_URL, **options)

ASYNC_DB_URL: URL

if "sqlite" in DATABASE_URL.drivername:
    ASYNC_DB_URL = DATABASE_URL.set(drivername="sqlite+aiosqlite")
else:
    ASYNC_DB_URL = DATABASE_URL.set(drivername="postgresql+asyncpg")
# IMPORTANT: pool_size must match or exceed the number of concurrent celery workers
# otherwise you will be seeing QueuePool errors about insufficient connections in the
# pool.
ASYNC_ENGINE: AsyncEngine = create_async_engine(ASYNC_DB_URL, **options)

make_session = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
make_async_session = async_sessionmaker(ASYNC_ENGINE, autocommit=False, autoflush=False)