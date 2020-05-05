from django.urls import path

from f_oauth.views_google import GoogleView, HelloView

urlpatterns = [
    path('oauth/hello/', HelloView.as_view(), name='hello'),
    path('oauth/google/', GoogleView.as_view()),
]
