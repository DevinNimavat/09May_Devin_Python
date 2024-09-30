from django.contrib import admin
from django.urls import path, include

from insuranceapp import views

urlpatterns = [
    path('',views.index),
    path('register/',views.register),
    path('otpverify/',views.otpverify,name='otpverify'),
    path('apply/',views.apply,name='apply'),
    path('health/',views.health),
    path('life/',views.life),
    path('vehicle/',views.vehicle),
    path('userlogout/',views.userlogout),
    path('home/',views.home),
    path('travel',views.travel),
    path('business',views.business),
    path('email_verify/',views.email_verify),
    path('reset_password/',views.reset_password,name='reset_password'),

]