import datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.exceptions.insufficient_balance import InsufficientBalance
from app.models.models import Client, Stock, Transactions
from app.schemas.transaction import TransactionOut, TransactionOutWithTotal
from app.schemas.user import ProfitableUsers
from app.services.investment_service import InvestmentService


@pytest.fixture
async def repository():
    return AsyncMock()


@pytest.fixture
async def user_repository():
    return AsyncMock()


@pytest.fixture
async def service(repository, user_repository):
    return InvestmentService(repository, user_repository)


@pytest.mark.asyncio
async def test_get_all_active_stocks(service, repository):
    repository.get_all_active_stocks.return_value = []
    result = await service.get_all_stocks()
    assert result == []
    service._repository.get_all_active_stocks.assert_called_once()

    service._repository.get_all_active_stocks.return_value = [
        Stock(id=1, name="test", price=1.0, active=True)
    ]
    result = await service.get_all_stocks()
    assert result[0].id == 1
    assert len(result) == 1


@pytest.mark.asyncio
async def test_get_user_transaction(service, repository, user_repository):
    repository.get_user_transactions.return_value = []
    result = await service.get_user_transactions(1)
    assert result.transactions == []
    assert result.total_gain == 0
    assert result.total_value == 0

    # Test with data
    transaction_1 = Transactions(
        id=1,
        client_id=1,
        stock_id=1,
        volume=3,
        price=30.0,
        purchase_price=10.0,
        created_at=datetime.datetime.now(),
    )
    transaction_2 = Transactions(
        id=2,
        client_id=1,
        stock_id=1,
        volume=2,
        price=30.0,
        purchase_price=15.0,
        created_at=datetime.datetime.now(),
    )
    repository.get_user_transactions.return_value = [
        (
            [
                transaction_1,
                "Test Stock 1",
                20,
            ]
        ),
        ([transaction_2, "Test Stock 2", 10]),
    ]
    result = await service.get_user_transactions(1)
    assert result.total_gain == 20
    assert result.total_value == 80
    assert len(result.transactions) == 2


@pytest.mark.asyncio
async def test_create_new_transaction(service, repository):
    # Test with insufficient balance
    repository.get_stock.return_value = Stock(
        id=1, name="test", price=20.5, active=True
    )
    with pytest.raises(InsufficientBalance):
        await service.create_new_transaction(1, 10, 1, 11)

    # Test with sufficient balance
    repository.get_stock.return_value = Stock(id=1, name="test", price=20, active=True)
    repository.create_new_transaction_and_decrease_balance.return_value = (True, 10)
    result = await service.create_new_transaction(1, 30, 1, 1)
    assert result == (True, 10)


@pytest.mark.asyncio
async def test_get_most_profitable_user(service, repository, user_repository):
    repository.get_most_profitable_users.return_value = []
    result = await service.get_most_profitable_users()
    assert result == []
    service._repository.get_most_profitable_users.assert_called_once()

    # Test with data
    repository.get_most_profitable_users.return_value = [("Test", "User", 10)]
    result = await service.get_most_profitable_users()
    assert result[0].name == "Test"
    assert result[0].surname == "User"
    assert result[0].profit == 10
    assert len(result) == 1
