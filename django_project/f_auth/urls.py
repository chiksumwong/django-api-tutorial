from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from f_auth import views


urlpatterns = [
    # Auth
    path('auth/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),  # oAuth
    # JWT
    path('auth/token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # JWT
    # View Data
    path('auth/users/', views.UserList.as_view()),
    path('auth/users/<pk>/', views.UserDetails.as_view()),
    path('auth/groups/', views.GroupList.as_view()),
    # Function
    path('auth/login/', views.Login.as_view()),
    path('auth/logout/', views.Logout.as_view())
]
