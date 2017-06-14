# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from main.models import Test, Sprawdzian, Przedmiot, Nauczyciel, Klasa, Uczen, Sprawdzian, Zadanie


# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def informacje(request):
    iloscPrzedmiotow = Przedmiot.objects.all().count()
    iloscTestow = Test.objects.all().count()
    iloscNauczycieli = Nauczyciel.objects.all().count()
    iloscKlas = Klasa.objects.all().count()
    iloscUczniow = Uczen.objects.all().count()
    iloscSprawdzianow = Sprawdzian.objects.all().count()
    iloscZadan = Zadanie.objects.all().count()
    return render(request, 'home/stats.html', {
        'iloscTestow': iloscTestow,
        'iloscPrzedmiotow': iloscPrzedmiotow,
        'iloscNauczycieli': iloscNauczycieli,
        'iloscKlas': iloscKlas,
        'iloscUczniow': iloscUczniow,
        'iloscSprawdzianow': iloscSprawdzianow,
        'iloscZadan': iloscZadan,
    })
