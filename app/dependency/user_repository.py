from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependency.database_session import get_database_session
from app.repository.user import UserRepository


@Depends
def get_user_repository(
    db_session: AsyncSession = get_database_session,
) -> UserRepository:
    return UserRepository(db_session)
