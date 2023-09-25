import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Numeric

from app.models.base import Base


class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    name = Column(String)
    surname = Column(String)
    email = Column(String, unique=True, index=True)
    active = Column(Integer, default=1)
    balance = Column(Numeric(9, 3), default=0.0)


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    price = Column(Numeric(9, 3))
    active = Column(Integer, default=1)


class Transactions(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    stock_id = Column(Integer, ForeignKey("stocks.id"))
    volume = Column(Integer)
    price = Column(Numeric(9, 3))
    purchase_price = Column(Numeric(9, 3), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
