from django.contrib.auth import get_user_model
from rest_framework import serializers
from google.oauth2 import id_token
from google.auth.transport import requests

from django_project.settings_dev_local import GOOGLE_CLIENT_ID
from f_social_login.apis.facebook_api import verify_token, get_app_token, get_user_profile, get_long_lived_token
from f_social_login.models import SocialAccount

User = get_user_model()


class GoogleLoginSerializer(serializers.Serializer):

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
                    unique_id=id_info['sub'],
                    access_token=validated_data.get('token')
                )
                return user
            else:
                social = SocialAccount.objects.get(unique_id=id_info['sub'])
                return social.user
        else:
            raise ValueError("Incorrect Credentials")


class FacebookLoginSerializer(serializers.Serializer):

    token = serializers.CharField(required=True)

    def verify_token(self, token):
        try:
            f_dist = verify_token(token, get_app_token())
            if f_dist.get('data').get('is_valid'):
                return f_dist
        except ValueError:
            pass

    def create(self, validated_data):
        f_dist = self.verify_token(validated_data.get('token'))
        if f_dist:
            # Get Facebook User Info
            f_user = get_user_profile(validated_data.get('token'))
            if not SocialAccount.objects.filter(unique_id=f_user['id']).exists():
                user = User.objects.create_user(
                    username=f"{f_user['name']} {f_user['email']}",  # Username has to be unique
                    email=f_user['email']
                )
                l_access_token = get_long_lived_token(validated_data.get('token')).get('access_token')
                SocialAccount.objects.create(
                    provider='facebook',
                    user=user,
                    unique_id=f_user['id'],
                    access_token=l_access_token
                )
                return user
            else:
                social = SocialAccount.objects.get(unique_id=f_user['id'])
                return social.user
        else:
            raise ValueError("Incorrect Credentials")
