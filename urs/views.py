from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.template import RequestContext
from urs.models import Place
from datetime import datetime
from urs.calendar import monthtoname, dayday, daysweek, times

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
	places = Place.objects.filter(camp = '본원')
	month = datetime.today().month
	day = datetime.today().day
	time = datetime.today().hour
	today = datetime.today()
	name = monthtoname(month)
	days = dayday(month)
	daytime = times()

	return render(
		request,
		'bonwon.html',
		{'places':places, 'month': name, 'date': day, 'times':daytime,
		 'time': time, 'today': today, 'days':days, 'daysweek':daysweek(days)}
	)

def gotomoonji(request):
	return render(request, 'moonji.html')

def gotohongreung(request):
	return render(request, 'hongreung.html')

def gotodogok(request):
	return render(request, 'dogok.html')

def insertplace(request, name, camp):
	Place(name = name, camp = camp).save()
	return render(request, 'insert.html', {'welcome text': 'Insert' + name + camp})


