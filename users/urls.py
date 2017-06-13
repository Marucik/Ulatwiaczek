from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'zaloguj/$', views.user_login, name="login"),
    url(r'wyloguj/$', views.user_logout, name="logout"),
    url(r'zarejestruj/$', views.user_register, name="register"),
]
