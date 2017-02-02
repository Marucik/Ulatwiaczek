# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from main.models import Test, Nauczyciel, Przedmiot, Sprawdzian
from django.db import models
from faker import Factory
import random
import datetime
class Command(BaseCommand):
    help = 'Seeding a database with fake data'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='+', type=int)

    def handle(self, *args, **options):
    	number = options['count'][0]
    	fake = Factory.create('pl_PL')
       	for i in range(number):
    		nauczyciel = Nauczyciel(None, fake.first_name().encode('ascii','ignore'), fake.last_name().encode('ascii','ignore'))
    		nauczyciel.save()

    		nazwaPrzedmiotu = fake.job().encode('ascii','ignore')
    		przedmiot = Przedmiot(None, nazwaPrzedmiotu, nazwaPrzedmiotu[0:3])
    		przedmiot.save()
        
        	test = Test(None, random.randint(1, Przedmiot.objects.all().count()), random.randint(5, 15), random.randint(20, 40),fake.sentence(nb_words=6, variable_nb_words=True) ,datetime.date.today(), datetime.date.today(), True)
        	test.save()