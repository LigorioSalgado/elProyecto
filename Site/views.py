from django.shortcuts import render

# Create your views here.

def  index(request):

	return render(request,'index.html')

def  contacto(request):

	print("En contacto")

	return render(request,'contacto.html')