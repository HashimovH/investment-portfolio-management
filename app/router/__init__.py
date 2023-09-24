from fastapi import APIRouter
from app.router.user import router as user_router
from app.router.investment import router as investment_router

router = APIRouter(prefix="/api")
router.include_router(user_router)
router.include_router(investment_router)