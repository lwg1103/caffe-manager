from django.shortcuts import render, redirect
from django.http import HttpRequest
from reservations.models import Reservation
from reservations.forms import ReservationForm


def home_page(request: HttpRequest):
    return render(request, 'home.html')


def reservations(request: HttpRequest):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
    else:
        form = ReservationForm()
    variables = {'reservations': __fetch_all_reservations(), 'form': form}
    return render(request, 'list.html', variables)


def show_reservation(request: HttpRequest, id):
    variables = {'reservation': Reservation.objects.get(id=id)}
    return render(request, 'reservation.html', variables)


def new_reservation(request: HttpRequest):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            __save_new_reservation(form.cleaned_data)
            return redirect('reservations')
        else:
            return reservations(request)


def delete_reservation(request: HttpRequest, id):
    Reservation.objects.get(id=id).delete()
    return redirect('reservations')


def __fetch_all_reservations():
    return Reservation.objects.all()


def __save_new_reservation(form_cleaned_data):
    reservation = Reservation()
    reservation.name = form_cleaned_data['name']
    reservation.date = form_cleaned_data['date']
    reservation.table = form_cleaned_data['table']
    reservation.telephone = form_cleaned_data['telephone']
    reservation.save()


