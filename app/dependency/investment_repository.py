from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependency.database_session import get_database_session
from app.repository.investment import InvestmentRepository


@Depends
def get_investment_repository(
    db_session: AsyncSession = get_database_session,
) -> InvestmentRepository:
    return InvestmentRepository(db_session)
