from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этокого рекоммендуется использовать SimpleRouter

# TODO Oпределять views в нашем случае необязательно — Djoser делает это из коробки.
from ads.views.ads import UserUploadImageView

users_router = SimpleRouter()

# обратите внимание, что здесь в роуте мы регистрируем ViewSet,
# который импортирован из приложения Djoser

users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(users_router.urls)),
    path('auth/password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('auth/password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('user/<int:pk>/upload_image/', UserUploadImageView.as_view(), name='user_upload_image'),
]

