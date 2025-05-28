from typing import Any

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser


class CustomUserManager(BaseUserManager):
    def create_user(
        self, phone_number: str, password: str, **extra_fields: Any
    ) -> AbstractBaseUser:
        if not phone_number:
            raise ValueError("The Phone Number field must be set")
        if len(phone_number) != 11:
            raise ValueError("The Phone Number must be 11 digits long")
        user: AbstractBaseUser = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_super_user(self, phone_number: str, password: str, **extra_fields: Any):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Super user must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self.create_user(phone_number, password, **extra_fields)
