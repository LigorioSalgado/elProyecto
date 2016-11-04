from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Gato, Comida

def index(request):

	gatos = Gato.objects.all().order_by("-name")
	cachorros = gatos.filter(age__lte = 5)
	comidas = Comida.objects.filter(caducidad__range=("2016-11-01", "2016-12-31")).first()

	return render(request, "gatos.html",{"gatos":gatos, "comidas":comidas, "cachorros":cachorros})


def saluda(request,nombre):

	return HttpResponse("Hola "+nombre+" Soy un gato y me llamo Filomeno")
# Create your views here.

def suma (request,x,y):
	parte1 = int(x)
	parte2 = int(y)

	suma = parte1 + parte2

	return HttpResponse(suma)


def nuevo(request):


	if request.method == "POST":

		gato = Gatos()

		gato.name = request.POST["name"]
		gato.age = request.POST["age"]
		gato.sexo = request.POST["sexo"]
	

		return redirect('gatos-index')


	else:
		comida = Comida.objects.all()

		return render(request,'nuevo_gato.html',{comida:comida})



	