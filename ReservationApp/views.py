# import Markup as Markup
import datetime

from django.shortcuts import render, redirect
from ReservationApp.forms import DateForm, BookingForm
from ReservationApp.models import TableList, Booking
from django.conf import settings
from django.core.mail import send_mail

width_hall = 600
height_hall = 300


def get_data_list(list_tables, data_time_req):
    data_list = []
    for data in list_tables:
        namber_table = data.namber_of_table
        namber_of_seats = data.namber_of_seats
        width_circle = width_hall / 100 * data.width_table
        height_circle = height_hall / 100 * data.height_table
        left = width_hall / 100 * data.position_x
        top = height_hall / 100 * data.position_y
        circle_type = data.circle_type
        booking_obj = Booking.objects.filter(namber_table=namber_table, date_time=data_time_req).first()

        if booking_obj is None or booking_obj.status == 0:
            color = "green"
            href_status = """/set_status/n_table={namber_table}&status={status}&date_time={data_time_req}&email_client={email}""".format(
                namber_table=namber_table, status=1,
                data_time_req=str(data_time_req), email="Null")
        elif booking_obj.status == 1:
            color = 'darkorange'
            href_status = """/set_status/n_table={namber_table}&status={status}&date_time={data_time_req}&email_client={email}""".format(
                namber_table=namber_table, status=0,
                data_time_req=str(data_time_req), email="Null")
        else:
            color = "red"
            href_status = """/"""

        if circle_type:
            table = """
            <a href="{href_status}">
            <div id="oval " style="width:{width_circle}px;
                height:{height_circle}px; background-color:{color};
                 -moz-border-radius:50px;-webkit-border-radius:50px;
                 border-radius:50px; position: absolute; 
                 left:{left}; top:{top};">
                 
                 <div style="position: relative; 
                 left:25%; top:20%; width: 70px; color: white;">
                 <p>№ {namber_table}
                 <br>мест {namber_of_seats}
                 </p>
                 </div>
                 
                </div></a>""".format(width_circle=width_circle, height_circle=height_circle,
                                     left=left, top=top,
                                     namber_table=namber_table, namber_of_seats=namber_of_seats, color=color,
                                     href_status=href_status)
        else:
            table = """
            <a href="{href_status}">
                <div id="rectangle " style="width:{width_circle}px;
                    height:{height_circle}px; background-color:{color};
                     position: absolute; 
                     left:{left}; top:{top};">
                     
                     <div style="position: relative; 
                     left:25%; top:20%; width: 70px; color: white;">
                     <p>
                        № {namber_table}<br>
                        мест {namber_of_seats}
                        </p>
                     </div>
                    </div></a>""".format(width_circle=width_circle, height_circle=height_circle,
                                         left=left, top=top,
                                         namber_table=namber_table, namber_of_seats=namber_of_seats, color=color,
                                         href_status=href_status)

        data_list.append(table)
    return data_list


def hall_layout(request, data_time_req=datetime.date.today()):
    form_booking = None
    if type(data_time_req) is str:
        data_time_req = datetime.datetime.strptime(data_time_req, '%Y-%m-%d').date()
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            data_time_req = form.cleaned_data['data_time_req']

    form = DateForm(initial={"data_time_req": data_time_req})

    before_date = data_time_req - datetime.timedelta(days=1)
    after_date = data_time_req + datetime.timedelta(days=1)
    booking_status_list = [i.status for i in Booking.objects.filter(date_time=data_time_req).all()]
    if 1 in booking_status_list:
        if request.method == 'POST':
            form_booking = BookingForm(request.POST)
            if form_booking.is_valid():
                email_client = form_booking.cleaned_data['email_fild']
                list_tables = TableList.objects.all()
                for data in list_tables:
                    n_table = data.namber_of_table
                    booking_obj = Booking.objects.filter(namber_table=n_table, date_time=data_time_req).first()
                    if not booking_obj:
                        continue
                    status = booking_obj.status
                    if status == 1:
                        booking_obj.status = 2
                        booking_obj.email_client = email_client
                        booking_obj.save()

                        subject = 'Заказ столика'
                        message = 'Вы заказали столик № {}.'.format(n_table)
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = [email_client, ]

                        send_mail(subject, message, email_from, recipient_list)

        form_booking = BookingForm()
    list_tables = TableList.objects.all()

    data_list = get_data_list(list_tables, data_time_req)

    return render(request, 'Reservation/hall.html',
                  {"width_hall": width_hall, 'form': form, "form_booking": form_booking, "height_hall": height_hall,
                   'data_list': data_list, "before_date": before_date.strftime('%Y-%m-%d'),
                   "after_date": after_date.strftime('%Y-%m-%d')})


def set_status_table(request, n_table, status, date_time, email_client):
    date_time_obj = datetime.datetime.strptime(date_time, '%Y-%m-%d')
    obj_booking = Booking.objects.filter(namber_table=n_table, date_time=date_time_obj).first()
    if not obj_booking:
        if email_client == "Null":
            data = Booking(namber_table=n_table, status=status, email_client=None, date_time=date_time)
        else:
            data = Booking(namber_table=n_table, status=status, email_client=email_client, date_time=date_time)
        data.save()
    else:
        obj_booking.status = status
        obj_booking.save()
    return redirect("/date/{}".format(date_time))
