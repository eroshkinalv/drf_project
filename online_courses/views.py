from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    get_object_or_404,
)

from online_courses.models import Course, Lesson, Follow
from online_courses.paginators import LessonPagination, CoursePagination
from online_courses.serializer import CourseSerializer, LessonSerializer, FollowSerializer
from users.permissions import IsModer, IsOwner


class CourseViewSet(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):

        if self.action in ["list", "retrieve", "update", "destroy", "partial_update"]:
            self.permission_classes = (IsModer | IsOwner,)

        elif self.action == "destroy":
            self.permission_classes = (~IsModer | IsOwner,)

        elif self.action == "create":
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
    permission_classes = (
        IsAuthenticated,
        IsOwner | IsModer,
    )
    pagination_class = LessonPagination


class LessonRetrieveApiView(RetrieveAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner | IsModer,
    )


class LessonUpdateApiView(UpdateAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner | IsModer,
    )


class LessonDestroyApiView(DestroyAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner | ~IsModer,
    )


class FollowListApiView(ListAPIView):

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, ~IsModer)

    def post(self, *args, **kwargs):

        user = self.request.user
        course_id = self.request.data.get("course")
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = Follow.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = "подписка удалена"

        else:
            Follow.objects.create(user=user, course=course_item)
            message = "подписка добавлена"

        return Response({"message": message})
