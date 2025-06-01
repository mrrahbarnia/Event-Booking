from rest_framework import serializers


def validate_phone_number(phone_number: str) -> None:
    if len(phone_number) != 11:
        raise serializers.ValidationError("Phone number must be 11 digits long")
