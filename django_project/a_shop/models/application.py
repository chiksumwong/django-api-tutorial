import uuid

from django.db import models


class Application(models.Model):
    status = {
        (0, 'archive'),
        (1, 'pending'),
        (2, 'approved'),
        (3, 'rejected'),
        (4, 'sent email')
    }
    application_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=100)
    status = models.SmallIntegerField(choices=status, default=1)

    class Meta:
        db_table = 'a_application'

    def __str__(self):
        return self.customer_name
