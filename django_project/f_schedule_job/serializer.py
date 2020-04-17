from apscheduler.schedulers.background import BackgroundScheduler
from rest_framework import serializers

from f_schedule_job.models import ScheduleJob

scheduler = BackgroundScheduler()


# The specific code to be executed
def job_by_custom(s):
    print(s)


class ScheduleJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleJob
        fields = '__all__'

    def create(self, validated_data):
        start_time = validated_data.get('start_time')  # User input task start time, '10:00:00'
        start_time = start_time.split(':')
        hour = int(start_time)[0]
        minute = int(start_time)[1]
        second = int(start_time)[2]
        s = 'nice'  # Receive various parameters for performing tasks
        # Create task
        scheduler.add_job(job_by_custom, 'cron', hour=hour, minute=minute, second=second, args=[s])
