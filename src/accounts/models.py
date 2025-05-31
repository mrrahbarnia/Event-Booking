import re

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.core.exceptions import ValidationError

from accounts.managers import CustomUserManager
from accounts.config import config as Config
from accounts.types import UserRole


ROLE_CHOICES = [
    ("CUSTOMER", "CUSTOMER"),
    ("ADMIN", "ADMIN"),
    ("SELLER", "SELLER"),
]


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(unique=True)
    password = models.CharField(max_length=128, blank=True)
    full_name = models.CharField(max_length=250)
    role = models.CharField(
        choices=ROLE_CHOICES, default=UserRole.CUSTOMER.name.upper()
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    registered_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(phone_number__regex=Config.PHONE_NUMBER_REGEX),
                name="phone_number_length_check",
            )
        ]

    def clean(self) -> None:
        if re.fullmatch(Config.PHONE_NUMBER_REGEX, self.phone_number) is None:
            raise ValidationError(
                f"Phone number must match the regex: {Config.PHONE_NUMBER_REGEX}"
            )

    def __str__(self) -> str:
        return self.phone_number
