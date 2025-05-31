from typing import Protocol

from accounts.models import User


class RepositoryInterface(Protocol):
    def __init__(self, db_alias: str) -> None:
        """Initialize the repository with a database alias."""
        ...

    def create_user(self, phone_number: str, full_name: str) -> None:
        """Create a new user in the database."""
        ...

    def get_user_by_phone_number(self, phone_number: str) -> User | None:
        """Retrieve a user by their phone number."""
        ...
