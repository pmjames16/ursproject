from django import forms
from django.contrib.auth.models import User
from .models import Reserv

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']

class ReservForm(forms.ModelForm):
	class Meta:
		model = Reserv
		fields = ['booker', 'camp', 'place', 'date', 'reason']