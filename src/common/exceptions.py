from rest_framework import status
from rest_framework.exceptions import APIException


class ServerError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "Something unexpected occured."
    default_code = "unexpected_error"
