from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("online_courses/", include('online_courses.urls', namespace='online_courses')),
]
