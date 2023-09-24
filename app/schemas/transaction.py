from typing import Optional
from pydantic import BaseModel
import datetime

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