import logging

from sqlalchemy import func, select, update

from app.models.models import Client, Stock, Transactions
from app.repository.base import Repository
from app.schemas.user import UserCreate
from decimal import Decimal


logger = logging.getLogger(__name__)


class InvestmentRepository(Repository):
    async def get_all_active_stocks(self) -> list[Stock]:
        stmt = select(Stock).where(Stock.active == 1).order_by(Stock.id.desc()).limit(5)
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def get_stock(self, id: int) -> Stock:
        stmt = select(Stock).where(Stock.id == id)
        result = await self._session.execute(stmt)
        return result.scalars().first()

    async def get_user_transactions(self, client_id) -> list[Transactions]:
        stmt = (
            select(Transactions, Stock.name, Stock.price)
            .where(Transactions.client_id == client_id)
            .join(Stock, Transactions.stock_id == Stock.id)
        )
        result = await self._session.execute(stmt)
        return result.all()

    async def create_new_transaction_and_decrease_balance(
        self,
        client_id,
        client_balance,
        stock_id,
        volume,
        transaction_price,
        purchase_price,
    ) -> tuple[bool, Decimal]:
        try:
            new_transaction = Transactions(
                client_id=client_id,
                stock_id=stock_id,
                volume=volume,
                price=transaction_price,
                purchase_price=purchase_price,
            )
            self._session.add(new_transaction)
            new_balance = client_balance - transaction_price
            stmt = (
                update(Client).where(Client.id == client_id).values(balance=new_balance)
            )
            await self._session.execute(stmt)
        except Exception as e:
            logger.error(f"Error while creating new transaction, {e}")
            await self._session.rollback()
            raise e

        await self._session.commit()
        return True, new_balance

    async def get_most_profitable_users(self) -> list[UserCreate]:
        stmt = (
            select(
                Client.name,
                Client.surname,
                func.sum(Transactions.price - Transactions.purchase_price),
            )
            .join(Transactions, Client.id == Transactions.client_id)
            .group_by(Client.name, Client.surname, Client.id)
            .order_by(func.sum(Transactions.price - Transactions.purchase_price).desc())
            .limit(5)
        )
        result = await self._session.execute(stmt)
        return result.all()
