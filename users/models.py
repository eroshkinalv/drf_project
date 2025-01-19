from django.db import models
from django.contrib.auth.models import AbstractUser

from online_courses.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=120, null=True, blank=True, verbose_name="Телефон")
    image = models.ImageField(upload_to="profile_img/", null=True, blank=True, verbose_name="Аватар")
    city = models.CharField(max_length=120, null=True, blank=True, verbose_name="Город")

    last_login = models.DateField(auto_now_add=True, verbose_name="Последняя активность", null=True, blank=True,)
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты")
    course = models.ForeignKey(
        Course, verbose_name="Оплаченный курс", on_delete=models.SET_NULL, null=True, blank=True
    )
    lesson = models.ForeignKey(
        Lesson, verbose_name="Оплаченный урок", on_delete=models.SET_NULL, null=True, blank=True
    )
    payment_amount = models.PositiveIntegerField(default=0, verbose_name="Сумма оплаты")

    METHOD_CHOICES = (("Наличные", "Наличные"), ("Перевод на счет", "Перевод на счет"))
    payment_method = models.CharField(max_length=250, verbose_name="Способ оплаты", choices=METHOD_CHOICES)

    session_id = models.CharField(max_length=250, verbose_name="id сессии платежа", null=True, blank=True)
    payment_link = models.URLField(max_length=400, verbose_name="Ссылка на оплату", null=True, blank=True)
    status = models.CharField(
        max_length=250,
        verbose_name="Статус платежа",
        null=True,
        blank=True,
        help_text="complete(оплачен)/expired(не действителен)/open(ожидает оплаты)",
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __int__(self):
        return self.payment_amount
