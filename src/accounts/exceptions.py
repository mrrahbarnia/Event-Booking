from rest_framework import status
from rest_framework.exceptions import APIException


class WrongPhoneNumberExc(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "There is no user with the provided phone number"
    default_code = "phone_number_not_found_error"


class OTPInvalidExc(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "The provided OTP is invalid."
    default_code = "otp_invalid_error"
