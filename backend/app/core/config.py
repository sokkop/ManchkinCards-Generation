from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"


settings = Settings()

