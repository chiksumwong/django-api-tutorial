from django.urls import path, include

from f_auth.views import UserList, UserDetails, GroupList

urlpatterns = [
    path('auth/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('auth/users/', UserList.as_view()),
    path('auth/users/<pk>/', UserDetails.as_view()),
    path('auth/groups/', GroupList.as_view()),
]