from rest_framework import serializers

from f_system_log.models import SystemLog


class SystemLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemLog
        fields = '__all__'
