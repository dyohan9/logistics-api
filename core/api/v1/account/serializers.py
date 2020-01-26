from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer

from core.authentication.models import User
from ..fields import PasswordField


class LoginSerializer(AuthTokenSerializer, serializers.ModelSerializer):
    username = serializers.EmailField(label=_("Email"))
    password = PasswordField(label=_("Password"))

    class Meta:
        model = User
        fields = ["username", "password"]
        ref_name = None


class RegisterUserSerializer(serializers.ModelSerializer):
    password = PasswordField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ["email", "name", "password"]
        ref_name = None

    @staticmethod
    def validate_password(value):
        return make_password(value)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "locale"]
        ref_name = None
