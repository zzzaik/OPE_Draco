from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from core.Backend.criptografia import cript, compararSenha
from core.Backend.instaAPI import alocarFotos
from core.Backend.createUser import verificaLogin, verificaSenha, gravaUsuario
#from core.Backend.login import verificaLogin

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
        password = request.POST["senha"].encode('utf-8')
        passwordHashed = cript(password, 8)
        if compararSenha(password, passwordHashed): #and compararLogin(request.POST["login"].encode('utf-8'))
            pass
            #return index(request)
    else:
        request.POST
    return render(request, 'User/login.html')

def catalogo(request):

    context = {
        'fotos': alocarFotos()
    }
    return render(request, 'catalogo.html',context)

def criarConta(request):
    if request.method == 'POST':
        login = request.POST["login"].encode('utf-8')
        password = request.POST["senha"].encode('utf-8')
        re_password = request.POST["re_senha"].encode('utf-8')
        nSalt = 8
        passwordHashed = cript(password, nSalt)
        re_passwordHashed = cript(re_password, nSalt)
        mensagenLogin = verificaLogin(login)
        mensagenSenha = verificaSenha(password, re_passwordHashed)
        if mensagenLogin == '' and mensagenSenha == '':
            gravaUsuario(login, passwordHashed)
            return render(request, 'User/login.html')
        context = {
            'msgE':mensagenLogin,
            'msgS':mensagenSenha
            }
        return render(request, 'User/criarConta.html', context)
    else:
        request.POST
        context = {
            'msgE':'',
            'msgS':''
        }
    return render(request, 'User/criarConta.html', context)
