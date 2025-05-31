from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User
from accounts.types import TokenDict


def generate_random_code(length: int = 6) -> str:
    import random

    return "".join(random.choices("0123456789", k=length))


def send_sms(phone_number: str, message: str) -> None:
    print(f"Sending SMS to {phone_number}: {message}")


def generate_jwt_tokens(user: User) -> TokenDict:
    refresh = RefreshToken.for_user(user)
    refresh["role"] = user.role
    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }
