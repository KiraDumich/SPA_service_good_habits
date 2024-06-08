from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserSerializer, CreateUserSerializer


class UserRegisterView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class UserRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
