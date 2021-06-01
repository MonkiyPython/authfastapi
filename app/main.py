from fastapi import FastAPI
from app.api.api_v1 import api
from app.core.config import settings
from app.db.database import engine, Base
from app.models.customer import Customer  # noqa  # Need do Fine Alteration

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_VERSION_STR}/openapi.json",
)

Base.metadata.create_all(bind=engine)

app.include_router(api.api_router, prefix=settings.API_VERSION_STR)
