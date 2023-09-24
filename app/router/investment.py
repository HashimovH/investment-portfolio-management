from fastapi import APIRouter, Depends, HTTPException, status, Header
from app.dependency.investment_service import get_investment_service
from app.dependency.user_service import get_user_service
from app.exceptions.insufficient_balance import InsufficientBalance
from app.router.user import get_current_user
from app.schemas.stock import Stock
from app.schemas.transaction import TransactionOut, TransactionIn, TransactionOutWithTotal

from app.services.investment_service import InvestmentService
from app.services.user_service import UserService

router = APIRouter(tags=["Investment"])

@router.get("/stocks", response_model=list[Stock])
async def get_available_stocks(service: InvestmentService = get_investment_service):
    stocks = await service.get_all_stocks()
    result = []
    for stock in stocks:
        result.append(Stock(id=stock.id, name=stock.name, price=stock.price))
    return result

@router.get("/transactions", response_model=TransactionOutWithTotal)
async def get_user_transactions(
    service: InvestmentService = get_investment_service, 
    user_service: UserService = get_user_service, 
    current_user: str = Depends(get_current_user)
):
    user = await user_service.get_user_by_username(current_user)
    transactions = await service.get_user_transactions(user.id)
    return transactions

@router.post("/transactions", response_model=bool, status_code=status.HTTP_201_CREATED)
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
        raise HTTPException(status_code=400, detail=str(e))