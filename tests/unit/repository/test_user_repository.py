import pytest
from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError

from app.models.models import Client
from app.repository.user import UserRepository
from app.schemas.user import UserCreate
from app.utils.auth import verify_password


@pytest.fixture
async def repository(db_session):
    return UserRepository(db_session)


@pytest.mark.asyncio
async def test_get_user_by_username(repository, db_session):
    user_data = {
        "username": "test_user",
        "password": "testpassword",
        "name": "Test",
        "surname": "User",
        "email": "test@example.com",
        "active": 1,
        "balance": 1000.0,
    }
    await db_session.execute(
        insert(Client).values(
            username=user_data["username"],
            password=user_data["password"],
            name=user_data["name"],
            surname=user_data["surname"],
            email=user_data["email"],
            active=user_data["active"],
            balance=user_data["balance"],
        )
    )
    await db_session.commit()
    # Retrieve the user by username
    retrieved_user = await repository.get_user_by_username(user_data["username"])

    assert retrieved_user is not None
    assert retrieved_user.username == user_data["username"]
    assert retrieved_user.name == user_data["name"]
    assert retrieved_user.surname == user_data["surname"]
    assert retrieved_user.email == user_data["email"]
    assert retrieved_user.active == user_data["active"]
    assert retrieved_user.balance == user_data["balance"]
