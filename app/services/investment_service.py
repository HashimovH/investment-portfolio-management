from fastapi import HTTPException
from app.exceptions.insufficient_balance import InsufficientBalance
from app.exceptions.username_taken import UsernameAlreadyTaken
from app.models.models import Client, Stock, Transactions
from app.schemas.transaction import TransactionIn, TransactionOut, TransactionOutWithTotal


class InvestmentService:
    def __init__(self, repository, user_repository) -> None:
        self._repository = repository
        self._user_repository = user_repository
    
    async def get_all_stocks(self) -> list[Stock]:
        return await self._repository.get_all_active_stocks()
    
    async def get_user_transactions(self, client_id) -> TransactionOutWithTotal:
        transactions = await self._repository.get_user_transactions(client_id)
        total_gain = 0
        total_value = 0
        result = []
        for transaction in transactions:
            gain = round(transaction[2] - transaction[0].purchase_price, 3)
            total_value += round(transaction[2] * transaction[0].volume, 3)
            total_gain += gain
            result.append(
                TransactionOut(
                    id=transaction[0].id, 
                    stock=transaction[1], 
                    current_price=transaction[2],
                    volume=transaction[0].volume, 
                    price=round(transaction[0].price, 3),
                    purchase_price=transaction[0].purchase_price, 
                    purchase_date=transaction[0].created_at.strftime('%Y-%m-%d %H:%M'),
                    gain=gain,
                )
            )

        return TransactionOutWithTotal(total_gain=round(total_gain, 3), transactions=result, total_value=total_value)


    async def create_new_transaction(self, client_id: int, client_balance: float, stock_id: int, volume: int) -> Transactions:
        stock = await self._repository.get_stock(stock_id)
        
        transaction_price = stock.price * volume
        if client_balance < transaction_price:
            raise InsufficientBalance("Insufficient balance")
        
        transaction = await self._repository.create_new_transaction(client_id, stock_id, volume, transaction_price, stock.price)
        
        client_balance = client_balance
        new_balance = client_balance - transaction_price
        await self._user_repository.decrease_balance(client_id, new_balance)

        return transaction