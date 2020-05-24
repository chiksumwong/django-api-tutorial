from django.urls import path, include
from rest_framework import routers

from f_system_log import views

router = routers.DefaultRouter()
router.register(r'access', views.AccessLogViewSet)
router.register(r'audit', views.AuditLogViewSet)
router.register(r'sync', views.SyncLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
