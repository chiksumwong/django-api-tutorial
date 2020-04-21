from django.urls import path
from f_schedule_job import views
from f_schedule_job import views_sync

urlpatterns = [
    path('sync/add/', views.add_task),
    path('sync/seconds/', views.job_by_seconds),
    path('sync/day/', views.job_by_day),
    # Sync from Dragonce
    path('sync/d/tables/', views_sync.gettable)
]
