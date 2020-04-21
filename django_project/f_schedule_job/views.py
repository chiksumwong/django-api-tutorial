import json
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from f_schedule_job.models import SyncTask
from f_schedule_job.serializer import ScheduleJobSerializer

from f_schedule_job.api import create_application_record

scheduler = BackgroundScheduler()   # Instantiate scheduler
scheduler.add_jobstore(DjangoJobStore(), 'default')   # The scheduler uses the default DjangoJobStore ()


@register_job(scheduler, "interval", seconds=60*1, id='job_by_seconds')  # interval way each 15 mines
def job_by_seconds():
    print("I'm a sync job!")
    sjs = SyncTask.objects.filter(status=1)
    for i in sjs:
        if i.category == 0:  # application
            if i.action == 1:  # create
                d = json.loads(i.parameters)  # get parameters
                create_application_record(d['application_id'], d['customer'], d['timestamp'])
        elif i.category == 1:
            print(i.action)

        # update status, and sent time
        i.status = 2
        i.sent_at = datetime.now()
        i.save()


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
