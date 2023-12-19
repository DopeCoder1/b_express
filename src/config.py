from typing import Any

from pydantic import PostgresDsn, model_validator
from pydantic_settings import BaseSettings

from src.constants import Environment

class Config(BaseSettings):
    DATABASE_URL: PostgresDsn
    ENVIRONMENT: Environment = Environment.LOCAL
    SITE_DOMAIN: str = "http://localhost:8000"

    SENTRY_DSN: str | None = None

    CORS_ORIGINS: list[str]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str]

    APP_VERSION: str = "1"

    @model_validator(mode="after")
    def validate_sentry_non_local(self) -> "Config":
        if self.ENVIRONMENT.is_deployed and not self.SENTRY_DSN:
            raise ValueError("SENTRY_DSN is required in production")
        return self
    
settings = Config()

app_configs: dict[str, Any] = {"title": "B-Express API"}
if settings.ENVIRONMENT.is_deployed:
    app_configs["root_path"] = "/api/v{settings.APP_VERSION}"

if not settings.ENVIRONMENT.is_debug:
    app_configs["openapi_url"] = None


