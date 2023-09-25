from sqlalchemy.engine import URL, make_url
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app import settings

DATABASE_URL: URL = make_url(settings.DATABASE_URL)

ASYNC_DB_URL = DATABASE_URL.set(drivername="postgresql+asyncpg")

ASYNC_ENGINE = create_async_engine(settings.DATABASE_URL, echo=True, pool_pre_ping=True)

make_async_session = async_sessionmaker(ASYNC_ENGINE, autocommit=False, autoflush=False)
