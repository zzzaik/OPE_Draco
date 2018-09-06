from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from core.Backend.instaAPI import alocarFotos
from core.Backend.createUser import salvaUsuario
from core.Backend.login import logar, getUsuarios
from core.models import Usuario

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
        login = request.POST['login']
        password = request.POST['senha']
        if logar(login, password):
            return index(request)
        return render(request, 'user/login.html', {'ret':'Usuarios disponiveis: %s Senhas: 123' %(getUsuarios())})
    else:
        request.POST
    return render(request, 'user/login.html', {'ret':'Usuarios disponiveis: %s Senhas: 123' %(getUsuarios())})

def catalogo(request):

    context = {
        'fotos': alocarFotos()
    }
    return render(request, 'catalogo.html',context)

def criarConta(request):
    if request.method == 'POST':
        login = request.POST["login"]
        password = request.POST["senha"]
        re_password = request.POST["re_senha"]
        nSalt = 8
        mensagens = salvaUsuario(login, password, re_password, nSalt, "c")
        if mensagens != True:
            context = {
                'msgs':mensagens
            }
            return render(request, 'user/criarConta.html', context)
        context = {
            'msgs':''
        }
        return index(request)
    else:
        request.POST
        context = {
            'msgs':''
        }
    return render(request, 'user/criarConta.html', context)
