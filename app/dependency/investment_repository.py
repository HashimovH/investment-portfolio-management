from app.repository.investment import InvestmentRepository
from fastapi import Depends
from app.dependency.database_session import get_database_session
from sqlalchemy.ext.asyncio import AsyncSession

@Depends
def get_investment_repository(db_session: AsyncSession = get_database_session) -> InvestmentRepository:
    return InvestmentRepository(db_session)