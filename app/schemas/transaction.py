from typing import Optional

from pydantic import BaseModel
from decimal import Decimal



class TransactionIn(BaseModel):
    stock: int
    volume: int


class TransactionOut(BaseModel):
    id: int
    stock: str
    volume: int
    price: Optional[Decimal]
    purchase_price: Optional[Decimal] = 0
    purchase_date: str
    current_price: Optional[Decimal] = None
    gain: Optional[Decimal] = 0


class TransactionOutWithTotal(BaseModel):
    total_gain: Optional[Decimal] = 0
    total_value: Optional[Decimal] = 0
    transactions: list[TransactionOut]


class CreateTransactionResponse(BaseModel):
    success: bool
    balance: Decimal
