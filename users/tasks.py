import datetime
from datetime import timedelta

from celery import shared_task

from users.models import User


@shared_task
def check_active_users():
    """Блокирует пользователя, если он не заходил более месяца."""

    for user in User.objects.filter(is_active=True):
        date = datetime.datetime.now().date()
        delta = timedelta(days=120)
        if user.last_login:
            if user.last_login + delta < date:
                user.is_active = False
                user.save()
