# -*- coding: utf-8 -*-
import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import FieldError
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import (Http404, HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect, JsonResponse)
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Przedmiot, Sprawdzian, Test, Uczen, Klasa, Zadanie
from main.forms import PrzedmiotAddForm, UczenAddForm, KlasaAddForm
from decimal import *


@login_required()
def index(request):
    return render(request, "main/base.html")


@login_required()
def test_dodaj(request):
    try:
        przedmioty = Przedmiot.objects.filter(autor=request.user.id).exclude(aktywny=False)
    except:
        przedmioty = False

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
                'error': True,
            })
    return render(request, 'main/test/dodaj.html', {
        'przedmioty': przedmioty,
    })


@login_required()
def test_lista(request):
    user = request.user
    testy = Test.objects.filter(autor=user).exclude(aktywny=False)

    """
    próbuje pobrać ilość wyświetlanych testów na stronę (metodą GET)
    jeśli się nie powiedzie (użytkownik wpisze np. literę)
    zostanie wyświetlona domyślna ilość czyli 10 testów na jedną stronę
    """
    try:
        getObjectsOnPage = int(request.GET.get('ilosc'))
    except:
        getObjectsOnPage = 10

    """
    próbuje pobrać typ sortowania listy (metodą GET)
    jeśli się nie powiedzie (użytkownik wpisze metodę sortowania która nie istnieje)
    lista zostanie posortowana domyślnie (czyli datą - od najnowszych testów do najstarszych)
    """

    """
    SORT_METHODS zawiera możliwości sortowania testów wraz z opisami do zwrócenia do template'
    """
    SORT_METHODS = [
        {
            'value': 'data_dodania',
            'description': 'Data dodania (rosnąco)'
        },
        {
            'value': '-data_dodania',
            'description': 'Data dodania (malejąco)'
        },
        {
            'value': 'ilosc_zadan',
            'description': 'Ilość zadań (rosnąco)'
        },
        {
            'value': '-ilosc_zadan',
            'description': 'Ilość zadań (malejąco)'
        },
        {
            'value': 'maks_ilosc_punktow',
            'description': 'Maksymalna ilość punktów (rosnąco)'
        },
        {
            'value': '-maks_ilosc_punktow',
            'description': 'Maksymalna ilość punktów (malejąco)'
        },
        {
            'value': 'temat',
            'description': 'Temat (rosnąco)'},
        {
            'value': '-temat',
            'description': 'Temat (malejąco)'},
        {
            'value': 'data_edytowania',
            'description': 'Data edytowania (rosnąco)'
        },
        {
            'value': '-data_edytowania',
            'description': 'Data edytowania (malejąco)'
        },
    ]

    def isMethodAvailable(list, method):
        for i in list:
            if i['value'] == method:
                return True
        return False
    try:
        getSortMethod = request.GET.get('sortowanie')
        if not isMethodAvailable(SORT_METHODS, getSortMethod):
            raise
        testy = testy.order_by(getSortMethod)
    except:
        testy = testy.order_by('data_dodania')

    """
    próbuje pobrać która strona ma być aktualnie wyświetlana (metodą GET)
    jeśli się nie powiedzie, do zmiennej przypisywana jest pierwsza strona
    """
    try:
        getPage = int(request.GET.get('strona'))
    except:
        getPage = 1

    # tworzy paginację listy testów
    paginator = Paginator(testy, getObjectsOnPage)

    try:
        tests = paginator.page(getPage)
    except EmptyPage:
        tests = paginator.page(paginator.num_pages)
    except:
        tests = paginator.page(1)

    return render(request, 'main/test/index.html', {
        'testy': tests,
        'iloscTestow': len(testy),
        'sortingMethods': SORT_METHODS,
    })


@login_required()
def test_szczegoly(request, id):
    try:
        test = Test.objects.filter(autor=request.user).get(pk=id)
    except Test.DoesNotExist:
        raise Http404
    return render(request, "main/test/szczegoly.html", {
        "test": test
    })


@login_required()
def test_usun(request, id):
    isDeleted = True
    try:
        test = Test.objects.filter(autor=request.user).get(pk=id)
    except Test.DoesNotExist:
        # raise Http404
        isDeleted = False
        return JsonResponse({
            "deleted": deleted,
        })

    try:
        test.aktywny = False
        test.save()
    except:
        isDeleted = False
    return JsonResponse({
        "deleted": isDeleted,
        "temat": test.temat
    })


@login_required()
def test_edytuj(request, id):
    # return HttpResponse("<h1> Edytowanko testu numerek %s </h1>" % id)
    try:
        test = Test.objects.filter(autor=request.user).get(pk=id)
    except Test.DoesNotExist:
        raise Http404


@login_required()
def sprawdzian_dodaj(request):
    try:
        test_id = int(request.POST.get('test_id'))
    except:
        return redirect('main:test_lista')
    try:
        klasa_id = int(request.POST.get('klasa_id'))
    except:
        klasy = Klasa.objects.filter(autor=request.user.id)
        return render(request, 'main/sprawdzian/dodaj.html', {
            'klasy': klasy,
            'test_id': test_id,
        })
    try:
        klasa = Klasa.objects.filter(autor=request.user.id).get(pk=klasa_id)
        test = Test.objects.filter(autor=request.user.id).get(pk=test_id)
    except:
        raise Http404

    new_sprawdzian = Sprawdzian()
    new_sprawdzian.test = test
    new_sprawdzian.autor = request.user
    new_sprawdzian.klasa = klasa
    new_sprawdzian.ilosc_uczniow = Uczen.objects.filter(autor=request.user).filter(klasa=klasa_id).count()
    new_sprawdzian.data_sprawdzianu = datetime.date.today()
    new_sprawdzian.save()

    return render(request, 'main/sprawdzian/dodaj.html', {
        'test': test,
        'klasa': klasa,
    })


@login_required()
def sprawdzian_lista(request):
    sprawdziany = Sprawdzian.objects.filter(autor=request.user.id)
    return render(request, 'main/sprawdzian/index.html', {
        'sprawdziany': sprawdziany,
    })


@login_required()
def sprawdzian_szczegoly(request, id):
    try:
        sprawdzian = Sprawdzian.objects.get(pk=id)
    except:
        raise Http404

    uczniowie_w_klasie = Uczen.objects.filter(autor=request.user).filter(klasa=sprawdzian.klasa).order_by('nazwisko')
    sumy_punktow = []
    for i in range(0, uczniowie_w_klasie.count()):
        zadania = Zadanie.objects.filter(autor=request.user).filter(sprawdzian=sprawdzian).filter(uczen=uczniowie_w_klasie[i])
        punkty = []
        context = {}
        context['user'] = uczniowie_w_klasie[i]
        for zadanie in zadania:
            punkty.append(zadanie.punkty)
        suma_punktow = sum(punkty)
        context['punkty'] = suma_punktow
        try:
            procentowy_wynik = int((suma_punktow / sprawdzian.test.maks_ilosc_punktow) * 100)
        except:
            procentowy_wynik = 0
        context['procenty'] = procentowy_wynik
        sumy_punktow.append(context)
    srednia_punktow_tab = []
    srednia_procentow_tab = []
    for suma in sumy_punktow:
        srednia_punktow_tab.append(suma['punkty'])
        srednia_procentow_tab.append(suma['procenty'])
    srednia_punktow = float(sum(srednia_punktow_tab) / uczniowie_w_klasie.count())
    srednia_procentow = float(sum(srednia_procentow_tab) / uczniowie_w_klasie.count())
    if srednia_procentow <= 19:
        latwosc = 'Bardzo trudny'
    elif srednia_procentow <= 49:
        latwosc = 'Trudny'
    elif srednia_procentow <= 69:
        latwosc = 'Umiarkowanie trudny'
    elif srednia_procentow <= 89:
        latwosc = 'Łatwy'
    else:
        latwosc = 'Bardzo łatwy'

    return render(request, "main/sprawdzian/szczegoly.html", {
        "sprawdzian": sprawdzian,
        "uczniowie": uczniowie_w_klasie,
        "sumy_punktow": sumy_punktow,
        "srednia_punktow": round(srednia_punktow, 2),
        "srednia_procentow": round(srednia_procentow, 2),
        "latwosc": latwosc,
    })


@login_required()
def sprawdzian_uczen(request, id, uczen_id):
    try:
        sprawdzian = Sprawdzian.objects.filter(autor=request.user).get(pk=id)
        uczen = Uczen.objects.filter(autor=request.user).get(pk=uczen_id)
        zadania = Zadanie.objects.filter(autor=request.user).filter(sprawdzian=sprawdzian).filter(uczen=uczen)
    except:
        raise Http404
    punkty = []
    for zadanie in zadania:
        punkty.append(zadanie.punkty)
    suma_punktow = sum(punkty)
    punkty_testu = sprawdzian.test.maks_ilosc_punktow
    procentowy_wynik = int((suma_punktow / punkty_testu) * 100)
    return render(request, 'main/sprawdzian/uczen.html', {
        'sprawdzian': sprawdzian,
        'zadania': zadania,
        'uczen': uczen,
        'suma_punktow': suma_punktow,
        'procentowy_wynik': procentowy_wynik,
    })


@login_required()
def sprawdzian_uczen_edytuj(request, id, uczen_id):
    try:
        sprawdzian = Sprawdzian.objects.filter(autor=request.user).get(pk=id)
    except:
        raise Http404
    try:
        uczen = Uczen.objects.filter(autor=request.user).get(pk=uczen_id)
    except:
        raise Http404
    if request.method == 'POST':
        ilosc_zadan = sprawdzian.test.ilosc_zadan
        for i in range(0, int(ilosc_zadan)):
            context = {}
            punkty_za_zadanie = request.POST.get('zad' + str(i + 1))
            punkty_za_zadanie = float('0' + str(punkty_za_zadanie))
            try:
                zadanie = Zadanie.objects.filter(autor=request.user).filter(sprawdzian=sprawdzian).filter(uczen=uczen).get(numer=i + 1)
            except:
                zadanie = Zadanie()
                zadanie.autor = request.user
                zadanie.sprawdzian = sprawdzian
                zadanie.uczen = uczen
                zadanie.numer = i + 1
            zadanie.punkty = punkty_za_zadanie
            zadanie.save()
    return render(request, 'main/sprawdzian/uczen_edytuj.html', {
        'sprawdzian': sprawdzian,
        'uczen': uczen,
        'ilosc_zadan': range(sprawdzian.test.ilosc_zadan),
    })


@login_required()
def sprawdzian_usun(request, id):
    return HttpResponse("<h1> Usuwanko sprawdzianu numerek %s </h1>" % id)


@login_required()
def sprawdzian_edytuj(request, id):
    return HttpResponse("<h1> Edytowanko sprawdzianku numerek %s </h1>" % id)


@login_required()
def przedmiot_lista(request):
    try:
        przedmioty = Przedmiot.objects.filter(autor=request.user).exclude(aktywny=False)
    except:
        przedmioty = False
    return render(request, 'main/przedmiot/index.html', {
        'przedmioty': przedmioty,
    })


@login_required()
def przedmiot_dodaj(request):
    if request.method == 'POST':
        form = PrzedmiotAddForm(request.POST)
        if form.is_valid():
            form.autor = request.user
            form.save()
            return redirect('main:przedmiot_lista')
        else:
            return render(request, 'main/przedmiot/dodaj.html', {
                'add_test_form': form,
                'add_test_error': True,
            })
    else:
        form = PrzedmiotAddForm()
    return render(request, 'main/przedmiot/dodaj.html', {
        'add_test_form': form,
    })


@login_required()
def klasa_lista(request):
    try:
        klasy = Klasa.objects.filter(autor=request.user)
    except:
        klasy = False
    return render(request, 'main/klasa/index.html', {
        'klasy': klasy,
    })


@login_required()
def klasa_dodaj(request):
    if request.method == 'POST':
        form = KlasaAddForm(request.POST)
        if form.is_valid():
            form.autor = request.user
            form.save()
        else:
            return render(request, 'main/klasa/dodaj.html', {
                'add_klasa_form': form,
                'add_klasa_error': True
            })
    else:
        form = KlasaAddForm()
    return render(request, 'main/klasa/dodaj.html', {
        'add_klasa_form': form
    })


@login_required()
def klasa_uczniowie(request, klasa_id):
    try:
        klasa = get_object_or_404(Klasa, pk=klasa_id)
    except:
        raise 404

    try:
        uczniowie_w_klasie = Uczen.objects.filter(autor=request.user).filter(klasa=klasa_id)
    except:
        uczniowie_w_klasie = False

    return render(request, 'main/klasa/szczegoly.html', {
        'uczniowie': uczniowie_w_klasie,
        'klasa': klasa
    })


@login_required()
def uczen_lista(request):
    try:
        uczniowie = Uczen.objects.filter(autor=request.user)
    except:
        uczniowie = False
    return render(request, 'main/uczen/index.html', {
        'uczniowie': uczniowie,
    })


@login_required()
def uczen_dodaj(request):
    if request.method == 'POST':
        form = UczenAddForm(request.POST)
        if form.is_valid():
            form.autor = request.user
            form.klasa = Klasa.objects.get(pk=int(request.POST.get("klasa_id")))
            form.save()
        else:
            return render(request, 'main/klasa/dodaj.html', {
                'add_uczen_form': form,
                'add_uczen_error': True
            })
    form = UczenAddForm()
    try:
        klasy = Klasa.objects.filter(autor=request.user)
    except Klasa.DoesNotExist:
        klasy = False
    return render(request, 'main/uczen/dodaj.html', {
        'add_uczen_form': form,
        'klasy': klasy,
    })


def testowanko(request):
    return JsonResponse({
        "deleted": True,
    })
