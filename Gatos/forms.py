from django import forms
from .models import Comida
from django.forms import ModelForm

class GatoForm(forms.Form):
	SEXO_CHOICES= (
		("M","Masculino"),
		("F", "Femenino")
	)


	name = forms.CharField(label='El nombre del gato:', max_length=100, widget=forms.TextInput(attrs={'class':'name'}))
	age =  forms.IntegerField(label='La edad del gato')
	callejero = forms.BooleanField(	label="Es callegero?")
	sexo = forms.ChoiceField(choices=SEXO_CHOICES)
	comida = forms.ModelChoiceField(queryset=Comida.objects.all())


class ComidaForm(ModelForm):

	class Meta:
		model = Comida
		
		exclude = ["compra"]
		widget= {
				'tipo':forms.TextInput(attrs={'class':'tipo'})
		}

