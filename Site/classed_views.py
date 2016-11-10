from django.shortcuts import render,redirect
from django.views.generic import View	
from .forms import RegisterForm
from django.contrib.auth.models import User

class Index(View):
	template = "index.html"

	def get(self,request,*args,**kargs):
		batch = "Batch 12 Este es otro view"
		cinta = "<p>Negra</p>"
		lista = ["cuchufleto", "gertrudis","garfield", "peje", "filomeno", "casimiro"]
		datos = {"name":"fido", "raza": "labrador", "edad": "4"}

		return render(request,self.template, {
			"variable":batch,"cinta":cinta, "lista":lista,
			"datos" : datos,})



class Register(View):
	form = RegisterForm()
	template = "register.html"
	
	def get(self,request,*args,**kargs):
		return render(request,self.template,{"form":self.form})
	
	def post(self,request,*args,**kargs):

		self.form = RegisterForm(request.POST)

		if self.form.is_valid():

			User.objects.create_user(
				first_name=self.form.cleaned_data["first_name"],
				last_name=self.form.cleaned_data["last_name"],
				username=self.form.cleaned_data["username"],
				password=self.form.cleaned_data["password"],
				email=self.form.cleaned_data["email"])
			return redirect('index2')










