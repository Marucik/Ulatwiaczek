from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'logowanie/$', views.login_user, name="login"),
    url(r'logout/$', views.wyloguj, name="wyloguj"),
    url(r'rejestracja/$', views.register_user, name="register"),
]
