from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test

def index(request):
    return render(request, 'index.html')

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