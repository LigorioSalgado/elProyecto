from django.shortcuts import render

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