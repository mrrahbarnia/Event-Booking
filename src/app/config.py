from enum import StrEnum, auto

from pydantic_settings import BaseSettings


class Environment(StrEnum):
    LOCAL = auto()
    PRODUCTION = auto()

    @property
    def is_debug(self) -> bool:
        return self == self.LOCAL


class Config(BaseSettings):
    ENVIRONMENT: Environment = Environment.PRODUCTION
    SECRET_KEY: str = "test"
    ALLOWED_HOSTS: list[str]
    DEFAULT_DB: str
    DB_ENGINE: str
    DB_PASSWORD: str
    DB_USER: str
    DB_NAME: str
    DB_PORT: int
    DB_HOST: str
    REDIS_URL: str
    ACCESS_TOKEN_LIFE_TIME_MIN: int
    REFRESH_TOKEN_LIFE_TIME_DAY: int
    JWT_ALGORITHM: str


config = Config()  # type: ignore[call-arg]
