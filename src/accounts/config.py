from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ADMIN_PANNEL_PASSWD: str
    PHONE_NUMBER_REGEX: str


config = Config()  # type: ignore[call-arg]
