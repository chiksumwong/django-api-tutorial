# Generated by Django 3.0.5 on 2020-04-21 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f_system_log', '0002_auto_20200421_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemlog',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'archive'), (1, 'active')], default=1),
        ),
    ]