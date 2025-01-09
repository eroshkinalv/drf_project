from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import PaymentViewSet, UserCreateApiView, UserListApiView, UserRetrieveApiView, UserUpdateApiView, \
    UserDestroyApiView

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"payment", PaymentViewSet)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
    path("register/", UserCreateApiView.as_view(), name="register"),

    path("user/", UserListApiView.as_view(), name="user_list"),
    path("user/", UserRetrieveApiView.as_view(), name="user_retrieve"),
    path("user/", UserUpdateApiView.as_view(), name="user_update"),
    path("user/", UserDestroyApiView.as_view(), name="user_destroy"),
]

urlpatterns += router.urls
