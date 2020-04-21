from django.http import HttpResponse
from f_schedule_job.api import get_application_table


def gettable():
    return HttpResponse(get_application_table())
