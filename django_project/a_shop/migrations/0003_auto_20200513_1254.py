# Generated by Django 3.0.6 on 2020-05-13 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_shop', '0002_auto_20200511_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_status',
            field=models.SmallIntegerField(choices=[(1, 'active'), (0, 'inactive')], default=0),
        ),
    ]
