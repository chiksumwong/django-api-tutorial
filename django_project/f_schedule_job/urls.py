from django.urls import path
from f_schedule_job import views

urlpatterns = [
    path('add/', views.add_task),
    path('seconds/', views.job_by_seconds),
    path('day/', views.job_by_day)
]
