from django.shortcuts import render
from .models import Slidemainpage
from .models import Aboutus
from .models import Quest
from .models import Prices
from .models import Testimonials


def index(request):
    slidemain = Slidemainpage.objects.all()
    aboutus = Aboutus.objects.get()
    quest = Quest.objects.all()
    prises = Prices.objects.all()
    testi = Testimonials.objects.all()[:3]


    return render(request, 'main/index.html', {'slidemain' : slidemain, 'about' : aboutus, 'quest' : quest, 'prices': prises, 'testi': testi})

def about(request):
    return render(request, 'main/about.html')

def price(request):
    return render(request, 'main/price.html')

def contakt(request):
    return render(request, 'main/contakt.html')

def vacancies(request):
    return render(request, 'main/vacancies.html')