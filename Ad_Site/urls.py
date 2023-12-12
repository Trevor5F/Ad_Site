from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("api/admin/", admin.site.urls),
    path('api/drf-auth/', include('rest_framework.urls')),
    path("api/redoc-tasks/", include("redoc.urls")),
    path("", include("ads.urls")),
    path("", include("users.urls")),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema')),

    # Djoser создаст набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    path('api/auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('auth/', include('djoser.urls.jwt')),
]


if settings.DEBUG:
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                             document_root=settings.MEDIA_ROOT)
