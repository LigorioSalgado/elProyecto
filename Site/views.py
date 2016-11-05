from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from .functions import authenticated
from django.contrib.auth import logout as lg
# Create your views here.

def  index(request):
	batch = "Batch 12"
	cinta = "<p>Negra</p>"
	lista = ["cuchufleto", "gertrudis","garfield", "peje", "filomeno", "casimiro"]
	datos = {"name":"fido", "raza": "labrador", "edad": "4"}
	return render(request, 'index.html',{
		"variable":batch, 
		"cinta":cinta, "lista":lista,
		"datos" : datos,
		})

def  contacto(request):
	return render(request,'contacto.html')


def register(request):

	if request.method == "POST":

		form = RegisterForm(request.POST)

		if form.is_valid():

			User.objects.create_user(
				first_name=form.cleaned_data["first_name"],
				last_name=form.cleaned_data["last_name"],
				username=form.cleaned_data["username"],
				password=form.cleaned_data["password"],
				email=form.cleaned_data["email"])

			return redirect("sites-index")

	else:

		form = RegisterForm()

		return render(request,"register.html",{"form":form})


def login(request):

	if request.method == "POST":

		form = LoginForm(request.POST)

		if form.is_valid():

			auth = authenticated(
				request,
				form.cleaned_data["username"],
				form.cleaned_data["password"]
				)

			log = 'sites-index' if auth else 'sites-login'

			return redirect(log)
	else:

		form = LoginForm()

		return render(request,"login.html",{"form":form})


def profile(request):

	if request.user.is_authenticated():

		user = User.objects.get(id=request.user.id)

		return render(request,"profile.html",{"user":user})


	else:
		return redirect('sites-login')


def logout(request):

	lg(request)
	return redirect('sites-index')



