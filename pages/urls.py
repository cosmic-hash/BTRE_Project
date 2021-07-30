from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'), #here '' contains no path means home page
    path('about', views.about, name='about'),
]