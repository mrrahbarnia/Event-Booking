from django.urls import path

from accounts import apis

urlpatterns = [
    path("health-check/", apis.HealthCheckAPI.as_view(), name="health_check"),
]
