from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from f_schedule_job.serializer import ScheduleJobSerializer


scheduler = BackgroundScheduler()   # Instantiate scheduler
scheduler.add_jobstore(DjangoJobStore(), 'default')   # The scheduler uses the default DjangoJobStore ()


@register_job(scheduler, "interval", seconds=60*60, id='job_by_seconds')  # interval way each 15 mines
def job_by_seconds():
    print("I'm a sync job!")


@register_job(scheduler, 'cron', hour=00, minute=00, second=00, id='job_by_day')   # Run this job at 8:30 every day
def job_by_day():
    print("I'm a day job!")


# API (set job - date time)
@api_view(['POST'])
def add_task(request):
    if request.method == 'POST':
        serializer = ScheduleJobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Register a scheduled task and start
register_events(scheduler)  # per-execution monitoring
scheduler.start()
