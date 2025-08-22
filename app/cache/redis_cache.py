import json
import redis
from app.core.config import settings

redis_client = redis.from_url(settings.REDIS_URL)


def get_cached_prediction(key: str):
    value = redis_client.get(key)
    if value is None:
        return None
    return json.loads(value)


def set_cached_prediction(key: str, value: dict, expiration_time: int = 3600):
    redis_client.setex(key, json.dumps(value), expiration_time)
