from django.conf.urls import url, include

urlpatterns = [
    url(r'^ulatwiaczek/', include('main.urls')),
    url(r'^', include('home.urls')),
]
