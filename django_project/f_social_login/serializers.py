from django.contrib.auth import get_user_model
from rest_framework import serializers
from google.oauth2 import id_token
from google.auth.transport import requests

from django_project.settings_dev_local import GOOGLE_CLIENT_ID
from f_social_login.apis.facebook_api import verify_token, get_app_token, get_user_profile, get_long_lived_token
from f_social_login.apis.microsoft_api import get_user_info
from f_social_login.models import SocialAccount

User = get_user_model()


class GoogleLoginSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)

    def verify_token(self, token):
        try:
            g_dict = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
            print("Google Verify: ", g_dict)
            if g_dict['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')
            if g_dict['aud'] not in [GOOGLE_CLIENT_ID]:
                raise ValueError('Could not verify audience.')
            # Success
            return g_dict
        except ValueError:
            pass

    def create(self, validated_data):
        g_user = self.verify_token(validated_data.get('token'))
        if g_user:
            # User not exists
            if not SocialAccount.objects.filter(unique_id=g_user['sub']).exists():
                user = User.objects.create_user(
                    username=f"{g_user['name']} {g_user['email']}",  # Username has to be unique
                    email=g_user['email']
                )
                SocialAccount.objects.create(
                    user=user,
                    unique_id=g_user['sub'],
                    access_token=validated_data.get('access_token')
                )
                return user
            else:
                social = SocialAccount.objects.get(unique_id=g_user['sub'])
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


class MicrosoftLoginSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)

    def create(self, validated_data):
        # Get Facebook User Info
        m_user = get_user_info(validated_data.get('token'))
        if not SocialAccount.objects.filter(unique_id=m_user['id']).exists():
            user = User.objects.create_user(
                username=f"{m_user['displayName']} {m_user['userPrincipalName']}",  # Username has to be unique
                email=m_user['userPrincipalName']
            )
            SocialAccount.objects.create(
                provider='microsoft',
                user=user,
                unique_id=m_user['id'],
                access_token=validated_data.get('token')
            )
            return user
        else:
            social = SocialAccount.objects.get(unique_id=m_user['id'])
            return social.user
