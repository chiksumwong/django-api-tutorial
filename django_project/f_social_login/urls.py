from django.urls import path

from f_social_login.views import GoogleLogin, FacebookLogin

urlpatterns = [
    path('social/google/token/obtain/', GoogleLogin.as_view()),
    path('social/facebook/token/obtain/', FacebookLogin.as_view()),
]
