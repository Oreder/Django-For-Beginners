# app/urls.py

from django.conf.urls import url

from app import views

urlpatterns = [
	url('^$', views.index, name='index'),
	url('profile/', views.profile, name='profile'),
]