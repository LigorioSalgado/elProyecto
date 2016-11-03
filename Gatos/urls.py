from django.conf.urls import url
from .views import index,saluda,suma

urlpatterns = [
    url(r'^hola/', index, name="gatos-index"),

    url(r'^saludo/(?P<nombre>\w+)/', saluda, name="gatos-saludo"),
    url(r'^suma/(?P<x>[0-9]+)/(?P<y>[0-9]+)', suma, name="gatos-suma"),
]