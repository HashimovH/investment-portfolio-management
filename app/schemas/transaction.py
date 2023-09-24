from pydantic import BaseModel
import datetime

class TransactionIn(BaseModel):
    stock: int
    volume: int

class TransactionOut(BaseModel):
    id: int
    stock: str
    volume: int
    purchase_price: float
    purchase_date: str