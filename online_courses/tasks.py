from celery import shared_task
import os
from django.core.mail import send_mail

from online_courses.models import Lesson, Follow


@shared_task
def check_update(pk):
    """Высылает сообщение на почту, если на курсе, на который подписан пользователь, появился новый урок"""

    lesson = Lesson.objects.filter(pk=pk).first()

    if Follow.objects.filter(user=lesson.owner, course=lesson.course):

        send_mail(
            f"Обновление курса {lesson.course}",
            f"На курсе '{lesson.course}' был добавлен урок '{lesson.name}'.",
            os.getenv("EMAIL_HOST_USER"),
            [f"{lesson.owner.email}"],
            fail_silently=False,
        )
