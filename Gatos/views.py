from django.views.generic import TemplateView, ListView, DetailView, DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Gato, Comida
from .forms import GatoForm,ComidaForm

class GatoTemplateView(TemplateView):
	template_name = "about.html"

class GatoListView(ListView):
	model = Gato
	context_object_name = "gatos"

class GatoDetailView(DetailView):
	model = Gato

class GatoDeleteView(DeleteView):
	model = Gato
	success_url = "/gatos/listado/"

class GatoUpdateView(UpdateView):
	model = Gato
	fields = ["name", "age"]
	success_url = "/gatos/listado/"

class GatoCreateView(CreateView):
	model = Gato
	fields = ["name","age","callejero", "sexo", "comida"]
	success_url = "/gatos/listado/"

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

		form = GatoForm(request.POST)

		if form.is_valid():

			gato = Gato(name=form.cleaned_data["name"],age=form.cleaned_data["age"])
			gato.name = form.cleaned_data["name"]
			gato.age = form.cleaned_data["age"]
			gato.sexo = form.cleaned_data["sexo"]
			gato.callejero = form.cleaned_data["callejero"]
			gato.comida = form.cleaned_data["comida"]

			gato.save()
	

			return redirect('gatos-index')
		return redirect('sites-index')



	else:
		form = GatoForm()

		return render(request,'nuevo_gato.html',{"form":form})


def comida(request):

	if request.method == "POST":
		comida = ComidaForm(request.POST)

		if comida.is_valid():

			comida.save()

		return redirect('gatos-index')
	else:

		form = ComidaForm()
		return render(request,'nueva_comida.html',{"form":form})




	