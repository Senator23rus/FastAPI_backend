from fastapi import APIRouter
from .auth import router as auth_router
from .country import router as country_router
from .industry import router as industry_router
# from .operations import router as operations_router
# from .reports import router as reports_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(country_router)
router.include_router(industry_router)