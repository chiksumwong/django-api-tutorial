# Schedule Job

## Package of "Schedule Job"
- Schedule (Lib)
- APScheduler (Lib)
- Sched (Python's module)
- Celery

## APScheduler (Advanced Python Scheduler) - Best Chose
1. Triggers
2. Job Stores
3. Executors
4. Schedulers


## APScheduler in Django
```python
$ pip install django-apscheduler
```

## Two Way to create "Task"
- the decorator way is suit to programmer which create the task
- if it is able to allow user to create the specify task, using the 
- For Example, use decorator way to sync the record every 5 mins
- use the function way to add the "Get All" operation to schedule
### Decorator
@register_job(scheduler, 'cron', id='test', hour=8, minute=30，args=['test'])
function way
### Function
add_job