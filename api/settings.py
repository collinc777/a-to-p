from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow")
    openai_api_key: str
    bucket_access_key_id: str
    bucket_secret_access_key: str
    bucket_url: str
    bucket_public_url: str
    aws_region: str
    aws_default_region: str
    database_url: str
    sentry_dsn: str
    stage: str
    edenai_api_key: str


@lru_cache()
def get_settings():
    return Settings()  # type: ignore
