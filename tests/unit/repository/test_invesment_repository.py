import datetime
import pytest
from sqlalchemy import insert
from app.models.models import Client, Stock, Transactions
from app.repository.investment import InvestmentRepository

@pytest.fixture
async def repository(db_session):
    return InvestmentRepository(db_session)

@pytest.mark.asyncio
async def test_get_all_active_stocks(repository, db_session):
    stocks = await repository.get_all_active_stocks()
    assert stocks == []

    test_stocks = [
        Stock(name="Test Stock 1", price=10.0, active=1),
        Stock(name="Test Stock 2", price=20.0, active=1),
        Stock(name="Inactive Stock", price=15.0, active=0)
    ]
    for stock in test_stocks:
        await db_session.execute(insert(Stock).values(name=stock.name, price=stock.price, active=stock.active))

    await db_session.commit()

    stocks = await repository.get_all_active_stocks()
    assert len(stocks) == 2
    assert stocks[0].name == "Test Stock 2"

@pytest.mark.asyncio
async def test_get_one_stock(repository, db_session):
    stock = await repository.get_stock(1)
    assert stock is None

    test_stock = Stock(name="Test Stock 1", price=10.0, active=1)
    await db_session.execute(insert(Stock).values(name=test_stock.name, price=test_stock.price, active=test_stock.active))
    await db_session.commit()

    stock = await repository.get_stock(1)
    assert stock.name == test_stock.name

@pytest.mark.asyncio
async def test_get_user_transactions(repository, db_session):
    transactions = await repository.get_user_transactions(1)
    assert transactions == []

    test_stock = Stock(id=1,name="Test Stock", price=25.0, active=1)
    test_client = Client(id=1,name="Test", surname="User", username="test",email="test@mail.ru", password="test", balance=1000.0)
    test_transaction = Transactions(
        client_id=1,
        stock_id=test_stock.id,
        volume=10,
        price=250.0,
        purchase_price=200.0,
        created_at=datetime.datetime.now()
    )
    await db_session.execute(insert(Stock).values(id=test_stock.id,name=test_stock.name, price=test_stock.price, active=test_stock.active))
    await db_session.execute(insert(Client).values(
        id=test_client.id,
        name=test_client.name,
        surname=test_client.surname,
        username=test_client.username,
        email=test_client.email,
        password=test_client.password,
        balance=test_client.balance,
    ))
    await db_session.execute(insert(Transactions).values(
        client_id=test_transaction.client_id,
        stock_id=test_transaction.stock_id,
        volume=test_transaction.volume,
        price=test_transaction.price,
        purchase_price=test_transaction.purchase_price,
        created_at=test_transaction.created_at
    ))
    await db_session.commit()

    transactions = await repository.get_user_transactions(1)
    assert len(transactions) == 1
    assert transactions[0].name == test_stock.name

@pytest.mark.asyncio
async def test_create_new_transaction_and_decrease_balance(repository, db_session):
    test_stock = Stock(id=1,name="Test Stock", price=25.0, active=1)
    test_client = Client(id=1,name="Test", surname="User", username="test",email="test@mail.ru", password="test", balance=1000.0)
    
    await db_session.execute(insert(Stock).values(id=test_stock.id,name=test_stock.name, price=test_stock.price, active=test_stock.active))
    await db_session.execute(insert(Client).values(
        id=test_client.id,
        name=test_client.name,
        surname=test_client.surname,
        username=test_client.username,
        email=test_client.email,
        password=test_client.password,
        balance=test_client.balance,
    ))
    await db_session.commit()
    result = await repository.create_new_transaction_and_decrease_balance(test_client.id, test_client.balance, test_stock.id, 10, test_stock.price*10, test_stock.price)
    assert result[0] == True
    assert result[1] == 750.0

@pytest.mark.asyncio
async def test_get_most_profitable_clients(repository, db_session):
    clients = await repository.get_most_profitable_users()
    assert clients == []
    test_client = Client(id=1,name="Test", surname="User", username="test",email="test@mail.ru", password="test", balance=1000.0)
    test_stock = Stock(id=1,name="Test Stock", price=25.0, active=1)
    test_transaction = Transactions(
        client_id=1,
        stock_id=test_stock.id,
        volume=10,
        price=250.0,
        purchase_price=200.0,
        created_at=datetime.datetime.now()
    )

    await db_session.execute(insert(Stock).values(id=test_stock.id,name=test_stock.name, price=test_stock.price, active=test_stock.active))
    await db_session.execute(insert(Client).values(
        id=test_client.id,
        name=test_client.name,
        surname=test_client.surname,
        username=test_client.username,
        email=test_client.email,
        password=test_client.password,
        balance=test_client.balance,
    ))
    await db_session.execute(insert(Transactions).values(
        client_id=test_transaction.client_id,
        stock_id=test_transaction.stock_id,
        volume=test_transaction.volume,
        price=test_transaction.price,
        purchase_price=test_transaction.purchase_price,
        created_at=test_transaction.created_at
    ))
    await db_session.commit()


    users = await repository.get_most_profitable_users()
    assert len(users) == 1
    assert users[0][0] == 'Test'
    assert users[0][1] == 'User'
    assert users[0][2] == 50.0
