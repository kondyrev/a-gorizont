from django.shortcuts import render
from .models import Slidemainpage
from .models import Aboutus
from .models import Quest


def index(request):
    slidemain = Slidemainpage.objects.all()
    aboutus = Aboutus.objects.get()
    quest = Quest.objects.all()
    return render(request, 'main/index.html', {'slidemain' : slidemain, 'about' : aboutus, 'quest' : quest})

def about(request):
    return render(request, 'main/about.html')

def price(request):
    return render(request, 'main/price.html')

def contakt(request):
    return render(request, 'main/contakt.html')

def vacancies(request):
    return render(request, 'main/vacancies.html')