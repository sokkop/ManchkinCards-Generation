from pydantic.v1 import BaseSettings


class Settings(BaseSettings):

    @property
    def all_cors_origins(self) -> list[str]:
        return [str(origin).rstrip("/") for origin in
                self.BACKEND_CORS_ORIGINS] + [
            self.FRONTEND_HOST
        ]


settings = Settings()
