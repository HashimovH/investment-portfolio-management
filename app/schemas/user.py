from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    name: str
    surname: str

class UserOut(UserCreate):
    id: int
    balance: Optional[float] = 0
    class Config:
        orm_mode = True
    
class UserLogin(BaseModel):
    username: str
    password: str