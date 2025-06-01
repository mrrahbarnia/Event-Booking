from accounts import exceptions
from app.config import config as Config
from accounts.models import User


class PostgresRepository:
    def __init__(self, db_alias: str = Config.DEFAULT_DB) -> None:
        self._db_alias = db_alias

    def create_user(self, phone_number: str, full_name: str) -> None:
        """Create a new user in the database."""
        user = User(phone_number=phone_number, full_name=full_name)
        user.full_clean()
        user.save(using=self._db_alias)

    def get_user_by_phone_number(self, phone_number: str) -> User | None:
        """Retrieve a user by their phone number."""
        try:
            return User.objects.using(self._db_alias).get(phone_number=phone_number)
        except User.DoesNotExist:
            raise exceptions.WrongPhoneNumberExc
