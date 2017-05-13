# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import Textarea
from django.db.models.fields import TextField

from .models import Przedmiot, Nauczyciel, Test, Sprawdzian, Zadanie

class ZadaniaInline(admin.TabularInline):
    model = Zadanie
    fields = ['numer', 'ilosc_punktow_uczniow', 'maks_ilosc_punktow']
    extra = 5

admin.site.register(Nauczyciel)
admin.site.register(Przedmiot)
admin.site.register(Test)
@admin.register(Sprawdzian)
class SprawdzianAdd(admin.ModelAdmin):
     inlines = [ZadaniaInline]
