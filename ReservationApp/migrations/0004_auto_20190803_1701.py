# Generated by Django 2.2.4 on 2019-08-03 14:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationApp', '0003_auto_20190803_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablelist',
            name='bottom',
        ),
        migrations.RemoveField(
            model_name='tablelist',
            name='right',
        ),
        migrations.AlterField(
            model_name='tablelist',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 3, 14, 1, 31, 726411, tzinfo=utc)),
        ),
    ]
