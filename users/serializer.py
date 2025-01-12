from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from online_courses.models import Follow
from users.models import Payment, User


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(ModelSerializer):

    followed_items = SerializerMethodField()

    def get_followed_items(self, user):
        return [follow.course.name for follow in Follow.objects.filter(user=user)]

    class Meta:
        model = User
        fields = ("id", "email", "password", "phone", "image", "city", "followed_items")
