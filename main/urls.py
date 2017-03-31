from django.conf.urls import url
from django.contrib import admin


from . import views

urlpatterns = [
    url(r'^$', views.redirect, name='index'),
    url(r'^ulatwiaczek/$', views.index, name='index'),

    url(r'^ulatwiaczek/logowanie/$', views.logowanie, name="logowanie"),
    url(r'^ulatwiaczek/wylogowanie/$', views.wylogowanie, name="wylogowanie"),

    url(r'^ulatwiaczek/test/$', views.test_lista, name='test_lista'),
    url(r'^ulatwiaczek/test/dodaj/$', views.test_dodaj, name='test_dodaj'),
    url(r'^ulatwiaczek/test/(?P<id>[0-9]+)/$', views.test_szczegoly, name='test_szczegoly'),
    url(r'^ulatwiaczek/test/(?P<id>[0-9]+)/usun/$', views.test_usun, name='test_usun'),
    url(r'^ulatwiaczek/test/(?P<id>[0-9]+)/edytuj/$', views.test_edytuj, name='test_edytuj'),

    url(r'^ulatwiaczek/sprawdzian/$', views.sprawdzian_lista, name='sprawdzian_lista'),
    url(r'^ulatwiaczek/sprawdzian/dodaj/$', views.sprawdzian_dodaj, name='sprawdzian_dodaj'),
    url(r'^ulatwiaczek/sprawdzian/(?P<id>[0-9]+)/$', views.sprawdzian_szczegoly, name='sprawdzian_szczegoly'),
    url(r'^ulatwiaczek/sprawdzian/(?P<id>[0-9]+)/usun/$', views.sprawdzian_usun, name='sprawdzian_usun'),
    url(r'^ulatwiaczek/sprawdzian/(?P<id>[0-9]+)/edytuj/$', views.sprawdzian_edytuj, name='sprawdzian_edytuj'),

    url(r'^stats/$', views.stats, name='stats'),

    url(r'^ulatwiaczek/admin/', admin.site.urls),
]
