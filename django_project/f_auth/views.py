from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from f_auth.serializer import UserSerializer, GroupSerializer
from f_system_log.views import save_access_log

User = get_user_model()


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        save_access_log(request.data.get('user_name') + ' logout')
        return HttpResponse(status=200)


class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = User.objects.get(pk=request.data.get('user_id'))
        serializer = UserSerializer(user)
        save_access_log(serializer.data.get('username') + ' login')
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
