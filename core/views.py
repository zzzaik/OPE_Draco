from django.shortcuts import render
from django.http import HttpResponseRedirect
#from datetime import datetime
#from django.contrib.auth.decorators import login_required, user_passes_test
from core.backend.instaAPI import alocarFotos
from core.backend.pinterAPI import pins
from core.backend.promos import getPromos
from core.backend.createUser import salvaUsuario
from core.backend.login import logar, getUsuarios
from core.backend.sessionsSettings import verifySession, isLogged, redefSenhaSession, killSession
#from core.backend.enviaConfirmacao import *
from core.backend.redefinicaoSenha import alterarSenha
from core.backend.token import enviarToken, verificarToken
#from core.models import Usuario



def index(request):
    #Usuario.objects.create(loginusuario="tatuador@tattoo.com", senhausuario="$2y$08$0X2GdkM5nBuiL4Dh.Igw6enQ/yegLU866sj7RekUJfH.w6564okSq", tipousuario=True, econfiavel=True)
    #Usuario.objects.create(loginusuario="zzzaik21@gmail.com", senhausuario="$2y$08$Ve0m4XPT8SM5YaR07wFUi.1JMPbvHfPq4xJOs62IzhaLrqk8vM0M2", tipousuario=True, econfiavel=False)
    context = {
        'fotos': alocarFotos(),
        'resp': verifySession(request)
    }
    return render(request, 'index.html', context)

def agenda(request):
    context = {
        'resp': verifySession(request)
    }
    return render(request, 'agenda.html', context)

def promocao(request):
    context = {
        'fotos': getPromos(),
        'pins': pins(),
        'resp': verifySession(request),
    }
    return render(request, 'promocao.html', context)

def portfolio(request):
    context = {
        'fotos': alocarFotos(),
        'resp': verifySession(request)
    }
    return render(request, 'portfolio.html', context)

def catalogo(request):
    context = {
        'pins': pins(),
        'resp': verifySession(request)
    }
    return render(request, 'catalogo.html',context)

def contato(request):
    context = {
        'resp': verifySession(request)
    }
    return render(request, 'contato.html', context)


##############################################   Usuario ##################################################

def login(request):
    if isLogged(request):
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['senha']
        Returnlogar = logar(login, password)
        if Returnlogar[0]:
            request.session['user'] = {
                'login':login,
                'name':'',
                'type':Returnlogar[1],
                'auth':True
            }
            return HttpResponseRedirect('/user/cadastra_dados/')
        request.session['user']['auth'] = False
        return render(request, 'user/login.html', {'ret':'//## Usuarios disponiveis: %s Senhas: 123 0 = cliente / 1 = Tatuador ##//' %(getUsuarios()), 'msg':Returnlogar[2]})
    request.POST
    return render(request, 'user/login.html', {'ret':'Usuarios disponiveis: %s Senhas: 123 0 = cliente / 1 = Tatuador' %(getUsuarios())})

def tokenRedefinirSenha(request):
    if isLogged(request):
        return HttpResponseRedirect('/user/redefinir_senha/')
    if request.method == 'POST':
        login = request.POST['email']
        msg = enviarToken(login, 0)
        redefSenhaSession(request, login)
        if msg != True:
            return render(request, 'user/tokenRedefinirSenha.html', {'msg':msg})
        return HttpResponseRedirect('/user/redefinir_senha/')
    return render(request, 'user/tokenRedefinirSenha.html')

def redefinirSenha(request):
    msg = ''
    salt = 8
    ret = False
    if not isLogged(request):
        pass
    if request.method == 'POST':
        login = request.session['login']
        if login is None:
            ret = True
            login = request.session['user']['login']
        try:
            msg += verificarToken(login, request.POST['token'])
        except:
            pass
        if msg == '':
            msg += alterarSenha(login, request.POST['senha'], request.POST['re_senha'], salt)
            if msg == '':
                try:
                    killSession(request, login)
                except:
                    pass
                return render(request, 'user/redefinirSenha.html', {'msg':'Senha alterada com sucesso', 'ret':ret})
        return render(request, 'user/redefinirSenha.html', {'msg':msg, 'ret':ret})
    ret = True
    return render(request, 'user/redefinirSenha.html', {'msg':msg, 'ret':ret})

def confirmEmail(request):
    ret = False
    if not isLogged(request):
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        msg = verificarToken(request.session['user']['login'], request.POST['token'])
        if msg != '':
            return render(request, 'user/confirmar_email.html', {'msg':msg, 'ret':ret})
        ret = True
        return render(request, 'user/confirmar_email.html', {'ret':ret})
    return render(request, 'user/confirmar_email.html', {'ret':ret})

def configsConta(request):
    if not isLogged(request):
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        context = {'ret':request.POST}
    context = {'ret':request.POST}
    return render(request, 'user/configsConta.html', context)

def sair(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return HttpResponseRedirect('/')


def criarConta(request):
    if isLogged(request):
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        login = request.POST["login"]
        password = request.POST["senha"]
        re_password = request.POST["re_senha"]
        nSalt = 8
        mensagens = salvaUsuario(login, password, re_password, nSalt, False)
        if mensagens != True:
            return render(request, 'user/criarConta.html', {'msgs':mensagens})
        token = enviarToken(login, 1)
        if token != '':
            return render(request, 'user/criarConta.html', {'msgs':token})
        return HttpResponseRedirect('/')
    return render(request, 'user/criarConta.html', {'msgs':''})

def cadastraDados(request):
    if not isLogged(request):
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        context = {
            'resp':request.POST
        }
    context = {
        'resp':''
    }
    request.POST
    return render(request, 'user/cadastraDados.html', context)

#############################################################################################################