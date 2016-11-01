from django.conf.urls import url
from .views import index, contacto
urlpatterns = [
	url(r'^$', index),
    url(r'^contacto/$',contacto),

    
]