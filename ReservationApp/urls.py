from django.urls import path

from ReservationApp import views

urlpatterns = [
    path('', views.hall_layout, name='hall_layout'),
    path(
        'set_status/n_table=<int:n_table>&status=<int:status>&date_time=<str:date_time>&email_client=<str:email_client>',
        views.set_status_table,
        name='set_status')
]
