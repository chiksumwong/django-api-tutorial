from django.urls import path
from f_schedule_job import views_job

urlpatterns = [
    path('sync/add/', views_job.add_task),
    path('sync/seconds/', views_job.job_by_seconds),
    path('sync/day/', views_job.job_by_day),
]
