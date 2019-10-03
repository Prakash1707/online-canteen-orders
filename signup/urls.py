from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('register',views.register),
    path('verify',views.verify),
    path('login',views.login),
    path('signin',views.signin),
    path('cartp',views.cartp),
    path('cmplt',views.cmplt),
    path('aboutus',views.aboutus),
    path('home',views.home)
]
