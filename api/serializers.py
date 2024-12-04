from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import PasswordResetConfirmSerializer as BasePasswordResetConfirmSerializer
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


class CustomPasswordResetConfirmSerializer(BasePasswordResetConfirmSerializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField()
    re_new_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        new_password = attrs.get('new_password')
        re_new_password = attrs.pop('re_new_password', None)

        # Check if the new passwords match
        if new_password != re_new_password:
            raise serializers.ValidationError(
                {"new_password": "The new password and re-entered password do not match."}
            )

        # Call the parent class validate method
        attrs = super().validate(attrs)

        # Ensure 'new_password' is in attrs
        attrs['new_password'] = new_password

        return attrs