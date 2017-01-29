from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index_logged, name='index_logged'),
    url(r'^test/dodaj/$', views.test_dodaj, name='test_dodaj'),
    url(r'^test/lista/$', views.test_lista, name='test_lista'),
    url(r'^sprawdzian/dodaj/$', views.sprawdzian_dodaj, name='sprawdzian_dodaj'),
    url(r'^sprawdzian/lista/$', views.sprawdzian_lista, name='sprawdzian_lista'),
]
