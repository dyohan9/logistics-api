import json

from django.test import RequestFactory
from django.test import TestCase
from rest_framework import status

from core.authentication.models import User
from ..account.views import LoginViewSet
from ..account.views import RegisterUserViewSet


class LoginTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.password = "abcgq!!123"
        self.email = "user@user.com"

        user = User.objects.create(email=self.email, name="User")
        user.set_password(self.password)
        user.save(update_fields=["password"])

    def request(self, data):
        request = self.factory.post("/v1/account/login/", data)
        response = LoginViewSet.as_view({"post": "create"})(request)
        response.render()
        content_data = json.loads(response.content)
        return response, content_data

    def test_okay(self):
        response, content_data = self.request(
            {"username": self.email, "password": self.password}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("token", content_data.keys())

    def test_wrong_password(self):
        response, content_data = self.request(
            {"username": self.email, "password": "wrong"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RegisterUserTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def request(self, data):
        request = self.factory.post("/v1/account/register/", data)
        response = RegisterUserViewSet.as_view({"post": "create"})(request)
        response.render()
        content_data = json.loads(response.content)
        return response, content_data

    def test_okay(self):
        email = "fake@user.com"
        password = "abc!1234"
        response, content_data = self.request(
            {"email": email, "name": "Fake", "password": password}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(email=email)
        self.assertTrue(user.check_password(password))

    def test_invalid_password(self):
        response, content_data = self.request(
            {"email": "fake@user.com", "name": "Fake", "password": "abc"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", content_data.keys())
