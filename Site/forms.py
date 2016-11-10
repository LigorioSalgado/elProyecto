from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
'''
	first_name
	last_name
	username
	password
	email
	is_active
	is_staff
	is_superuser
'''


class RegisterForm(ModelForm):

	class Meta:
		model=User
		fields = ["first_name","last_name","username","password","email"]
		widgets = {
		"password":forms.PasswordInput(attrs={
			"type":"password"})

		}




class LoginForm(forms.Form):

	username = forms.CharField(max_length=100,
		widget=forms.TextInput(attrs={'placeholder':"pepito1"}))

	password =  forms.CharField(max_length=100,
		widget=forms.PasswordInput(attrs={
			"type":"password"}))


