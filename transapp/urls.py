
from django.contrib import admin
from django.urls import path
from transapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name=about),
    path('contact/', views.contact, name=contact),
    path('get-a-quote/', views.get, name=get),
    path('index/', views.index, name=index),
    path('prising/', views.prising, name=prising),
    path('service-details/', views.service, name=service),
    path('services/', views.services, name=services),
    path('starter/', views.starter, name=starter),
]
