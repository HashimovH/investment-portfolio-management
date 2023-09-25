from app.exceptions.username_taken import UsernameAlreadyTaken
from app.models.models import Client
from app.schemas.user import UserCreate


class UserService:
    def __init__(self, user_repository) -> None:
        self._repository = user_repository

    async def get_user_by_username(self, username: str) -> Client:
        return await self._repository.get_user_by_username(username)
