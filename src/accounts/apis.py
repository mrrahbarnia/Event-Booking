from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


class HealthCheckAPI(APIView):
    def get(self, request: Request) -> Response:
        return Response("OK", status.HTTP_200_OK)
