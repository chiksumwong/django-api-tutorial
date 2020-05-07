from django.db import models

from django_project import settings


class SocialAccount(models.Model):
    provider = models.CharField(max_length=200, default='google')
    unique_id = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
