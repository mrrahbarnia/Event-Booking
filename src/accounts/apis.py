from typing import Any

from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from drf_spectacular.utils import OpenApiResponse, extend_schema

from app.config import config as Config
from accounts import validators
from accounts.services import new_account_service
from repositories.pg_repository import PostgresRepository


class LoginAPI(APIView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._service = new_account_service(PostgresRepository(Config.DEFAULT_DB))

    class LoginInputSerializer(serializers.Serializer):
        phone_number = serializers.CharField(required=True)

        def validate_phone_number(self, value: str) -> str:
            validators.validate_phone_number(value)
            return value

    @extend_schema(
        request=LoginInputSerializer,
        responses={200: OpenApiResponse(description="OTP sent successfully.")},
        summary="Login via phone number",
    )
    def post(self, request: Request) -> Response:
        """
        - **phone_number** must be 11 digits long.
        """
        serializer = self.LoginInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self._service.login(
            phone_number=serializer.validated_data["phone_number"]  # type: ignore[union-attr]
        )
        return Response({"detail": "OTP was sent successfully."}, status.HTTP_200_OK)


class RegisterAPI(APIView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._service = new_account_service(PostgresRepository(Config.DEFAULT_DB))

    class RegisterInputSerializer(serializers.Serializer):
        phone_number = serializers.CharField(required=True)
        full_name = serializers.CharField(max_length=250, required=True)

        def validate_phone_number(self, value: str) -> str:
            validators.validate_phone_number(value)
            return value

    @extend_schema(
        request=RegisterInputSerializer,
        responses={200: OpenApiResponse(description="OTP sent successfully.")},
        summary="Registration endpoint.",
    )
    def post(self, request: Request) -> Response:
        """
        - **phone_number** is required must be 11 digits long.
        - **fullname** is required and must not exceed 250 characters.
        """
        serializer = self.RegisterInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self._service.register(
            phone_number=serializer.validated_data["phone_number"],  # type: ignore[union-attr]
            full_name=serializer.validated_data["full_name"],  # type: ignore[union-attr]
        )
        return Response({"detail": "OTP was sent successfully."}, status.HTTP_200_OK)


class VerifyOTPAPI(APIView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._service = new_account_service(PostgresRepository(Config.DEFAULT_DB))

    class VerifyOtpInputSerializer(serializers.Serializer):
        otp = serializers.CharField(required=True)

    class VerifyOtpOutputSerializer(serializers.Serializer):
        access_token = serializers.CharField()
        refresh_token = serializers.CharField()

    @extend_schema(
        request=VerifyOtpInputSerializer,
        responses={200: OpenApiResponse(description="OTP verified successfully.")},
        summary="Verify OTP",
    )
    def post(self, request: Request) -> Response:
        """
        - **otp** must be a 6-digit code.
        """
        serializer = self.VerifyOtpInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = self._service.verify_otp(
            otp=serializer.validated_data["otp"],  # type: ignore[union-attr]
        )
        return Response(
            {
                "access_token": tokens["access"],
                "refresh_token": tokens["refresh"],
            },
            status.HTTP_200_OK,
        )
