# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import FieldError

# Create your views here.
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
        return render(request, 'users/login.html')

def rejestracja(request):
    return render(request, 'users/register.html')

def wylogowanie(request):
    logout(request)
    return render(request, 'users/logout.html')
