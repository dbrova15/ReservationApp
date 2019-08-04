# Generated by Django 2.2.4 on 2019-08-03 14:51

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationApp', '0010_auto_20190803_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablelist',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 3, 14, 51, 10, 752976, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tablelist',
            name='position_x',
            field=models.IntegerField(default=0, help_text='Position x. Origin in the upper left corner, %', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='tablelist',
            name='position_y',
            field=models.IntegerField(default=0, help_text='Position y. Origin in the upper left corner, %', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
