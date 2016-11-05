from django.conf.urls import url
from .views import *
urlpatterns = [
	url(r'^$', index, name="sites-index"),
    url(r'^contacto/$',contacto, name="sites-contacto"),
    url(r'^register/$',register, name="sites-register"),
    url(r'^login/$',login, name="sites-login"),
    url(r'^profile/$',profile, name="sites-profile"),
    url(r'^logout/$',logout, name="sites-logout"),

    
]