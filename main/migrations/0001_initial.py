# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-14 15:30
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Klasa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('skrot', models.CharField(max_length=10)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Klasy',
                'db_table': 'Klasa',
            },
        ),
        migrations.CreateModel(
            name='Nauczyciel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Nauczyciele',
                'db_table': 'Nauczyciel',
            },
        ),
        migrations.CreateModel(
            name='Przedmiot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('skrot', models.CharField(max_length=10)),
                ('aktywny', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Przedmioty',
                'db_table': 'Przedmiot',
            },
        ),
        migrations.CreateModel(
            name='Sprawdzian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilosc_uczniow', models.IntegerField()),
                ('data_sprawdzianu', models.DateField()),
                ('data_dodania', models.DateField(default=datetime.date.today)),
                ('data_edytowania', models.DateField(default=datetime.date.today)),
                ('aktywny', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('klasa', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='main.Klasa')),
            ],
            options={
                'verbose_name_plural': 'Sprawdziany',
                'db_table': 'Sprawdzian',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilosc_zadan', models.IntegerField()),
                ('maks_ilosc_punktow', models.IntegerField()),
                ('temat', models.CharField(max_length=50)),
                ('data_dodania', models.DateField(default=datetime.date.today)),
                ('data_edytowania', models.DateField(default=datetime.date.today)),
                ('aktywny', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('przedmiot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Przedmiot')),
            ],
            options={
                'verbose_name_plural': 'Testy',
                'db_table': 'Test',
            },
        ),
        migrations.CreateModel(
            name='Uczen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('klasa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Klasa')),
            ],
            options={
                'verbose_name_plural': 'Uczniowie',
                'db_table': 'Uczen',
            },
        ),
        migrations.CreateModel(
            name='Zadanie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numer', models.IntegerField()),
                ('punkty', models.FloatField()),
                ('autor', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sprawdzian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Sprawdzian')),
                ('uczen', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='main.Uczen')),
            ],
            options={
                'verbose_name_plural': 'Zadania',
                'db_table': 'Zadanie',
            },
        ),
        migrations.AddField(
            model_name='sprawdzian',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Test'),
        ),
    ]
