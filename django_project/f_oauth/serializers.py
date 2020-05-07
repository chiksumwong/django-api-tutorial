from django.contrib.auth import get_user_model
from rest_framework import serializers
from google.oauth2 import id_token
from google.auth.transport import requests

from django_project.settings_dev_local import GOOGLE_CLIENT_ID
from f_oauth.models import SocialAccount

User = get_user_model()


class SocialLoginSerializer(serializers.Serializer):

    token = serializers.CharField(required=True)

    def verify_token(self, token):
        try:
            idinfo = id_token.verify_oauth2_token(
                token, requests.Request(), GOOGLE_CLIENT_ID)
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')
            if idinfo['aud'] not in [GOOGLE_CLIENT_ID]:
                raise ValueError('Could not verify audience.')
            # Success
            return idinfo
        except ValueError:
            pass

    def create(self, validated_data):
        id_info = self.verify_token(validated_data.get('token'))
        if id_info:
            # User not exists
            if not SocialAccount.objects.filter(unique_id=id_info['sub']).exists():
                user = User.objects.create_user(
                    username=f"{id_info['name']} {id_info['email']}",  # Username has to be unique
                    email=id_info['email']
                )
                SocialAccount.objects.create(
                    user=user,
                    unique_id=id_info['sub']
                )
                return user
            else:
                social = SocialAccount.objects.get(unique_id=id_info['sub'])
                return social.user
        else:
            raise ValueError("Incorrect Credentials")

