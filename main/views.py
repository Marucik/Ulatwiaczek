# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from main.models import Test, Sprawdzian


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
    return HttpResponse("<h1>Dodawanie testu</h1>")

@login_required(login_url='/ulatwiaczek/logowanie/')
def test_lista(request):
    testy = Test.objects.all()
    return render(request, 'test/index.html',  {
        'testy': testy,
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
