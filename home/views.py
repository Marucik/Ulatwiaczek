# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from main.models import Test, Sprawdzian, Przedmiot


# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def informacje(request):
    iloscPrzedmiotow = Przedmiot.objects.all().count()
    iloscTestow = Test.objects.all().count()
    return render(request, 'home/stats.html', {
        'iloscTestow': iloscTestow,
        'iloscPrzedmiotow': iloscPrzedmiotow,
    })
