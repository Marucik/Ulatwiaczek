# -*- coding: utf-8 -*-
from django import forms

from main.models import Klasa, Przedmiot, Uczen


class PrzedmiotAddForm(forms.Form):
    nazwa = forms.CharField(
        max_length=50,
        help_text="Nazwa przedmiotu",
    )
    skrot = forms.CharField(
        max_length=10,
        help_text="Skrót",
    )
    autor = None

    class Meta:
        model = Przedmiot
        fields = ("nazwa", "skrot", )

    def save(self):
        new_przedmiot = Przedmiot()
        new_przedmiot.nazwa = self.cleaned_data["nazwa"]
        new_przedmiot.skrot = self.cleaned_data["skrot"]
        new_przedmiot.aktywny = True
        new_przedmiot.autor = self.autor
        new_przedmiot.save()


class KlasaAddForm(forms.Form):
    nazwa = forms.CharField(
        max_length=50,
        help_text="Nazwa klasy np. Technik Informatyk"
    )
    skrot = forms.CharField(
        max_length=10,
        help_text="Skrót np. 2BI"
    )
    autor = None

    class Meta:
        model = Klasa
        fields = ("nazwa", "skrot", )

    def save(self):
        klasa = Klasa()
        klasa.nazwa = self.cleaned_data["nazwa"]
        klasa.skrot = self.cleaned_data["skrot"]
        klasa.autor = self.autor
        klasa.save()


class UczenAddForm(forms.Form):
    imie = forms.CharField(
        max_length=50,
        help_text="Imie ucznia"
    )
    nazwisko = forms.CharField(
        max_length=50,
        help_text="Nazwisko ucznia"
    )
    autor = None
    klasa = None

    class Meta:
        model = Uczen
        fields = ("imie", "nazwisko", )

    def save(self):
        uczen = Uczen()
        uczen.imie = self.cleaned_data["imie"]
        uczen.nazwisko = self.cleaned_data["nazwisko"]
        uczen.autor = self.autor
        uczen.klasa = self.klasa
        uczen.save()
