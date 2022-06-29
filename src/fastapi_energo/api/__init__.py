from fastapi import APIRouter

from .devices import router as devices_router
from .anagram import router as anagram_router

router = APIRouter()
router.include_router(anagram_router)
router.include_router(devices_router)
