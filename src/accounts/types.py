from typing import TypedDict
from enum import StrEnum, auto


class UserRole(StrEnum):
    ADMIN = auto()
    SELLER = auto()
    CUSTOMER = auto()


class TokenDict(TypedDict):
    access: str
    refresh: str
