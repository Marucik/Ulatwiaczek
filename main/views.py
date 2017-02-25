# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from main.models import Test, Sprawdzian, Przedmiot
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime


def index(request):
    return render(request, "base.html")

def logowanie(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('test_lista')
        else:
            return HttpResponse("Nie znaleziono lub nieprawidłowe dane")
    else: 
        return render(request, 'login.html')

def wylogowanie(request):
    logout(request)
    return redirect('logowanie')

@login_required(login_url='/ulatwiaczek/logowanie/')
def index_logged(request):
    return HttpResponse("<h1>Hello, world. Only 4 logged users. Super Secret.</h1>")

@login_required(login_url='/ulatwiaczek/logowanie/')
def test_dodaj(request):
    przedmioty = Przedmiot.objects.all()
    if request.method == 'POST':
        przedmiot = request.POST['idPrzedmiotu']
        autor = request.user.id
        ilosc_zadan = request.POST['ilosc_zadan']
        maks_ilosc_punktow = request.POST['maks_ilosc_punktow']
        temat = str(request.POST['temat'])
        data_dodania = datetime.date.today()
        data_edytowania = datetime.date.today()
        aktywny = True
        nowyTest = Test(None, przedmiot, autor, ilosc_zadan, maks_ilosc_punktow, temat, data_dodania, data_edytowania, aktywny)
        try:
            nowyTest.save()
        except:
            return render(request, 'test/dodaj.html', {
                'przedmioty': przedmioty,
                'error':True,
            })
    return render(request, 'test/dodaj.html', {
        'przedmioty': przedmioty,
    })

@login_required(login_url='/ulatwiaczek/logowanie/')
def test_lista(request):
    user = request.user
    testy = Test.objects.filter(autor=user)
    getPage = request.GET.get('strona')

    if(request.GET.get('ilosc')):
        getObjectsOnPage = request.GET.get('ilosc')
    else:
        getObjectsOnPage = 10
    paginator = Paginator(testy, getObjectsOnPage)
    
    try: 
        tests = paginator.page(getPage)
    except PageNotAnInteger:
        tests = paginator.page(1)
    except EmptyPage:
        tests = paginator.page(paginator.num_pages)
    return render(request, 'test/index.html', {
        'testy': tests,
        'iloscTestow': len(testy),
        
    })

@login_required(login_url='/ulatwiaczek/logowanie/')
def test_szczegoly(request, id):
    test = get_object_or_404(Test, pk=id)
    return render(request, "test/szczegoly.html", {
        "test":test
    })

@login_required(login_url='/ulatwiaczek/logowanie/')
def test_usun(request, id):
    return HttpResponse("<h1> Usuwanko testu numerek %s </h1>" % id)

@login_required(login_url='/ulatwiaczek/logowanie/')
def test_edytuj(request, id):
    return HttpResponse("<h1> Edytowanko testu numerek %s </h1>" % id)

@login_required(login_url='/ulatwiaczek/logowanie/')
def sprawdzian_dodaj(request):
    return HttpResponse("<h1>Dodawanie sprawdzianu</h1>")

@login_required(login_url='/ulatwiaczek/logowanie/')
def sprawdzian_lista(request):
    return HttpResponse("<h1>Lista sprawdzianów</h1>")

@login_required(login_url='/ulatwiaczek/logowanie/')
def sprawdzian_szczegoly(request, id):
    sprawdzian = get_object_or_404(Sprawdzian, pk=id)
    return render(request, "sprawdzian/szczegoly.html", {
        "sprawdzian" : sprawdzian,
    })

@login_required(login_url='/ulatwiaczek/logowanie/')
def sprawdzian_usun(request, id):
    return HttpResponse("<h1> Usuwanko sprawdzianu numerek %s </h1>" % id)

@login_required(login_url='/ulatwiaczek/logowanie/')
def sprawdzian_edytuj(request, id):
    return HttpResponse("<h1> Edytowanko sprawdzianku numerek %s </h1>" % id)
