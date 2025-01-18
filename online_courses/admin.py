from django.contrib import admin
from online_courses.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
    )
    list_filter = ("name",)
    search_fields = ("owner", "name")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
    )
    list_filter = ("name",)
    search_fields = ("owner", "name")
