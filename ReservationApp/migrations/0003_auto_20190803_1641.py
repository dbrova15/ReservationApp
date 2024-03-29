# Generated by Django 2.2.4 on 2019-08-03 13:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationApp', '0002_auto_20190803_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablelist',
            name='status',
            field=models.IntegerField(default=0, help_text='Enter status of table. 0 - free, 1 - there is a reservation request, 2 - booked'),
        ),
        migrations.AlterField(
            model_name='tablelist',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 3, 13, 41, 51, 894792, tzinfo=utc)),
        ),
    ]
