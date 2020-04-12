from rest_framework import generics
from rest_framework import permissions
# Model
from django.contrib.auth.models import User
from tutorial4.models import SnippetAuth
# Serializer
from tutorial4.serializers import UserSerializer
from tutorial1.serializers import SnippetSerializer
# Permission (customization)
from tutorial4.permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):  # only list all user record
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):  # only get one user record
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = SnippetAuth.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Associating Snippets with Users
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SnippetAuth.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
