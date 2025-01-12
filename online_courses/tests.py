from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from online_courses.models import Course, Lesson, Follow
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="email@example.com")
        self.course = Course.objects.create(name="The Magic of Art", owner=self.user)
        self.lesson = Lesson.objects.create(name="What is Art?", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):

        url = reverse("online_courses:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("name"), "The Magic of Art"
        )

    def test_course_create(self):

        url = reverse("online_courses:course-list")
        data = {"name": "МЭШ", "owner": self.user}
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_update(self):

        url = reverse("online_courses:course-detail", args=(self.course.pk,))
        data = {"description": "It's a kind of magic", "owner": self.user}
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("description"), "It's a kind of magic"
        )

    def test_course_delete(self):

        url = reverse("online_courses:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Course.objects.all().count(), 0
        )

    def test_course_list(self):

        url = reverse("online_courses:course-list")
        response = self.client.get(url)
        data = response.json()

        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [{'name': self.course.name,
                               'image': None,
                               'description': None,
                               'owner': self.user.pk,
                               'lessons_count': 1,
                               'lessons': [{'id': self.lesson.pk,
                                            'name': self.lesson.name,
                                            'description': None,
                                            'image': None,
                                            'video': None,
                                            'course': self.course.pk,
                                            'owner': self.user.pk}],
                               'follow': False}]}

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data, result
        )


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="email@example.com")
        self.course = Course.objects.create(name="The Magic of Art", owner=self.user)
        self.lesson = Lesson.objects.create(name="What is Art?", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):

        url = reverse("online_courses:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("name"), self.lesson.name
        )

    def test_lesson_create(self):

        url = reverse("online_courses:lesson_create")
        data = {"name": "Forms of Art", "course": self.course.pk, "owner": self.user}
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse("online_courses:lesson_update", args=(self.lesson.pk,))
        data = {"description": "There is no must in Art because it is free", "owner": self.user}
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("description"), "There is no must in Art because it is free"
        )

    def test_lesson_delete(self):
        url = reverse("online_courses:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_course_list(self):
        url = reverse("online_courses:lesson_list")
        response = self.client.get(url)
        data = response.json()

        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [{'id': self.lesson.pk,
                               'name': self.lesson.name,
                               'description': None,
                               'image': None,
                               'video': None,
                               'course': self.course.pk,
                               'owner': self.user.pk}]}

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data, result
        )


class FollowTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="email@example.com")
        self.course = Course.objects.create(name="The Magic of Art", owner=self.user)
        self.follow = Follow.objects.create(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_follow_list(self):

        url = reverse("online_courses:follow_list")
        response = self.client.get(url)
        data = response.json()

        result = [{'id': 1, 'user': 6, 'course': 7}]

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data, result
        )
