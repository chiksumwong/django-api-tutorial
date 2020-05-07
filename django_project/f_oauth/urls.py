from django.urls import path

from f_oauth.views_google import GoogleLogin

urlpatterns = [
    path('oauth/token/obtain/', GoogleLogin.as_view()),
]
