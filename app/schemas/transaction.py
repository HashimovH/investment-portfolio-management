from typing import Optional

from pydantic import BaseModel


class TransactionIn(BaseModel):
    stock: int
    volume: int


class TransactionOut(BaseModel):
    id: int
    stock: str
    volume: int
    price: Optional[float]
    purchase_price: Optional[float] = 0
    purchase_date: str
    current_price: Optional[float] = None
    gain: Optional[float] = 0


class TransactionOutWithTotal(BaseModel):
    total_gain: Optional[float] = 0
    total_value: Optional[float] = 0
    transactions: list[TransactionOut]


class CreateTransactionResponse(BaseModel):
    success: bool
    balance: float
