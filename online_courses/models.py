from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Название курса')
    image = models.ImageField(upload_to='course_img/', null=True, blank=True, verbose_name='Превью (картинка)')
    description = models.TextField(null=True, blank=True, verbose_name='Описание курса')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Unit(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Название урока', help_text='Укажите название урока')
    description = models.TextField(null=True, blank=True, verbose_name='Описание урока')
    image = models.ImageField(upload_to='unit_img/', null=True, blank=True, verbose_name='Превью (картинка)')

    course = models.ForeignKey(Course, on_delete=models.SET, verbose_name='Название курса')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
