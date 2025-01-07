from rest_framework.viewsets import ModelViewSet

from users.models import Payment
from users.serializer import PaymentSerializer


class PaymentViewSet(ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_fields = ['date', 'payment_method', 'course', 'lesson']
