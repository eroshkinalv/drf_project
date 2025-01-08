from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from online_courses.models import Course, Unit
from online_courses.serializer import CourseSerializer, UnitSerializer


class CourseViewSet(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class UnitCreateApiView(CreateAPIView):

    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class UnitListApiView(ListAPIView):

    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class UnitRetrieveApiView(RetrieveAPIView):

    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class UnitUpdateApiView(UpdateAPIView):

    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class UnitDestroyApiView(DestroyAPIView):

    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
