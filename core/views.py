from django.shortcuts import render
#from datetime import datetime
#from django.contrib.auth.decorators import login_required, user_passes_test
from core.backend.instaAPI import alocarFotos
from core.backend.pinterAPI import pins
from core.backend.createUser import salvaUsuario
from core.backend.login import logar, getUsuarios
#from core.models import Usuario

def sair(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return index(request)

def index(request):
    #Usuario.objects.create(loginusuario="tatuador@tattoo.com", senhausuario="$2y$08$0X2GdkM5nBuiL4Dh.Igw6enQ/yegLU866sj7RekUJfH.w6564okSq", tipousuario=True, econfiavel=True)
    context = {
        'fotos': alocarFotos(),
        'resp': request.session.get('user')
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
        Returnlogar = logar(login, password)
        if Returnlogar[0]:
            request.session['user'] = {
                    'username':login,
                    'name':'',
                    'type':Returnlogar[1].tipousuario,
                    'auth':True
                }
            return index(request)
        request.session['user'] = {
                    'username':login,
                    'name':'',
                    'type':Returnlogar[1].tipousuario,
                    'auth':False
                }
        return render(request, 'user/login.html', {'ret':'Usuarios disponiveis: %s Senhas: 123 0 = cliente / 1 = Tatuador' %(getUsuarios())})
    else:
        request.POST
    return render(request, 'user/login.html', {'ret':'Usuarios disponiveis: %s Senhas: 123 0 = cliente / 1 = Tatuador' %(getUsuarios())})

def catalogo(request):

    context = {
        'pins': pins()
    }
    return render(request, 'catalogo.html',context)

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
    else:
        request.POST
        context = {
            'msgs':''
        }
    return render(request, 'user/criarConta.html', context)
