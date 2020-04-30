from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from f_system_log.models import AuditLog, AccessLog, SyncLog
from f_system_log.serializers import AccessLogSerializer, AuditLogSerializer, SyncLogSerializer


class AccessLogViewSet(viewsets.ModelViewSet):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer
    permission_classes = [IsAdminUser]


class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [IsAdminUser]


class SyncLogViewSet(viewsets.ModelViewSet):
    queryset = SyncLog.objects.all()
    serializer_class = SyncLogSerializer
    permission_classes = [IsAdminUser]
