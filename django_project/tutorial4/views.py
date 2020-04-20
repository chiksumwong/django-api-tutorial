from rest_framework import generics
# Model
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from tutorial4.models import SnippetAuth
# Serializer
from tutorial4.serializers import UserSerializer
from tutorial4.serializers import SnippetSerializer
# Permission (customization)
from tutorial4.permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):  # only list all user record
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserDetail(generics.RetrieveAPIView):  # only get one user record
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class SnippetList(generics.ListCreateAPIView):
    queryset = SnippetAuth.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Associating Snippets with Users
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SnippetAuth.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
