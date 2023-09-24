from fastapi import APIRouter, Depends, HTTPException, status, Header
from app.dependency.investment_service import get_investment_service
from app.dependency.user_service import get_user_service
from app.exceptions.insufficient_balance import InsufficientBalance
from app.router.user import get_current_user
from app.schemas.stock import Stock
from app.schemas.transaction import TransactionOut, TransactionIn

from app.services.investment_service import InvestmentService
from app.services.user_service import UserService

router = APIRouter(tags=["Investment"])

@router.get("/stocks", response_model=list[Stock])
async def get_current_user_route(service: InvestmentService = get_investment_service):
    stocks = await service.get_all_stocks()
    result = []
    for stock in stocks:
        result.append(Stock(id=stock.id, name=stock.name, price=stock.price))
    return result

@router.get("/transactions", response_model=list[TransactionOut])
async def get_current_user_route(
    service: InvestmentService = get_investment_service, 
    user_service: UserService = get_user_service, 
    current_user: str = Depends(get_current_user)
):
    user = await user_service.get_user_by_username(current_user)
    transactions = await service.get_user_transactions(user.id)
    result = []
    for transaction in transactions:
        formatted_datetime = transaction[0].created_at.strftime('%Y-%m-%d %H:%M')
        print(transaction)
        result.append(TransactionOut(id=transaction[0].id, stock=transaction[1], current_price=transaction[2],volume=transaction[0].volume, price=round(transaction[0].price, 3),purchase_price=transaction[0].purchase_price, purchase_date=formatted_datetime))
    return result

@router.post("/transactions", response_model=bool)
async def create_new_transaction(
    body: TransactionIn,
    service: InvestmentService = get_investment_service, 
    user_service: UserService = get_user_service, 
    current_user: str = Depends(get_current_user)
):
    try:
        user = await user_service.get_user_by_username(current_user)
        await service.create_new_transaction(user.id, user.balance, body.stock, body.volume)
        return True
    except InsufficientBalance as e:
        return HTTPException(status_code=400, detail=str(e))