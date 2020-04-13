import json
from django.http import JsonResponse
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')


# Interface with the front end
def test_add_task(request):
    if request.method == 'POST':
        content = json.loads(request.body.decode())  # Receive parameters
        try:
            start_time = content['start_time']  # User input task start time, '10:00:00'
            start_time = start_time.split(':')
            hour = int(start_time)[0]
            minute = int(start_time)[1]
            second = int(start_time)[2]
            s = content['s']  # Receive various parameters for performing tasks
            # Create task
            scheduler.add_job(test, 'cron', hour=hour, minute=minute, second=second, args=[s])
            code = '200'
            message = 'success'
        except Exception as e:
            code = '400'
            message = e

        back = {
            'code': code,
            'message': message
        }
        return JsonResponse(json.dumps(back, ensure_ascii=False), safe=False)


# The specific code to be executed
def test(s):
    print(s)
    pass


register_events(scheduler)
scheduler.start()
