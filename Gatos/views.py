from django.shortcuts import render
from django.http import HttpResponse



def index(request):

	return HttpResponse("Hola Soy un Gato")


def saluda(request,nombre):

	return HttpResponse("Hola "+nombre+" Soy un gato y me llamo Filomeno")
# Create your views here.

def suma (request,x,y):
	parte1 = int(x)
	parte2 = int(y)

	suma = parte1 +parte2

	return HttpResponse(suma)





	