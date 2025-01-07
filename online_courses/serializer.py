from rest_framework.serializers import ModelSerializer, SerializerMethodField

from online_courses.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):

    lessons_view = LessonSerializer(many=True, read_only=True, source='lesson_set')

    lessons_count = SerializerMethodField()

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ('name', 'image', 'description', 'lessons_count', 'lessons_view')
