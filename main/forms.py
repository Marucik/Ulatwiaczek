# -*- coding: utf-8 -*-
from main.models import Przedmiot
from django import forms


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

