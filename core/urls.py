from core.api.v1.routers import router
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation", default_version="v1.0.0", description="Documentation"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="API Documentation")),
    path("admin/", admin.site.urls),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui()),
    path("", schema_view.with_ui("swagger")),
]
