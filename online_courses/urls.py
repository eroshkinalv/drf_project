from django.urls import path
from rest_framework.routers import SimpleRouter

from online_courses.views import (
    CourseViewSet,
    LessonCreateApiView,
    LessonListApiView,
    LessonRetrieveApiView,
    LessonUpdateApiView,
    LessonDestroyApiView, FollowListApiView,
)

from online_courses.apps import OnlineCoursesConfig

app_name = OnlineCoursesConfig.name

router = SimpleRouter()

router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lesson_list"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson_retrieve"),
    path("lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lesson_update"),
    path("lessons/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="lesson_delete"),

    path("follows/", FollowListApiView.as_view(), name="follow_list"),
]

urlpatterns += router.urls
