from django.urls import path

from accounts import apis

urlpatterns = [
    path("login/", apis.LoginAPI.as_view(), name="login"),
]
