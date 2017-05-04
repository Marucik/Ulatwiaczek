from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('home.urls', namespace="home")),
    url(r'^ulatwiaczek/', include('main.urls', namespace="main")),
    url(r'^konto/', include('users.urls', namespace="users")),
    url(r'^admin/', admin.site.urls),
]
