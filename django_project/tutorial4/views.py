from rest_framework import generics

from django.contrib.auth.models import User

from tutorial4.serializers import UserSerializer


class UserList(generics.ListAPIView):  # only list all user record
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):  # only get one user record
    queryset = User.objects.all()
    serializer_class = UserSerializer
