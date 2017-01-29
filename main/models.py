from django.db import models

# heh3szki
class Przedmiot(models.Model):
	nazwa = models.CharField(max_length = 50)
	skrot = models.CharField(max_length = 10)
	class Meta:
		db_table = 'Przedmiot'
	def __str__(self):
		return self.nazwa
class Nauczyciel(models.Model):
	imie = models.CharField(max_length = 50)
	nazwisko = models.CharField(max_length = 50)
	class Meta:
		db_table = 'Nauczyciel'
	def __str__(self):
		return self.imie + ' ' + self.nazwisko
class Test(models.Model):
	przedmiot = models.ForeignKey(Przedmiot, on_delete = models.CASCADE)
	ilosc_zadan = models.IntegerField()
	maks_ilosc_punktow = models.IntegerField()
	temat = models.CharField(max_length = 50)
	data_dodania = models.DateField()
	active = models.BooleanField()
	class Meta:
		db_table = 'Test'
	def __str__(self):
		return self.temat
class Sprawdzian(models.Model):
	test = models.ForeignKey(Test, on_delete = models.CASCADE)
	nauczyciel = models.ForeignKey(Nauczyciel, on_delete = models.CASCADE)
	ilosc_uczniow = models.IntegerField()
	data_sprawdzianu = models.DateField()
	class Meta:
		db_table = 'Sprawdzian'
	def __str__(self):
		return str(self.test) + ' przez ' + str(self.nauczyciel)
class Zadanie(models.Model):
	sprawdzian = models.ForeignKey(Sprawdzian, on_delete = models.CASCADE)
	numer = models.IntegerField()
	ilosc_punktow_uczniow = models.DecimalField(max_digits = 5, decimal_places = 2)
	maks_ilosc_punktow = models.IntegerField()
	class Meta:
		db_table = 'Zadanie'
	def __str__(self):
		return str(self.sprawdzian) + ' zadanie numer ' + str(self.numer)
