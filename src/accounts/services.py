from functools import lru_cache

from repositories.repository import RepositoryInterface
from repositories.pg_repository import PostgresRepository


class AccountService:
    def __init__(self, repository: RepositoryInterface) -> None:
        self._repository = repository

    def login(self, *, phone_number: str):
        self._repository.get_user_by_phone_number(phone_number)


@lru_cache
def new_account_service(repo: RepositoryInterface | None = None) -> AccountService:
    """
    Factory function to create a new instance
    of AccountService and passing repository to it.
    """
    return AccountService(repo or PostgresRepository())
