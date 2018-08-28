from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from core.backend import alocarFotos, cript, compararSenha

def index(request):
    
    context = {
        'fotos': alocarFotos(),
    }
    return render(request, 'index.html', context)

def agenda(request):
    return render(request, 'agenda.html')

def promocao(request):

    return render(request, 'promocao.html')

def portfolio(request):
    
    context = {
        'fotos': alocarFotos()
    }
    return render(request, 'portfolio.html', context)

def login(request):
    if request.method == 'POST':
        infos = cript(request)
        if compararSenha(infos):
            return index(request)
    else:
        request.POST
    return render(request, 'login.html')

def catalogo(request):
    return render(request, 'catalogo.html')