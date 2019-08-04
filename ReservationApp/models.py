from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

from django.db import models

# Create your models here.


class TableList(models.Model):
    namber_of_table = models.IntegerField(null=False, default=None)
    namber_of_seats = models.IntegerField(help_text="Enter namber of seats", default=4)
    circle_type = models.BooleanField(default=True,)
    width_table = models.IntegerField(default=20, help_text="Table width, %", validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    height_table = models.IntegerField(default=40, help_text="Table height, %", validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    position_x = models.IntegerField(help_text="Position x. Origin in the upper left corner, %", default=0, validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    position_y = models.IntegerField(help_text="Position y. Origin in the upper left corner, %", default=0, validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    date_time = models.DateField(blank=True, default=timezone.now(), help_text="")

    def __str__(self):
        if self.circle_type:
            type_table = "Oval"
        else:
            type_table = "Rectangle "
        return "id:{} Seats:{} Type:{}".format(self.namber_of_table, self.namber_of_seats, type_table)


class Booking(models.Model):
    namber_table = models.IntegerField(help_text="Enter namber of seats", default=None)
    status = models.IntegerField(
        help_text="Enter status of table. 0 - free, 1 select table, 3 - booked", default=0)
    email_client = models.EmailField(help_text="Customer Email for Booking Notification", null=True, unique=True,
                                     blank=True, default="test")
    date_time = models.DateField(blank=True, help_text="")