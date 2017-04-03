from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name="glowna"),
    url(r'^kontakt/$', views.kontakt, name="kontakt"),
]

