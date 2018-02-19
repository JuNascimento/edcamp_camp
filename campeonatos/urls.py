from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista_campeonatos, name='lista_campeonatos'),
    url(r'^campeonato/(?P<pk>[0-9]+)/$', views.campeonato_detalhe, name='campeonato_detalhe'),
    # url(r'^edicoes$', views.lista_edicoes, name='lista_edicoes'),
    # url(r'^campeonato-brasileiro-serie-a$', views.campeonato_brasileiro_serie_a, name='campeonato-brasileiro-serie-a'),
]