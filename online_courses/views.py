from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from online_courses.models import Course, Lesson
from online_courses.serializer import CourseSerializer, LessonSerializer
from users.permissions import IsModer, IsOwner


class CourseViewSet(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):

        if self.action in ['list', 'retrieve', 'update', 'destroy', 'partial_update']:
            self.permission_classes = (IsModer | IsOwner,)

        elif self.action == 'destroy':
            self.permission_classes = (~IsModer | IsOwner,)

        elif self.action == 'create':
            self.permission_classes = (~IsModer,)

        return super().get_permissions()


class LessonCreateApiView(CreateAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, ~IsModer)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListApiView(ListAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | IsModer,)


class LessonRetrieveApiView(RetrieveAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | IsModer,)


class LessonUpdateApiView(UpdateAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | IsModer,)


class LessonDestroyApiView(DestroyAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | ~IsModer,)
