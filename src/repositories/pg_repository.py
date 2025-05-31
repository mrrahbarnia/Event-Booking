from app.config import config as Config
from accounts.models import User

from rest_framework.exceptions import NotFound


class PostgresRepository:
    def __init__(self, db_alias: str = Config.DEFAULT_DB) -> None:
        self.db_alias = db_alias

    def get_user_by_phone_number(self, phone_number: str) -> User:
        """Retrieve a user by their phone number."""
        try:
            return User.objects.using(self.db_alias).get(phone_number=phone_number)
        except User.DoesNotExist:
            raise NotFound("Redirect to register page.")
