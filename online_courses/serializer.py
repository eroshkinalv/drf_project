from rest_framework.serializers import ModelSerializer, SerializerMethodField

from online_courses.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        read_only_fields = ['owner']


class CourseSerializer(ModelSerializer):

    lessons = LessonSerializer(many=True, read_only=True, source="lesson_set")

    lessons_count = SerializerMethodField()

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ("name", "image", "description", "owner", "lessons_count", "lessons")
        read_only_fields = ['owner']
