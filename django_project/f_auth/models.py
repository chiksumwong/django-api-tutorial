import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):   # auth_user
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    first_name = None
    last_name = None

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.username
