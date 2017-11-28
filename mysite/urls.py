"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from urs.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^home/$', home, name = 'home'),
    url(r'^admin/', admin.site.urls, name = 'admin'),
    url(r'^place_list/$', place_list, name = 'post_list'),
    url(r'^signup/home/$', login, name = 'after_signup'),
    
    url(r'^signup/$', signup, name = 'signup'),
    url(r'^accounts/login/$', login, name = 'login'),

    url(r'^bonwon/$', gotobonwon, name = 'bonwon'),
    url(r'^moonji/$', gotomoonji, name = 'moonji'),
    url(r'^hongreung/$', gotohongreung, name = 'hongreung'),
    url(r'^dogok/$', gotodogok, name = 'dogok'),

    url(r'^insert/(?P<name>.+);(?P<camp>.+)', insertplace, name = 'insertplace')
]

