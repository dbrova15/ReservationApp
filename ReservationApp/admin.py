from django.contrib import admin

# Register your models here.
from ReservationApp.models import *

admin.site.register(TableList)
admin.site.register(Booking)
