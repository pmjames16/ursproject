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
	url(r'^$', home, name = 'home'),
    url(r'^admin/', admin.site.urls, name = 'admin'),
    
    url(r'^signup/$', signup, name = 'signup'),
    url(r'^accounts/login/$', signin, name = 'login'),
    url(r'^accounts/logout/$', signout, name = 'logout'),
    #url(r'^logout/$', logout, {'next_page': 'home/'}),
    url(r'^(?P<campus>[가-힣\s]+)/$', gotocampus, name = 'gotocampus'),
    url(r'^(?P<campus>[가-힣\s]+)/(?P<placeid>[0-9]+)$', placeinfo, name = 'placeinfo'),
    url(r'^(?P<campus>[가-힣\s]+)/(?P<placeid>[0-9]+)/(?P<when>[0-9]+)$', chooseday, name = 'chooseday'),
    url(r'^(?P<campus>[가-힣\s]+)/(?P<placeid>[0-9]+)/(?P<when>[0-9]+)/reservate$', reservate, name = 'reservate'),

]

