from app.models.base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
import datetime


class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    name = Column(String)
    surname = Column(String)
    email = Column(String, unique=True, index=True)
    active = Column(Integer, default=1)
    balance = Column(Float, default=0.0)


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    price = Column(Float)
    total_volume = Column(Integer, default=100)
    active = Column(Integer, default=1)


class Transactions(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    stock_id = Column(Integer, ForeignKey("stocks.id"))
    volume = Column(Integer)
    price = Column(Float)
    purchase_price = Column(Float, nullable=True, default=0.0)
    created_at = Column(DateTime, default=datetime.datetime.now())
