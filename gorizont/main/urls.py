from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('price', views.price, name = 'price'),
    path('contakt', views.contakt, name = 'contakt'),
    path('vacancies', views.vacancies, name = 'vacancies')
]