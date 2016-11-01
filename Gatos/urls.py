from django.conf.urls import url
from .views import index,saluda,suma
urlpatterns = [
    url(r'^hola/', index),

    url(r'^saludo/(?P<nombre>\w+)/', saluda),
    url(r'^suma/(?P<x>[0-9]+)/(?P<y>[0-9]+)', suma),
]