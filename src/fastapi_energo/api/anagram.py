from fastapi import APIRouter
from collections import Counter
import aioredis


from fastapi_energo.settings import REDIS_DATABASE_URL

router = APIRouter(
    prefix='/anagram'
)


@router.get("/{str_1}/{str_2}")
async def anagram(str_1: str, str_2: str):
    redis = aioredis.from_url(REDIS_DATABASE_URL)
    if Counter(str_1) == Counter(str_2):
        return {"is_anagram": True, "count": await redis.incr("some_counter")}
    return {"is_anagram": False, "count": int(await redis.get("some_counter"))}
