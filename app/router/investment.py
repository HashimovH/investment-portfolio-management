from fastapi import APIRouter, Depends, HTTPException, status, Header
from app.dependency.investment_service import get_investment_service
from app.router.user import get_current_user
from app.schemas.stock import Stock

from app.services.investment_service import InvestmentService

router = APIRouter(tags=["Investment"])

@router.get("/stocks", response_model=list[Stock], description="Get current user")
async def get_current_user_route(service: InvestmentService = get_investment_service):
    stocks = await service.get_all_stocks()
    result = []
    for stock in stocks:
        print(stock)
        result.append(Stock(id=stock.id, name=stock.name, price=stock.price))
    return result