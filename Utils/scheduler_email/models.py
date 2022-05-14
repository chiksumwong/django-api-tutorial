import uuid

from django.db import models


class EmailTask(models.Model):

    class Status(models.IntegerChoices):
        PENDING = 0
        SENDING = 1
        COMPLETED = 2
        FAIL = 3
        SKIP = 4

    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    status = models.IntegerField(choices=Status.choices, default=Status.PENDING)
    params = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    count = models.SmallIntegerField(default=0)
    start_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'email_task'
        ordering = ['-created_at']
        verbose_name_plural = 'Email Task'

    def __str__(self):
        return str(self.id)


class EmailCheckExpiredTime(models.Model):
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'email_check_expired_time'
        verbose_name_plural = 'Email Check Expired Time'
