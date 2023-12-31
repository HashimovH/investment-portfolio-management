import logging

from app.exceptions.insufficient_balance import InsufficientBalance
from app.models.models import Stock
from app.schemas.transaction import TransactionOut, TransactionOutWithTotal
from app.schemas.user import ProfitableUsers
from decimal import Decimal

logger = logging.getLogger(__name__)


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
            gain = round(
                transaction[0].volume
                * (transaction[2] - transaction[0].purchase_price),
                3,
            )
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
                    purchase_date=transaction[0].created_at.strftime("%Y-%m-%d %H:%M"),
                    gain=gain,
                )
            )

        return TransactionOutWithTotal(
            total_gain=round(total_gain, 3),
            transactions=result,
            total_value=total_value,
        )

    async def create_new_transaction(
        self, client_id: int, client_balance: Decimal, stock_id: int, volume: int
    ) -> tuple[bool, Decimal]:
        stock = await self._repository.get_stock(stock_id)

        transaction_price = stock.price * volume
        if client_balance < transaction_price:
            logger.warning(f"Insufficient balance for client {client_id}")
            raise InsufficientBalance("Insufficient balance")
        _, balance = await self._repository.create_new_transaction_and_decrease_balance(
            client_id, client_balance, stock_id, volume, transaction_price, stock.price
        )

        return True, balance

    async def get_most_profitable_users(self) -> list[ProfitableUsers]:
        profits = await self._repository.get_most_profitable_users()
        print(profits)
        result = []
        for profit in profits:
            if(profit[2] <= 0):
                continue
            result.append(
                ProfitableUsers(name=profit[0], surname=profit[1], profit=profit[2])
            )
        return result
