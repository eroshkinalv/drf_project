from django.urls import path
from rest_framework.routers import SimpleRouter


from users.apps import UsersConfig
from users.views import PaymentViewSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r'payment', PaymentViewSet)

urlpatterns = []

urlpatterns += router.urls
