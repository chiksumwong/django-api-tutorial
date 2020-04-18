from django.urls import path, include
from rest_framework.routers import DefaultRouter
from f_system_log import views

router = DefaultRouter()
router.register(r'log', views.SystemLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
