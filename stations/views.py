from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from csv import DictReader




def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    bus_station = []

    with open('data-398-2018-08-30.csv', newline='', encoding="utf-8") as data:
        reader = DictReader(data)
        for row in reader:
            bus_station.append(row)

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_station, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
