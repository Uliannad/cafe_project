from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
def home(request):
    #return HttpResponse("Привіт, мій преший view!")
    return render (request, "home.html")
# Create your views here.

# Список активних столиків
def tables_list(request):
    tables = Table.objects.filter(is_active=True)
    context = {"tables": tables}
    return render(request,"tables_list.html",context)

def table_detail(request, table_id):
    table = get_object_or_404(Table, id=table_id)

    return render(
        request,
        "table_detail.html",
        {"table": table}
    )

def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)

    # усі бронювання цього клієнта
    bookings = Booking.objects.filter(client=client)

    return render(
        request,
        "client_detail.html",
        {
            "client": client,
            "bookings": bookings
        }
    )

def bookings_by_date(request):
    date = request.GET.get("date")
    bookings = None

    if date:
        bookings = Booking.objects.filter(date=date)

    return render(
        request,
        "bookings_by_date.html",
        {
            "bookings": bookings,
            "date": date
        }
    )

def client_list(request):
    clients = Client.objects.all()
    return render(
        request,
        "client_list.html",
        {"clients": clients}
    )


def table_bookings(request, table_id):
    table = get_object_or_404(Table, id=table_id)
    bookings = Booking.objects.filter(table=table)

    return render(
        request,
        "table_bookings.html",
        {
            "table": table,
            "bookings": bookings
        }
    )
