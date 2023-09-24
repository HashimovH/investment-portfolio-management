from sqlalchemy.orm import Session
from app.models.models import Stock
from sqlalchemy import select

from app.schemas.user import UserCreate
from app.repository.base import Repository
from app.utils.auth import hash_password

class InvestmentRepository(Repository):
    async def get_all_active_stocks(self) -> Stock:
        stmt = (
            select(Stock).where(Stock.active == 1)
        )
        result = await self._session.execute(stmt)
        return result.scalars().all()