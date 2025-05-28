from pydantic_settings import BaseSettings


class Config(BaseSettings):
    PHONE_NUMBER_REGEX: str


config = Config()  # type: ignore[call-arg]
