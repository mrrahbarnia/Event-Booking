from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from app.config import config as Config

urlpatterns = [
    path("admin/", admin.site.urls),
    # API endpoints
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # Accounts app URLs
    path("accounts/", include("accounts.urls")),
]

if Config.ENVIRONMENT.is_debug:
    urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
