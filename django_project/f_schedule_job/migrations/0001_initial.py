# Generated by Django 3.0.5 on 2020-04-21 03:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleJob',
            fields=[
                ('schedule_job_id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.SmallIntegerField(choices=[(1, 'active'), (0, 'archive')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'f_schedule_job',
            },
        ),
    ]
