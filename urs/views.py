from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm, ReservForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.template import RequestContext
from urs.models import Place, Reserv
from datetime import datetime
from urs.calendar import monthtoname, dayday, daysweek, times

def home(request):
	return render(request, 'home.html')

def signup(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(
				username=request.POST['username'],
				password=request.POST['password'],
				email=request.POST['email'],
			)
			login(request, authenticate(
				username=request.POST['username'],
				password=request.POST['password'],
			))
			return redirect('/')
		else :
			return HttpResponse('다시 시도해보세요')
	else:
		form = UserForm()
		return render(request, 'adduser.html', {'form': form})

def signin(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else : 
			return HttpResponse('다시 시도해보세요')
	else :
		form = LoginForm()
		return render(request, 'login.html', {'form': form})

def signout(request):
	logout(request)
	return redirect('/')

def gotocampus(request, campus):
	places = Place.objects.filter(camp = campus)
	month = datetime.today().month
	day = datetime.today().day
	time = datetime.today().hour
	today = datetime.today()
	name = monthtoname(month)
	days = dayday(month)
	daytime = times()
	return render(
		request,
		'campus.html',
		{'places': places, 'camp': campus,
		 'month': name, 'date': day, 'times': daytime,
		 'time': time, 'today': today, 'days': days, 'daysweek': daysweek(days)}
	)




def placeinfo(request, campus, placeid):
	places = Place.objects.filter(camp=campus)
	month = datetime.today().month
	day = datetime.today().day
	time = datetime.today().hour
	today = datetime.today()
	name = monthtoname(month)
	days = dayday(month)
	daytime = times()
	place = Place.objects.get(id=placeid)
	explain = place.explain()
	return render(request, 'placeinfo.html',
				  {'places': places, 'camp': campus, 'pla': place, 'id':placeid, 'explain': explain,
				   'month': name, 'date': day, 'times': daytime,
				   'time': time, 'today': today, 'days': days, 'daysweek': daysweek(days)})


def chooseday(request, campus, placeid, when):
	places = Place.objects.filter(camp=campus)
	month = datetime.today().month
	day = datetime.today().day
	time = datetime.today().hour
	today = datetime.today()
	name = monthtoname(month)
	days = dayday(month)
	daytime = times()
	place = Place.objects.get(id=placeid)
	explain = place.explain()
	return render(request, 'chooseday.html',
				  {'places': places, 'camp':campus, 'pla': place, 'id':placeid, 'explain': explain,
				   'month': name, 'date': day, 'times': daytime, 'rday':when,
				   'time': time, 'today': today, 'days': days, 'daysweek': daysweek(days)})

def reservate(request, campus, placeid, when):
	if request.method=="POST":
		form = ReservForm(request.POST)
		if form.is_valid():
			Reserv.objects.create(
				booker=request.POST['booker'],
				campus=request.POST['campus'],
				place=request.POST['place'],
				date=request.POST['date'],
				reason=request.POST['reason'],
			)
			return redirect('/')
	else:
		place = Place.objects.get(id=placeid)
		form = ReservForm()
		return render(request, 'reservate.html',
					  {'form': form, 'camp':campus, 'place':place, 'date':when})



