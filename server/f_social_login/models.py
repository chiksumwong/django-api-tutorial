import uuid

from django.db import models

from server import settings


class SocialAccount(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    provider = models.CharField(max_length=200, default='google')
    unique_id = models.CharField(max_length=200)
    access_token = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = 'f_social_login_social_account'

    def __str__(self):
        return self.user
