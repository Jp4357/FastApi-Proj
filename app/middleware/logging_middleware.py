from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import logging


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logging.info(f"{request.method} {request.url}")
        response = await call_next(request)
        logging.info(f"{response.status_code}")
        return response
