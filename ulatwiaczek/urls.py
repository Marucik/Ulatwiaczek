from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('home.urls')),
    url(r'^ulatwiaczek/', include('main.urls')),
    url(r'^users/', include('users.urls')),
]
