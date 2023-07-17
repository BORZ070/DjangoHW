from django.shortcuts import render
from mainpageHW.models import Car

def start_views(request):
    cars = Car.objects.all()
    return render(request, 'indexHW.html', {'cars': cars})
