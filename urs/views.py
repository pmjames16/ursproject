from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.template import RequestContext


def home(request):
	return render(request, 'home.html')

def place_list(request):
	return render(request, 'place_list.html')

def signup(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			login(request, new_user)
			return redirect('home')
		else :
			return HttpResponse('다시 시도해보세요')
	else:
		form = UserForm()
		return render(request, 'adduser.html', {'form': form})

def login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		username = request.POST('username')
		password = request.POST('password')
		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else : 
			return HttpResponse('다시 시도해보세요')
	else :
		form = LoginForm()
		return render(request, 'login.html', {'form': form})

def gotobonwon(request):
	return render(request, 'bonwon.html')

def gotomoonji(request):
	return render(request, 'moonji.html')

def gotohongreung(request):
	return render(request, 'hongreung.html')

def gotodogok(request):
	return render(request, 'dogok.html')

