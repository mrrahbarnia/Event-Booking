from typing import Protocol

from accounts.models import User


class RepositoryInterface(Protocol):
    def __init__(self, db_alias: str) -> None:
        """Initialize the repository with a database alias."""
        ...

    def get_user_by_phone_number(self, phone_number: str) -> User:
        """Retrieve a user by their phone number."""
        ...
