# Generated by Django 2.2.4 on 2019-08-03 14:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationApp', '0004_auto_20190803_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablelist',
            name='left',
        ),
        migrations.RemoveField(
            model_name='tablelist',
            name='top',
        ),
        migrations.AddField(
            model_name='tablelist',
            name='position_x',
            field=models.IntegerField(default=0, help_text='Position x. Origin in the upper left corner'),
        ),
        migrations.AddField(
            model_name='tablelist',
            name='position_y',
            field=models.IntegerField(default=0, help_text='Position y. Origin in the upper left corner'),
        ),
        migrations.AlterField(
            model_name='tablelist',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 3, 14, 4, 36, 120207, tzinfo=utc)),
        ),
    ]