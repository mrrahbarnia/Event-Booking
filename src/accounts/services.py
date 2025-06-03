import logging

from django.core.cache import cache

from accounts import exceptions
from accounts.utils import generate_random_code, send_message, generate_jwt_tokens
from accounts.config import config as Config
from accounts.types import TokenDict
from repositories.repository import RepositoryInterface
from common.exceptions import ServerError

logger = logging.getLogger("accounts")


class AccountService:
    def __init__(self, repository: RepositoryInterface) -> None:
        self._repository = repository

    def login(self, *, phone_number: str) -> None:
        try:
            self._repository.get_user_by_phone_number(phone_number)
            otp = generate_random_code()
            cache.set(otp, phone_number, Config.OTP_LIFETIME_SEC)
            # TODO: Sending OTP via Message
            send_message(phone_number, otp)

        except exceptions.WrongPhoneNumberExc as ex:
            logger.info(ex)
            raise ex

        except Exception as ex:
            logger.warning(ex)
            raise ServerError

    def verify_otp(self, *, otp: str) -> TokenDict:
        try:
            cached_otp = cache.get(otp)  # phone_number
            if not cached_otp:
                raise exceptions.OTPInvalidExc
            user = self._repository.get_user_by_phone_number(cached_otp)
            if user is None:
                raise exceptions.OTPInvalidExc
            return generate_jwt_tokens(user)

        except exceptions.WrongPhoneNumberExc as ex:
            logger.warning(ex)
            raise ex

        except exceptions.OTPInvalidExc as ex:
            logger.info(ex)
            raise ex

        except Exception as ex:
            logger.warning(ex)
            raise ServerError

    def register(self, *, phone_number: str, full_name: str) -> None:
        try:
            otp = generate_random_code()
            self._repository.create_user(phone_number, full_name)
            cache.set(otp, phone_number, Config.OTP_LIFETIME_SEC)
            # TODO: Sending OTP via Message
            send_message(phone_number, otp)

        except Exception as ex:
            logger.warning(ex)
            raise ServerError


def new_account_service(repo: RepositoryInterface) -> AccountService:
    """
    Factory function to create a new instance
    of AccountService and passing repository to it.
    """
    return AccountService(repo)
