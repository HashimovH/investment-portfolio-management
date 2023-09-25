from pydantic import BaseModel
from decimal import Decimal


class Stock(BaseModel):
    id: int
    name: str
    price: Decimal
