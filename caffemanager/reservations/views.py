from django.shortcuts import render, redirect
from django.http import HttpRequest
from reservations.models import Reservation


def home_page(request: HttpRequest):
    return render(request, 'home.html')


def reservations(request: HttpRequest):

    variables = {'reservations': __fetch_all_reservations()}

    return render(request, 'reservations.html', variables)


def new_reservation(request: HttpRequest):
    if request.method == 'POST':
        __save_new_reservation(request.POST['reservation_name'])

    return redirect('reservations')


def delete_reservation(request: HttpRequest, id):
    Reservation.objects.get(id=id).delete()
    return redirect('reservations')


def __fetch_all_reservations():
    return Reservation.objects.all()


def __save_new_reservation(reservation_name):
    reservation = Reservation()
    reservation.name = reservation_name
    reservation.save()


