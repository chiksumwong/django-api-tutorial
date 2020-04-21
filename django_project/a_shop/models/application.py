import uuid

from django.db import models


class Application(models.Model):
    status = {
        (0, 'archive'),
        (1, 'wait to sync'),
        (2, 'wait to review'),
        (3, 'approved'),
        (4, 'rejected')
    }
    email_status = {
        (0, 'not send email'),
        (1, 'sent email')
    }
    application_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=100)
    status = models.SmallIntegerField(choices=status, default=1)
    email_status = models.SmallIntegerField(choices=email_status, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'a_application'

    def __str__(self):
        return self.customer_name
