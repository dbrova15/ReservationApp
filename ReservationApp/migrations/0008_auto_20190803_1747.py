# Generated by Django 2.2.4 on 2019-08-03 14:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationApp', '0007_auto_20190803_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablelist',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 3, 14, 47, 28, 794483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tablelist',
            name='email_client',
            field=models.EmailField(default='', help_text='Customer Email for Booking Notification', max_length=254, null=True, unique=True),
        ),
    ]
