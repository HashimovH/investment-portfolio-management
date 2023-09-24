from fastapi import Depends
from app.dependency.investment_repository import get_investment_repository
from app.dependency.user_repository import get_user_repository
from app.repository.investment import InvestmentRepository
from app.repository.user import UserRepository
from app.services.investment_service import InvestmentService

@Depends
def get_investment_service(repository: InvestmentRepository = get_investment_repository, user_repository: UserRepository = get_user_repository):
    return InvestmentService(repository, user_repository)