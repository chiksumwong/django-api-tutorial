from django.urls import path, include
from rest_framework.routers import DefaultRouter

from f_file.views import FileUploadViewSet

router = DefaultRouter()
router.register(r'file', FileUploadViewSet)

urlpatterns = [
    path('', include(router.urls))
]
