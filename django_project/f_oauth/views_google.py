import json

import requests
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from google.oauth2 import id_token
from google.auth.transport import requests

from django.contrib.auth import get_user_model

from django_project.settings_dev_local import GOOGLE_CLIENT_ID

User = get_user_model()


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class GoogleView(APIView):
    def post(self, request):
        token = request.data.get("token")  # validate the token
        try:
            # Specify the CLIENT_ID of the app that accesses the backend:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')

            # ID token is valid. Get the user's Google Account ID from the decoded token.
            user_id = idinfo['sub']
            email = idinfo['email']

            # Create User if user is not exist

            # if User exist, do login action

            response = {'user_id': user_id, 'email': email}
            return Response(response)

        except ValueError:
            # Invalid token
            pass
