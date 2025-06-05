from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = "Добавьте пользователя"

    def handle(self, *args, **kwargs):

        user = User.objects.create(email="another_user@example.com")

        user.set_password("123zaq")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = False
        user.last_login = "2024-01-18"
        user.save()
