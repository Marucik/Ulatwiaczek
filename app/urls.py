from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('main.urls2')),
    url(r'^ulatwiaczek/', include('main.urls')),
]
