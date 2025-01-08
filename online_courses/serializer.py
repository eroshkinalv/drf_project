from rest_framework.serializers import ModelSerializer

from online_courses.models import Course, Unit


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class UnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'
