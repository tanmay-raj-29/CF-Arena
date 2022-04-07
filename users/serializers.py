from rest_framework import serializers
from django.contrib.auth import get_user_model

from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

#Models
from .models import User

# User serializer
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        required=True, allow_blank=False, max_length=68, min_length=6, write_only=True
    )
    token = serializers.CharField(max_length=65, min_length=6, read_only=True)

    class Meta:
        model = User
        fields = ["email","username", "password", "token"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        password = attrs.get("password", "")
        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        
        return {"email": user.email, "token": user.token}
