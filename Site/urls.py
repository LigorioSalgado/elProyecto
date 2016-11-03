from django.conf.urls import url
from .views import index, contacto
urlpatterns = [
	url(r'^$', index, name="sites-index"),
    url(r'^contacto/$',contacto, name="sites-contacto"),

    
]