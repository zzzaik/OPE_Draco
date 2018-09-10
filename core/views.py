from django.shortcuts import render
#from datetime import datetime
#from django.contrib.auth.decorators import login_required, user_passes_test
from core.backend.instaAPI import alocarFotos
from core.backend.pinterAPI import pins
from core.backend.createUser import salvaUsuario
from core.backend.login import logar, getUsuarios
#from core.models import Usuario

def verifySession(request):
    if request.session.get('user') is None:
        request.session['user'] = {'username':'','name':'','type':'','auth':False}
    return request.session.get('user')

def index(request):
    #Usuario.objects.create(loginusuario="tatuador@tattoo.com", senhausuario="$2y$08$0X2GdkM5nBuiL4Dh.Igw6enQ/yegLU866sj7RekUJfH.w6564okSq", tipousuario=True, econfiavel=True)
    context = {
        'fotos': alocarFotos(),
        'resp': verifySession(request)
    }
    return render(request, 'index.html', context)

def agenda(request):
    verifySession(request)
    return render(request, 'agenda.html')

def promocao(request):
    verifySession(request)
    return render(request, 'promocao.html')

def portfolio(request):
    verifySession(request)
    context = {
        'fotos': alocarFotos()
    }
    return render(request, 'portfolio.html', context)

def catalogo(request):
    verifySession(request)
    context = {
        'pins': pins()
    }
    return render(request, 'catalogo.html',context)


##############################################   Usuario ##################################################

def isLogged(request):
    verifySession(request)
    return request.session['user']['auth']


def login(request):
    if isLogged(request):
        return index(request)
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['senha']
        Returnlogar = logar(login, password)
        if Returnlogar[0]:
            request.session['user'] = {
                'username':login,
                'name':'',
                'type':Returnlogar[1],
                'auth':True
            }
            return index(request)
        request.session['user']['auth'] = False
        return render(request, 'user/login.html', {'ret':'Usuarios disponiveis: %s Senhas: 123 0 = cliente / 1 = Tatuador' %(getUsuarios())})
    request.POST
    return render(request, 'user/login.html', {'ret':'Usuarios disponiveis: %s Senhas: 123 0 = cliente / 1 = Tatuador' %(getUsuarios())})


def sair(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return index(request)


def criarConta(request):
    if request.method == 'POST':
        login = request.POST["login"]
        password = request.POST["senha"]
        re_password = request.POST["re_senha"]
        nSalt = 8
        mensagens = salvaUsuario(login, password, re_password, nSalt, False)
        if mensagens != True:
            context = {
                'msgs':mensagens
            }
            return render(request, 'user/criarConta.html', context)
        context = {
            'msgs':''
        }
        return index(request)
    request.POST
    context = {
        'msgs':''
    }
    return render(request, 'user/criarConta.html', context)

def cadastraDados(request):
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