# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1> Witam na stronie głównej</h1><a href="">Logowanko</a>')
def kontakt(request):
    return HttpResponse('kontakt here')
