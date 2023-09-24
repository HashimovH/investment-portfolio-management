from fastapi import HTTPException
from app.exceptions.insufficient_balance import InsufficientBalance
from app.exceptions.username_taken import UsernameAlreadyTaken
from app.schemas.user import UserCreate
from app.models.models import Client, Stock, Transactions


class InvestmentService:
    def __init__(self, repository, user_repository) -> None:
        self._repository = repository
        self._user_repository = user_repository
    
    async def get_all_stocks(self) -> list[Stock]:
        return await self._repository.get_all_active_stocks()
    
    async def get_user_transactions(self, client_id) -> list[Transactions]:
        return await self._repository.get_user_transactions(client_id)


    async def create_new_transaction(self, client_id: int, client_balance: float, stock_id: int, volume: int) -> Transactions:
        stock = await self._repository.get_stock(stock_id)
        
        transaction_price = stock.price * volume
        if client_balance < transaction_price:
            raise InsufficientBalance(status_code=400)
        
        transaction = await self._repository.create_new_transaction(client_id, stock_id, volume, transaction_price, stock.price)
        
        client_balance = client_balance
        new_balance = client_balance - transaction_price
        await self._user_repository.decrease_balance(client_id, new_balance)

        return transaction