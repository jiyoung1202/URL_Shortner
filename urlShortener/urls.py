from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
	url(r'^api/',include('shortener.api.urls',namespace='api')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('shortener.urls')),
]
