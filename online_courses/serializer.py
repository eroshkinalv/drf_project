from rest_framework.serializers import ModelSerializer, SerializerMethodField

from online_courses.models import Course, Lesson, Follow
from online_courses.validators import VideoValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        read_only_fields = ['owner']
        validators = [VideoValidator(field='video')]


class CourseSerializer(ModelSerializer):

    follow = SerializerMethodField()

    def get_follow(self, course):
        if Follow.objects.filter(course=course):
            return True
        return False

    lessons = LessonSerializer(many=True, read_only=True, source="lesson_set")

    lessons_count = SerializerMethodField()

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ("name", "image", "description", "owner", "lessons_count", "lessons", "follow")
        read_only_fields = ['owner']


class FollowSerializer(ModelSerializer):
    class Meta:
        model = Follow
        fields = "__all__"
