from typing import Any

from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from drf_spectacular.utils import OpenApiResponse, extend_schema

from accounts.services import new_account_service


class LoginAPI(APIView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.service = new_account_service()

    class InputSerializer(serializers.Serializer):
        phone_number = serializers.CharField(required=True)

        def validate_phone_number(self, value: str) -> str:
            if len(value) != 11:
                raise serializers.ValidationError("Phone number must be 11 digits long")
            return value

    @extend_schema(
        request=InputSerializer,
        responses={200: OpenApiResponse(description="OTP sent successfully.")},
        summary="Login via phone number",
    )
    def post(self, request: Request) -> Response:
        """
        - **phone_number** must be 11 digits long.
        """
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.service.login(
            phone_number=serializer.validated_data["phone_number"]  # type: ignore[union-attr]
        )
        return Response({"detail": "OTP was sent successfully."}, status.HTTP_200_OK)
