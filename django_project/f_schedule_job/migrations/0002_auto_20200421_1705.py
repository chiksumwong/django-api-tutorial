# Generated by Django 3.0.5 on 2020-04-21 09:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('f_schedule_job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyncTableLet',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('table', models.CharField(max_length=100)),
                ('let', models.DateTimeField(blank=True)),
            ],
            options={
                'db_table': 'f_sj_sync_table_let',
            },
        ),
        migrations.CreateModel(
            name='SyncTask',
            fields=[
                ('sync_task_id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.SmallIntegerField(choices=[(0, 'archive'), (1, 'pending'), (2, 'sent')], default=1)),
                ('category', models.SmallIntegerField(choices=[(0, 'application'), (1, 'product')])),
                ('action', models.SmallIntegerField(choices=[(1, 'create'), (0, 'list'), (3, 'update'), (2, 'get')])),
                ('parameters', models.TextField(blank=True)),
                ('response', models.TextField(blank=True)),
                ('sent_at', models.DateTimeField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'f_sj_sync_task',
            },
        ),
        migrations.DeleteModel(
            name='ScheduleJob',
        ),
    ]
