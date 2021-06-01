from fastapi import FastAPI
from app.api.api_v1 import api
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_VERSION_STR}/openapi.json",
)

app.include_router(api.api_router, prefix=settings.API_VERSION_STR)
