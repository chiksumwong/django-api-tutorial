from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

# Instantiate scheduler
scheduler = BackgroundScheduler()
# The scheduler uses the default DjangoJobStore ()
scheduler.add_jobstore(DjangoJobStore(), 'default')


# Run this job at 8:30 every day
@register_job(scheduler, 'cron', id='test', hour=8, minute=30, args=['test'])
def test(s):
    # The specific code to be executed
    pass


# Register a scheduled task and start
register_events(scheduler)
scheduler.start()
