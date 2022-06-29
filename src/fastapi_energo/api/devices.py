from fastapi import APIRouter
import asyncpg

from fastapi_energo.settings import USER, PASSWORD, DATABASE, HOST


router = APIRouter(
    prefix='/devices'
)


@router.get('/unattached_stats')
async def get_unattached_devices_stats():
    conn = await asyncpg.connect(
        user=USER, password=PASSWORD, database=DATABASE, host=HOST
    )
    try:
        return await conn.fetch(
            """
        SELECT dev_type, count(*) FROM endpoints RIGHT JOIN devices ON devices.id = endpoints.device_id WHERE endpoints.id IS NULL GROUP BY dev_type
        """
        )
    finally:
        await conn.close()


@router.get("/random", status_code=201)
async def put_random_devices():
    conn = await asyncpg.connect(
        user=USER, password=PASSWORD, database=DATABASE, host=HOST
    )
    try:
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
    finally:
        await conn.close()
