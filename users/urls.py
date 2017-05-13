from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'login/$', views.login_user, name="login"),
    url(r'register/$', views.register_user, name="register"),
    url(r'logout/$', views.logout_user, name="logout")
]
