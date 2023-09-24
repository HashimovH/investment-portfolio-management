from app.exceptions.username_taken import UsernameAlreadyTaken
from app.schemas.user import UserCreate
from app.models.models import Stock


class InvestmentService:
    def __init__(self, repository) -> None:
        self._repository = repository
    
    async def get_all_stocks(self) -> Stock:
        return await self._repository.get_all_active_stocks()
    
