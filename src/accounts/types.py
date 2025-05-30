from enum import StrEnum, auto


class UserRole(StrEnum):
    ADMIN = auto()
    SELLER = auto()
    CUSTOMER = auto()
