from fastapi import APIRouter, Depends, HTTPException
from app.dependency.user_service import get_user_service
from app.exceptions.username_taken import UsernameAlreadyTaken

from app.schemas.user import UserCreate, UserOut
from app.services.user_service import UserService
from app.utils.auth import verify_password, create_access_token


router = APIRouter(tags=["User"])

@router.post(
    "/register",
    status_code=201,
    description="Register a new user",
    response_model = UserOut
)
async def register(
    user_create: UserCreate,
    service: UserService = get_user_service
):
    try:
        user = await service.create_user(user_create)
    except UsernameAlreadyTaken as e:
        raise HTTPException(status_code=400, detail=str(e))
        
    return user

@router.post("/login/")
async def login(username: str, password: str, service: UserService = get_user_service):
    user = await service.get_user_by_username(username)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}