from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ADMIN_PANNEL_PASSWD: str
    PHONE_NUMBER_REGEX: str
    OTP_LIFETIME_SEC: int


config = Config()  # type: ignore[call-arg]
