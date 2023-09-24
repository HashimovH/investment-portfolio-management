from fastapi import APIRouter, Depends, HTTPException, status, Header
from app.dependency.user_service import get_user_service
from app.exceptions.username_taken import UsernameAlreadyTaken

from app.schemas.user import UserCreate, UserOut, UserLogin
from app.services.user_service import UserService
from app.utils.auth import verify_password, create_access_token, verify_token


def get_current_user(authorization: str = Header(...)):
    token = authorization.split()[1]
    print(token)
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = verify_token(token)
    return token.get("sub")

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

@router.post("/login", status_code=200, description="Login")
async def login(body: UserLogin, service: UserService = get_user_service):
    user = await service.get_user_by_username(body.username)
    if not user or not verify_password(body.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut, description="Get current user")
async def get_current_user_route(service: UserService = get_user_service, current_user: str = Depends(get_current_user)):
    user = await service.get_user_by_username(current_user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user