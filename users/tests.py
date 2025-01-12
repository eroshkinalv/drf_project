import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from online_courses.models import Course
from users.models import User, Payment


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="email@example.com", password="123zaq")
        self.client.force_authenticate(user=self.user)

    def test_user_retrieve(self):
        url = reverse("users:user_retrieve", args=(self.user.pk,))
        response = self.client.get(url)
        data = response.json()

        print(data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("email"), self.user.email
        )

        self.assertEqual(
            data.get("password"), self.user.password
        )

    def test_user_create(self):

        url = reverse("users:register")
        data = {"email": "new_user@example.com", "password": "123zaq"}
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

        self.assertEqual(
            User.objects.all().count(), 2)

    def test_user_update(self):
        url = reverse("users:user_update", args=(self.user.pk,))
        data = {"payment_amount": 1500}
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("payment_amount"), 1500
        )

    def test_user_delete(self):
        url = reverse("users:user_delete", args=(self.user.pk,))
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            User.objects.all().count(), 0)

    def test_user_list(self):
        url = reverse("users:user_list")
        response = self.client.get(url)
        data = response.json()

        result = [{'id': self.user.pk,
                   'email': self.user.email,
                   'password': self.user.password,
                   'phone': None,
                   'image': None,
                   'city': None,
                   'followed_items': []}]

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data, result
        )


class PaymentTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="email@example.com")
        self.course = Course.objects.create(name="The Magic of Art", owner=self.user)
        self.payment = Payment.objects.create(user=self.user, course=self.course, payment_amount=1000, payment_method="Наличные")
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse("users:payment-detail", args=(self.payment.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("user"), self.payment.user.pk
        )

    def test_payment_create(self):

        url = reverse("users:payment-list")
        data = {"user": self.user.pk, "date": "2025-02-02", "course": self.course.pk, "payment_amount": 2000, "payment_method": "Наличные"}
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

        self.assertEqual(
            Payment.objects.all().count(), 2
        )

    def test_payment_update(self):

        url = reverse("users:payment-detail", args=(self.payment.pk,))
        data = {"payment_amount": 1999}
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("payment_amount"), 1999
        )

    def test_payment_delete(self):

        url = reverse("users:payment-detail", args=(self.payment.pk,))
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Payment.objects.all().count(), 0
        )

    # def test_payment_list(self):
    #
    #     url = reverse("users:payment-list")
    #     response = self.client.get(url)
    #     data = response.json()
    #
    #     print(data)
    #
    #     result = [{'id': self.payment.pk,
    #                'date': self.payment.date,
    #                'payment_amount': self.payment.payment_amount,
    #                'payment_method': self.payment.payment_method,
    #                'user': self.payment.user.pk,
    #                'course': self.payment.course.pk,
    #                'lesson': None}]
    #
    #     self.assertEqual(
    #         response.status_code, status.HTTP_200_OK
    #     )
    #
    #     self.assertEqual(
    #         data, result
    #     )
