from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from djoser.email import PasswordResetEmail
from .serializers import CustomPasswordResetSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomPasswordResetView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomPasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email']
        )
        context = {'user': user}
        to = [user.email]
        PasswordResetEmail(self.request, context).send(to)
        return Response(status=status.HTTP_204_NO_CONTENT)
