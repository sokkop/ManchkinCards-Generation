from functools import lru_cache

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    database_url: str
    jwt_access_cookie_name: str
    jwt_secret_key: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
