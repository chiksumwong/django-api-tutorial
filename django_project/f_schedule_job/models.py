import uuid

from django.db import models


class SyncTask(models.Model):
    status = {
        (0, 'archive'),
        (1, 'pending'),
        (2, 'sent')
    }
    category = {
        (0, 'application'),
        (1, 'product')
    }
    action = {
        (0, 'list'),
        (1, 'create'),
        (2, 'get'),
        (3, 'update')
    }
    sync_task_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    status = models.SmallIntegerField(choices=status, default=1)
    category = models.SmallIntegerField(choices=category)
    action = models.SmallIntegerField(choices=action)
    parameters = models.TextField(blank=True)
    response = models.TextField(blank=True)
    sent_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'f_sj_sync_task'

    def __str__(self):
        return self.category


class SyncTableLet (models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    table = models.CharField(max_length=100)
    let = models.DateTimeField(blank=True)

    class Meta:
        db_table = 'f_sj_sync_table_let'

    def __str__(self):
        return self.table
