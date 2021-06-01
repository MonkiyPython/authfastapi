from pydantic import BaseSettings


class Settings(BaseSettings):
    API_VERSION_STR: str = "/api/v1"

    PROJECT_NAME: str = "FastAPI Authentication Project"


settings = Settings()
