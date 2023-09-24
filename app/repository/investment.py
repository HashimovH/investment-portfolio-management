from sqlalchemy.orm import Session
from app.models.models import Client, Stock, Transactions
from sqlalchemy import func, select

from app.schemas.user import UserCreate
from app.repository.base import Repository
from app.utils.auth import hash_password

class InvestmentRepository(Repository):
    async def get_all_active_stocks(self) -> list[Stock]:
        stmt = (
            select(Stock).where(Stock.active == 1)
        )
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def get_stock(self, id: int) -> Stock:
        stmt = (
            select(Stock).where(Stock.id == id)
        )
        result = await self._session.execute(stmt)
        return result.scalars().first()
    
    async def get_user_transactions(self, client_id) -> list[Transactions]:
        stmt = (
           select(Transactions, Stock.name, Stock.price).where(Transactions.client_id == client_id).join(Stock, Transactions.stock_id == Stock.id)
        )
        result = await self._session.execute(stmt)
        return result.all()

    async def create_new_transaction(self, client_id, stock_id, volume, price, purchase_price) -> Transactions:
        new_transaction = Transactions(client_id=client_id, stock_id=stock_id, volume=volume, price=price, purchase_price=purchase_price)
        self._session.add(new_transaction)
        await self._session.commit()
        return new_transaction

    async def get_most_profitable_users(self) -> list[UserCreate]:
        stmt = (
            select(Client.name, Client.surname, func.sum(Transactions.price - Transactions.purchase_price)).join(Transactions, Client.id == Transactions.client_id).group_by(Client.name, Client.surname, Client.id).order_by(func.sum(Transactions.price - Transactions.purchase_price).desc()).limit(5)
        )
        result = await self._session.execute(stmt)
        return result.all()
