from functools import lru_cache

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
