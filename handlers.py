from services import logger
from fastapi.exception_handlers import http_exception_handler

async def custom_http_exception_handler(request, exc):
    logger.exception(f"{exc.detail}")
    return await http_exception_handler(request, exc)