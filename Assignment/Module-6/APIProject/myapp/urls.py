from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.getall),
    path('getone/<int:id>',views.getone),
    path('addbook/',views.addbook),
    path('updatebook/<int:id>',views.updatebook),
    path('deletebook/<int:id>',views.deletebook),


]