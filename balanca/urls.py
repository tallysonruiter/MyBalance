from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from balanca import views

urlpatterns = [
    
    url(r'^pessoa/$', views.pessoa_list.as_view()),
    url(r'^pessoa/(?P<pk>[0-9]+)/$', views.PessoaDetail.as_view()),
    url(r'^peso/$', views.peso_list.as_view()),
    url(r'^peso/(?P<pk>[0-9]+)/$', views.PesoDetail.as_view()),
    

]

urlpatterns = format_suffix_patterns(urlpatterns)


