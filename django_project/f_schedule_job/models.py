import uuid

from django.db import models


# class ScheduleJob(models.Model):
#     status = {
#         (0, 'archive'),
#         (1, 'active')
#     }
#     system_log_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
#     log = models.CharField(max_length=100)
#     message = models.TextField()
#     status = models.SmallIntegerField(choices=status, default=1)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'f_schedule_job'
#
#     def __str__(self):
#         return self.log
