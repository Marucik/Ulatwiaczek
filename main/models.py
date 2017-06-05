from django.db import models
from django.contrib.auth.models import User
from datetime import date



class Przedmiot(models.Model):
    nazwa = models.CharField(max_length=50)
    skrot = models.CharField(max_length=10)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    aktywny = models.BooleanField(default=True)

    class Meta:
        db_table = 'Przedmiot'
        verbose_name_plural = 'Przedmioty'

    def __str__(self):
        return self.nazwa


class Nauczyciel(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)

    class Meta:
        db_table = 'Nauczyciel'
        verbose_name_plural = 'Nauczyciele'

    def __str__(self):
        return self.imie + ' ' + self.nazwisko


class Test(models.Model):
    przedmiot = models.ForeignKey(Przedmiot, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    ilosc_zadan = models.IntegerField()
    maks_ilosc_punktow = models.IntegerField()
    temat = models.CharField(max_length=50)
    data_dodania = models.DateField(default=date.today)
    data_edytowania = models.DateField(default=date.today)
    aktywny = models.BooleanField(default=True)

    class Meta:
        db_table = 'Test'
        verbose_name_plural = 'Testy'

    def __str__(self):
        return self.temat


class Klasa(models.Model):
    nazwa = models.CharField(max_length=50)
    skrot = models.CharField(max_length=10)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Klasa'
        verbose_name_plural = 'Klasy'


class Uczen(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    klasa = models.ForeignKey(Klasa, on_delete=models.CASCADE, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Uczen'
        verbose_name_plural = 'Uczniowie'


class Sprawdzian(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    klasa = models.ForeignKey(Klasa, on_delete=models.CASCADE, null=False, default=False)
    ilosc_uczniow = models.IntegerField()
    data_sprawdzianu = models.DateField()
    data_dodania = models.DateField(default=date.today)
    data_edytowania = models.DateField(default=date.today)
    aktywny = models.BooleanField(default=True)

    class Meta:
        db_table = 'Sprawdzian'
        verbose_name_plural = 'Sprawdziany'

    def __str__(self):
        return str(self.test) + ' przez ' + str(self.autor)


class Zadanie(models.Model):
    sprawdzian = models.ForeignKey(Sprawdzian, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    uczen = models.ForeignKey(Uczen, on_delete=models.CASCADE, default=False)
    numer = models.IntegerField()
    #punkty = models.DecimalField(max_digits=5, decimal_places=2)
    punkty = models.FloatField()

    class Meta:
        db_table = 'Zadanie'
        verbose_name_plural = 'Zadania'

    def __str__(self):
        return str(self.sprawdzian) + ' zadanie numer ' + str(self.numer) + ' punktow ' + str(self.punkty)
