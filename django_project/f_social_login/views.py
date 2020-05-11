from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from f_social_login.serializers import GoogleLoginSerializer, FacebookLoginSerializer

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class GoogleLogin(TokenObtainPairView):
    permission_classes = [AllowAny]  # AllowAny for login

    def post(self, request):
        serializer = GoogleLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(get_tokens_for_user(user))
        else:
            raise ValueError('Not serializable')


class FacebookLogin(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = FacebookLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(get_tokens_for_user(user))
        else:
            raise ValueError('Not serializable')
