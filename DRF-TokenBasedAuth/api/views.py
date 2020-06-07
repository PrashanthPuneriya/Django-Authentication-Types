from rest_framework.response import Response
from rest_framework import (
    views,
    generics,
    status,
)
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.models import MyUser
from rest_framework.authtoken.models import Token
from .serializers import MyUserSerializer

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404


class RegisterAPI(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = MyUserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        username = request.data.get("username")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        password = request.data.get("password")
        user = MyUser.objects.create_user(email, username, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        #Generating a token for new users
        token = Token.objects.create(user=user) #Token and MyUser has a OneToOne relation
        return Response({'detail': 'User has been created with token: ' + token.key}, status=status.HTTP_200_OK)


class LoginAPI(views.APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        # username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(email=email, password=password)
        # user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'detail': token.key}, status=status.HTTP_200_OK)

class ChangePassword(views.APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        # user = get_object_or_404(MyUser, email=request.user)
        user = request.user
        user.set_password(request.POST.get('new_password'))
        user.save()
        return Response({'detail': 'Password has been changed successfully'}, status=status.HTTP_200_OK)

class TestAPI(views.APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        data = {'sample_data': 123}
        return Response(data, status=status.HTTP_200_OK)
