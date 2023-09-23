from fastapi import Depends
from app.repository.user import UserRepository

from app.services.user_service import UserService
from app.dependency.user_repository import get_user_repository

@Depends
def get_user_service(user_repository: UserRepository = get_user_repository):
    return UserService(user_repository)