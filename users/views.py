# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import (Http404, HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect, JsonResponse)
from django.shortcuts import get_object_or_404, redirect, render

from users.forms import RegisterForm


def user_login(request):
    if request.user.is_authenticated:
        return redirect('main:test_lista')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('main:index')
        else:
            return render(request, 'users/login.html', {
                'loginError': True,
            })
    return render(request, 'users/login.html')


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main:index')
        else:
            return render(request, 'users/register.html', {
                'register_form': form,
                'register_error': True,
            })
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {
        'register_form': form,
    })


def user_logout(request):
    """Wylogowanie użytkownika"""
    logout(request)
    return redirect(reverse('users:login'))
