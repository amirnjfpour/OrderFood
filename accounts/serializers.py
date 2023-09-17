from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator
from rest_framework import serializers

from accounts.models import BaseUser


class AddUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = BaseUser
        fields = ("email", "password")

    def validate(self, attrs):
        email_validator = EmailValidator()
        email = attrs.get('email')
        if email:
            email_validator(email)
        password = attrs.get('password')
        if password:
            validate_password(password)
        return attrs


class RegisterSerializer(AddUserSerializer):

    def create(self, validated_data):
        user_obj = self.Meta.model.objects.create_user(**self.validated_data)
        return user_obj


class AddAdminSerializer(AddUserSerializer):

    def create(self, validated_data):
        admin_obj = self.Meta.model.objects.create_admin(**self.validated_data)
        return admin_obj
