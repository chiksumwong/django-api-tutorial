from django.urls import path

from scheduler_email import views

urlpatterns = [
    # For Testing
    path('test_add_email_task/', views.test_add_confirm_email_task),
    path('test_run_send_email_task/', views.test_run_send_email_task),
]