from typing import Optional

from pydantic import BaseModel, validator


class UserCreate(BaseModel):
    username: str
    password: str
    name: str
    surname: str


class UserOut(UserCreate):
    id: int
    balance: Optional[float] = 0

    @validator("balance", pre=True, always=True)
    def round_balance(cls, value):
        if value is not None:
            return round(value, 3)
        return value

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    username: str
    password: str


class ProfitableUsers(BaseModel):
    name: str
    surname: str
    profit: float
