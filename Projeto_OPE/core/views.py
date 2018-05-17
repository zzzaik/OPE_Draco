from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from core.tests import getPhoto

def index(request):
    fotos = []
    resp = getPhoto()
    for elements in resp['data']:
        fotos.append(elements['images']['standard_resolution']['url'])
    context = {
        'fotos':fotos
    }
    return render(request, 'index.html', context)

def agenda(request):
    return render(request, 'agenda.html')

def promocao(request):
    return render(request, 'promocao.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def login(request):
    return render(request, 'login.html')

def catalogo(request):
    return render(request, 'catalogo.html')