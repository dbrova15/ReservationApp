# Generated by Django 2.2.4 on 2019-08-03 15:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationApp', '0013_auto_20190803_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 3, 15, 7, 33, 695287, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tablelist',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 3, 15, 7, 33, 695287, tzinfo=utc)),
        ),
    ]
