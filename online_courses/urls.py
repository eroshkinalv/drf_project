from django.urls import path
from rest_framework.routers import SimpleRouter

from online_courses.views import CourseViewSet, UnitCreateApiView, UnitListApiView, UnitRetrieveApiView, UnitUpdateApiView, UnitDestroyApiView

from online_courses.apps import OnlineCoursesConfig

app_name = OnlineCoursesConfig.name

router = SimpleRouter()

router.register('', CourseViewSet)

urlpatterns = [
    path("units/", UnitListApiView.as_view(), name='unit_list'),
    path("units/create/", UnitCreateApiView.as_view(), name='unit_create'),
    path("units/<int:pk>/", UnitRetrieveApiView.as_view(), name='unit_retrieve'),
    path("units/<int:pk>/update/", UnitUpdateApiView.as_view(), name='unit_update'),
    path("units/<int:pk>/delete/", UnitDestroyApiView.as_view(), name='unit_delete'),
]

urlpatterns += router.urls
