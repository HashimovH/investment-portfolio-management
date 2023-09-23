from app.exceptions.username_taken import UsernameAlreadyTaken
from app.schemas.user import UserCreate
from app.models.models import Client


class UserService:
    def __init__(self, user_repository) -> None:
        self._repository = user_repository
    
    async def get_user_by_username(self, username: str) -> Client:
        return await self._repository.get_user_by_username(username)

    async def create_user(self, user: UserCreate) -> Client:
        existing_user = await self.get_user_by_username(user.username)
        if existing_user:
            raise UsernameAlreadyTaken("User already exists")
        return await self._repository.create(user)
    
