from rest_framework import viewsets

from f_system_log.models import SystemLog
from f_system_log.serializers import SystemLogSerializer


class SystemLogViewSet(viewsets.ModelViewSet):
    queryset = SystemLog.objects.all()
    serializer_class = SystemLogSerializer
