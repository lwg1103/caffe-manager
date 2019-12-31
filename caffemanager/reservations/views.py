from django.shortcuts import render, redirect
from django.http import HttpRequest
from reservations.models import Reservation


def home_page(request: HttpRequest):

    variables = {'reservations': __fetch_all_reservations()}

    if request.method == 'POST':
        __save_new_reservation(request.POST['reservation_name'])
        return redirect('/')

    return render(request, 'home.html', variables)

def __fetch_all_reservations():
    return Reservation.objects.all()

def __save_new_reservation(reservation_name):
    reservation = Reservation()
    reservation.name = reservation_name
    reservation.save()

