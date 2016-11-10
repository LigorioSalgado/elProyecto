from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^hola/', index, name="gatos-index"),

    url(r'^saludo/(?P<nombre>\w+)/', saluda, name="gatos-saludo"),
    url(r'^suma/(?P<x>[0-9]+)/(?P<y>[0-9]+)', suma, name="gatos-suma"),
    url(r'^nuevo/', nuevo , name="gatos-nuevo"),
    url(r'^comida/', comida , name="gatos-comida"),
    url(r'^listado/', GatoListView.as_view(), name="lista-gatos"),
    url(r'^detalle/(?P<pk>[0-9]+)/', GatoDetailView.as_view(), name="detalle-gatos"),
    url(r'^about/', GatoTemplateView.as_view(), name="about-gatos"),
    url(r'^delete/(?P<pk>[0-9]+)/', GatoDeleteView.as_view(), name="delete-gatos"),
    url(r'^create/', GatoCreateView.as_view(), name="create-gatos"),
    url(r'^update/(?P<pk>[0-9]+)/', GatoUpdateView.as_view(), name="update-gatos")
]