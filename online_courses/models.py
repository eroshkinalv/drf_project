from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Название курса')
    image = models.ImageField(upload_to='course_img/', null=True, blank=True, verbose_name='Превью (картинка)')
    description = models.TextField(null=True, blank=True, verbose_name='Описание курса')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Название урока')
    description = models.TextField(null=True, blank=True, verbose_name='Описание урока')
    image = models.ImageField(upload_to='unit_img/', null=True, blank=True, verbose_name='Превью (картинка)')
    video = models.CharField(null=True, blank=True, verbose_name='Ссылка на видео')

    course = models.ForeignKey(Course, on_delete=models.SET, verbose_name='Название курса', related_name='lesson_set')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name
