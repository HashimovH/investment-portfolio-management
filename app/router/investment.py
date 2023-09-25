from fastapi import APIRouter, Depends, HTTPException, status

from app.dependency.investment_service import get_investment_service
from app.dependency.user_service import get_user_service
from app.exceptions.insufficient_balance import InsufficientBalance
from app.router.user import get_current_user
from app.schemas.stock import Stock
from app.schemas.transaction import (
    CreateTransactionResponse,
    TransactionIn,
    TransactionOutWithTotal,
)
from app.services.investment_service import InvestmentService
from app.services.user_service import UserService
import logging

router = APIRouter(tags=["Investment"])
logger = logging.getLogger(__name__)


@router.get("/stocks", response_model=list[Stock])
async def get_available_stocks(service: InvestmentService = get_investment_service):
    try:
        stocks = await service.get_all_stocks()
        result = []
        for stock in stocks:
            result.append(Stock(id=stock.id, name=stock.name, price=stock.price))
        return result
    except Exception as e:
        logger.error(f"Error while getting stocks, {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/transactions", response_model=TransactionOutWithTotal)
async def get_user_transactions(
    service: InvestmentService = get_investment_service,
    user_service: UserService = get_user_service,
    current_user: str = Depends(get_current_user),
):
    try:
        user = await user_service.get_user_by_username(current_user)
        transactions = await service.get_user_transactions(user.id)
        return transactions
    except Exception as e:
        logger.error(f"Error while getting user transactions, {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post(
    "/transactions",
    response_model=CreateTransactionResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_new_transaction(
    body: TransactionIn,
    service: InvestmentService = get_investment_service,
    user_service: UserService = get_user_service,
    current_user: str = Depends(get_current_user),
):
    try:
        user = await user_service.get_user_by_username(current_user)
        _, balance = await service.create_new_transaction(
            user.id, user.balance, body.stock, body.volume
        )
        response = CreateTransactionResponse(success=True, balance=balance)
        return response
    except InsufficientBalance as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error while creating new transaction, {e}")
        raise HTTPException(status_code=500, detail=str(e))
