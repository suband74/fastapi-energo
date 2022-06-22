from fastapi import FastAPI
from collections import Counter
import aioredis
import asyncpg

app = FastAPI()


@app.get("/anagram/{str_1}/{str_2}")
async def anagram(str_1: str, str_2: str):
    redis = aioredis.from_url("redis://anagrams_db")
    if Counter(str_1) == Counter(str_2):
        return {"is_anagram": True, "count": await redis.incr("some_counter")}
    return {"is_anagram": False, "count": int(await redis.get("some_counter"))}


@app.get("/devices/random", status_code=201)
async def put_random_devices():
    conn = await asyncpg.connect(
        user="postgres", password="postgres", database="postgres", host="devices_db"
    )

    await conn.execute(
        """
    create table if not exists devices
    (
    id  bigserial  not null  constraint devices_pk  primary key,
    dev_id   varchar(200) not null,
    dev_type  varchar(120) not null
    )
    """
    )

    await conn.execute(
        """
    create  index  if not exists devices_dev_id_dev_type_index on devices (dev_id, dev_type)
    """
    )

    await conn.execute(
        """
    create table  if not exists endpoints
    (
    id bigserial not null constraint endpoints_pk primary key,
    device_id integer constraint endpoints_devices_id_fk references devices on update cascade on delete cascade,
    comment   text
    )
    """
    )

    await conn.execute(
        """
    WITH devices_ids as (
        INSERT INTO devices (dev_type, dev_id)
        SELECT (ARRAY['emeter', 'zigbee', 'lora', 'gsm'])[FLOOR(RANDOM() * 4 + 1)], LEFT(MD5(RANDOM()::TEXT), 12)
        FROM generate_series(1, 10)
        RETURNING devices.id
    )
    INSERT INTO endpoints (device_id) SELECT * FROM devices_ids ORDER BY random() LIMIT 5
    """
    )

    return {
        " The tables DEVICES and ENDPOINTS": " Have been created or modified successfully"
    }


@app.get("/devices/unattached_stats")
async def get_unattached_devices_stats():
    conn = await asyncpg.connect(
        user="postgres", password="postgres", database="postgres", host="devices_db"
    )

    return await conn.fetch(
        """
    SELECT dev_type, count(*) FROM endpoints RIGHT JOIN devices ON devices.id = endpoints.device_id WHERE endpoints.id IS NULL GROUP BY dev_type
    """
    )
