from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'logowanie/$', views.logowanie, name="logowanie"),
    url(r'rejestracja/$', views.rejestracja, name="rejestracja"),
    url(r'wylogowanie/$', views.wylogowanie, name="wylogowanie")
]
