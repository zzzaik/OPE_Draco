from django.shortcuts import render
from django.http import HttpResponseRedirect as redirect
from django.urls import reverse
#from datetime import datetime
#from django.contrib.auth.decorators import login_required, user_passes_test
from core.backend.instaAPI import alocarFotos
from core.backend.pinterAPI import pins
#from core.backend.promos import getPromos
from core.backend.createUser import salvaUsuario
from core.backend.login import logar
from core.backend.sessionsSettings import verifySession, isLogged, redefSenhaSession, killSession, atualuzarUserSession
#from core.backend.enviaConfirmacao import *
from core.backend.redefinicaoSenha import alterarSenha
from core.backend.token import enviarToken, verificarToken
from core.backend.getUsuarios import getUsuarios
from core.backend.confirmarEmail import tornarConfiavel
from core.models import Usuario

############################### Admin ##########################################

def reset(request):
    sess = []
    for x in request.session.keys():
        sess.append(x)
    for y in sess:
        try:
            del request.session[y]
        except KeyError:
            pass
    return redirect(reverse('home'))

################################################################################

def index(request):
    #Usuario.objects.create(loginusuario="tatuador@tattoo.com", senhausuario="$2y$08$0X2GdkM5nBuiL4Dh.Igw6enQ/yegLU866sj7RekUJfH.w6564okSq", tipousuario=True, econfiavel=True)
    #Usuario.objects.create(loginusuario="zzzaik21@gmail.com", senhausuario="$2y$08$Ve0m4XPT8SM5YaR07wFUi.1JMPbvHfPq4xJOs62IzhaLrqk8vM0M2", tipousuario=True, econfiavel=False)
    context = {
        'user':verifySession(request),
        'fotos':alocarFotos()
    }
    return render(request, 'index.html', context)

def agenda(request):
    context = {
        'user': verifySession(request)
    }
    return render(request, 'agenda.html', context)

def promocao(request):
    context = {
        'fotos': alocarFotos(),
        'pins': pins(),
        'user': verifySession(request),
    }
    return render(request, 'promocao.html', context)

def portfolio(request):
    context = {
        'fotos': alocarFotos(),
        'user': verifySession(request)
    }
    return render(request, 'portfolio.html', context)

def catalogo(request):
    context = {
        'pins': pins(),
        'user': verifySession(request)
    }
    return render(request, 'catalogo.html',context)

def contato(request):
    context = {
        'user': verifySession(request)
    }
    return render(request, 'contato.html', context)


############################################# Usuario ##################################################

def confirmEmail(request):
    if not isLogged(request):
        return redirect(reverse('home'))
    if request.method == 'POST':
        login = request.session['user']['login']
        msg = verificarToken(login, request.POST['token'])
        if msg != '':
            return render(request, 'user/confirmarEmail.html', {'msg':msg, 'user':verifySession(request)})
        tornarConfiavel(login)
        atualuzarUserSession(request, 'user', 'confiavel', Usuario.objects.get(loginusuario=login).econfiavel)
        return render(request, 'user/confirmarEmail.html', {'msg':'E-mail confirmado!', 'user':verifySession(request)})
    return render(request, 'user/confirmarEmail.html', {'user':verifySession(request)})

def tokenRedefinirSenha(request):
    if isLogged(request):
        return redirect(reverse('redefinirSenha'))
    if request.method == 'POST':
        login = request.POST['email']
        msg = enviarToken(login, 0)
        redefSenhaSession(request, login)
        if msg != '':
            return render(request, 'user/tokenRedefinirSenha.html', {'msg':msg, 'user':verifySession(request)})
        return redirect(reverse('redefinirSenha'))
    return render(request, 'user/tokenRedefinirSenha.html', {'user':verifySession(request)})

def redefinirSenha(request):
    msg = ''
    salt = 8
    ret = False
    if request.method == 'POST':
        login = request.session.get('login')
        if login is None:
            ret = True
            login = request.session['user']['login']
        else:
            login = request.session['login']
        try:
            msg += verificarToken(login, request.POST['token'])
        except:
            pass
        if msg == '':
            msg += alterarSenha(login, request.POST['senha'], request.POST['re_senha'], salt)
            if msg == '':
                killSession(request, 'login')
                return render(request, 'user/redefinirSenha.html', {'msg':'Senha alterada com sucesso!', 'ret':ret, 'user':verifySession(request)})
        return render(request, 'user/redefinirSenha.html', {'msg':msg, 'ret':ret, 'user':verifySession(request)})
    return render(request, 'user/redefinirSenha.html', {'msg':msg, 'ret':ret, 'user':verifySession(request)})

def cadastraDados(request):
    ret = ''
    if not isLogged(request):
        return redirect(reverse('home'))
    if request.method == 'POST':
        ret = request.POST
    context = {
        'ret':ret,
        'user':verifySession(request)
    }
    request.POST
    return render(request, 'user/cadastraDados.html', context)

def configsConta(request):
    if not isLogged(request):
        return redirect(reverse('home'))
    if request.method == 'POST':
        context = {'ret':request.POST, 'user':verifySession(request)}
    context = {'ret':request.POST, 'user':verifySession(request)}
    return render(request, 'user/configsConta.html', context)

def criarConta(request):
    if isLogged(request):
        return redirect(reverse('home'))
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
        return redirect(reverse('login'))
    return render(request, 'user/criarConta.html', {'msgs':'', 'user':verifySession(request)})

def login(request):
    if isLogged(request):
        return redirect(reverse('home'))
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['senha']
        returnLogar = logar(login, password)
        if returnLogar == '':
            user = Usuario.objects.get(loginusuario=login)
            request.session['user'] = {'login':login, 'nome':'', 'tipo':user.tipousuario, 'confiavel':user.econfiavel, 'auth':True}
            return redirect(reverse('cadastraDados'))
        request.session['user']['auth'] = False
        return render(request, 'user/login.html', {'ret':'Usuarios disponiveis: %s Senhas: 123 0 = cliente / 1 = Tatuador' %(getUsuarios()), 'msg':returnLogar, 'user':verifySession(request)})
    request.POST
    return render(request, 'user/login.html', {'ret':'Usuarios disponiveis: %s Senhas: 123 0 = cliente / 1 = Tatuador' %(getUsuarios()), 'user':verifySession(request)})

def sair(request):
    killSession(request, 'user')
    return redirect(reverse('reset'))

#############################################################################################################

############################################### Tatuador ####################################################

def gestaoClientes(request):
    if not isLogged(request):
        return redirect(reverse('home'))
    if request.session['user']['tipo'] != 1:
        return redirect(reverse('home'))
    return render(request, 'tatuador/gestaoClientes.html', {'user':verifySession(request)})

#############################################################################################################