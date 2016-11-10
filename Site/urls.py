from django.conf.urls import url
from .views import *
from .classed_views import Index,Register
urlpatterns = [
	url(r'^$', index, name="sites-index"),
    url(r'^contacto/$',contacto, name="sites-contacto"),
    url(r'^register/$',register, name="sites-register"),
    url(r'^login/$',login, name="sites-login"),
    url(r'^profile/$',profile, name="sites-profile"),
    url(r'^logout/$',logout, name="sites-logout"),
    url(r'^index2/$',Index.as_view(), name="index2"),
    url(r'^register2/$',Register.as_view(), name="register2"),



    
]