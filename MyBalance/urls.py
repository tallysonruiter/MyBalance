from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('balanca.urls')),
   # url(r'^', include(router.urls)),
   # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
