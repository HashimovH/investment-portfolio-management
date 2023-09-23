from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    name: str
    surname: str

class UserOut(UserCreate):
    id: int
    class Config:
        orm_mode = True
    
class UserLogin(BaseModel):
    username: str
    password: str