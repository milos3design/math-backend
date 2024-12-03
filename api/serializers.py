from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User

User = get_user_model()

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class CustomPasswordResetSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')

        # Check if the username and email match an existing user
        if not User.objects.filter(username=username, email=email).exists():
            raise serializers.ValidationError(
                "No active account found with the given username and email."
            )
        return attrs

    def get_user(self):
        # Retrieve the user matching the username and email
        validated_data = self.validated_data
        return User.objects.get(username=validated_data['username'], email=validated_data['email'])
