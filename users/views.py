from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from users.models import Payment, User
from users.serializer import PaymentSerializer, UserSerializer
from users.services import create_stripe_session, create_stripe_price, create_stripe_product, create_stripe_checkout


class PaymentViewSet(ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_fields = ["date", "payment_amount", "payment_method", "course", "lesson"]

    def perform_create(self, serializer):

        user_payment = serializer.save(user=self.request.user)
        product = create_stripe_product(user_payment.course if user_payment.course else user_payment.lesson)
        amount = create_stripe_price(user_payment.payment_amount, product)
        session_id, payment_link = create_stripe_session(amount)
        user_payment.session_id = session_id
        user_payment.payment_link = payment_link
        checkout = create_stripe_checkout(session_id)
        user_payment.status = checkout.status
        user_payment.save()


class UserCreateApiView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):

        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListApiView(ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveApiView(RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateApiView(UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyApiView(DestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
