from app.repository.user import UserRepository
from fastapi import Depends
from app.dependency.database_session import get_database_session
from sqlalchemy.ext.asyncio import AsyncSession

@Depends
def get_user_repository(db_session: AsyncSession = get_database_session) -> UserRepository:
    return UserRepository(db_session)