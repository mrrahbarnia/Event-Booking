from django.urls import path

from accounts import apis

urlpatterns = [
    path("login/", apis.LoginAPI.as_view(), name="login"),
    path("verify-otp/", apis.VerifyOTPAPI.as_view(), name="verify_otp"),
    path("register/", apis.RegisterAPI.as_view(), name="register"),
]
