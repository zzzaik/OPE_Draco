from django.shortcuts import render
from django.http import HttpResponseRedirect as redirect
from django.http import JsonResponse
from django.urls import reverse
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
#from datetime import datetime
#from django.contrib.auth.decorators import login_required, user_passes_test
from core.backend.instaAPI import alocarFotos, getFoto, salvarFoto, selectFotos, alterarEstilo
from core.backend.pinterAPI import selectPins, salvarPins, getBoards
#from core.backend.fbAPI import postar
#from core.backend.promos import getPromos
from core.backend.calendar import getCalendar
from core.backend.createUser import salvaUsuario
from core.backend.login import logar
from core.backend.sessionsSettings import verifyUserSession, isLogged, redefSenhaSession, killSession, createSession, alterSession
from core.backend.redefinicaoSenha import alterarSenha, verificarSenha
from core.backend.token import enviarToken, verificarToken
from core.backend.getUsuarios import getUsuarios
from core.backend.confirmarEmail import tornarConfiavel
from core.backend.dataJson import fillJson, getEstilos
from core.models import Usuario, Tatuador, Imagem

from core.serializers import ImagensSerializer

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

def alimentarJson(request):
    fillJson()
    alterSession(request, 'firstRun', False)
    return redirect(reverse('home'))

############################ API Endpoints #######################################

class ListImagensView(CreateAPIView):
    querySet = Imagem.objects.all()
    serializerClass = ImagensSerializer
    def post(self, serializer):
        imagem = self.request.data
        s = serializer.save()
        return Response(s)


    def get(self, request, format=None):
        imagens = Imagem.objects.all()
        serial = ImagensSerializer(imagens, many=True)
        return Response(serial.data)

################################################################################

def index(request):
    #Usuario.objects.create(loginusuario="tatuador@tattoo.com", senhausuario="$2y$08$0X2GdkM5nBuiL4Dh.Igw6enQ/yegLU866sj7RekUJfH.w6564okSq", tipousuario=True, econfiavel=True)
    #Usuario.objects.create(loginusuario="zzzaik21@gmail.com", senhausuario="$2y$08$Ve0m4XPT8SM5YaR07wFUi.1JMPbvHfPq4xJOs62IzhaLrqk8vM0M2", tipousuario=True, econfiavel=False)

    context = {
        'user':verifyUserSession(request),
        'fotos':alocarFotos(),
        #'postar':postar()
    }
    return render(request, 'index.html', context)

def agenda(request):
    context = {
        'user': verifyUserSession(request),
        'calendar':  getCalendar()
    }
    return render(request, 'agenda.html', context)

def promocao(request):
    context = {
        'fotos': alocarFotos(),
        'pins': pins(),
        'user': verifyUserSession(request),
    }
    return render(request, 'promocao.html', context)

def portfolio(request):
    context = {
        'fotos': alocarFotos(),
        'user': verifyUserSession(request)
    }
    return render(request, 'portfolio.html', context)

def catalogo(request):
    context = {
        'pins': pins(),
        'user': verifyUserSession(request)
    }
    return render(request, 'catalogo.html',context)

def contato(request):
    context = {
        'user': verifyUserSession(request)
    }
    return render(request, 'contato.html', context)


############################################# Usuario ##################################################

def reenviarConfirmarEmail(request):
    if not isLogged(request):
        return redirect(reverse('home'))
    enviarToken(request, request.session['user']['login'], 1)
    return redirect(reverse('confirmEmail'))

def confirmEmail(request):
    if not isLogged(request):
        return redirect(reverse('home'))
    if request.method == 'POST':
        login = request.session['user']['login']
        msg = verificarToken(login, request.POST['token'])
        if msg != '':
            return render(request, 'user/confirmarEmail.html', {'msg':msg, 'user':verifyUserSession(request)})
        tornarConfiavel(login)
        user = Usuario.objects.get(loginusuario=login)
        request.session['user'] = {'login':user.loginusuario, 'nome':'', 'tipo':user.tipousuario, 'confiavel':user.econfiavel, 'auth':True}
        return render(request, 'user/confirmarEmail.html', {'msg':'E-mail confirmado!', 'user':verifyUserSession(request)})
    return render(request, 'user/confirmarEmail.html', {'user':verifyUserSession(request)})

def tokenRedefinirSenha(request):
    if isLogged(request):
        return redirect(reverse('redefinirSenha'))
    if request.method == 'POST':
        login = request.POST['email']
        msg = enviarToken(request, login, 0)
        redefSenhaSession(request, login)
        if msg != '':
            return render(request, 'user/tokenRedefinirSenha.html', {'msg':msg, 'user':verifyUserSession(request)})
        return redirect(reverse('redefinirSenha'))
    return render(request, 'user/tokenRedefinirSenha.html', {'user':verifyUserSession(request)})

def reenviarRedefinirSenha(request):
    if not isLogged(request):
        enviarToken(request, request.session['login'], 0)
        return redirect(reverse('redefinirSenha'))
    enviarToken(request, request.session['user']['login'], 0)
    return redirect(reverse('redefinirSenha'))

def redefinirSenha(request):
    msg = ''
    ret = request.session['user']['auth']
    if request.session.get('login') is None and not request.session['user']['auth']:
        return redirect(reverse('tokenRedefinirSenha'))
    if request.method == 'POST':
        login = request.session.get('login')
        if login is None:
            login = request.session['user']['login']
        else:
            login = request.session['login']
        try:
            msg += verificarToken(login, request.POST['token'])
        except:
            msg += verificarSenha(login, request.POST['senha_antiga'])
        if msg == '':
            msg += alterarSenha(login, request.POST['senha'], request.POST['re_senha'])
            if msg == '':
                killSession(request, 'login')
                return render(request, 'user/redefinirSenha.html', {'msg':'Senha alterada com sucesso!', 'ret':ret, 'user':verifyUserSession(request)})
        return render(request, 'user/redefinirSenha.html', {'msg':msg, 'ret':ret, 'user':verifyUserSession(request)})
    return render(request, 'user/redefinirSenha.html', {'msg':msg, 'ret':ret, 'user':verifyUserSession(request)})

def cadastraDados(request):
    ret = ''
    if not isLogged(request):
        return redirect(reverse('home'))
    if request.method == 'POST':
        ret = request.POST
    context = {
        'ret':ret,
        'user':verifyUserSession(request)
    }
    request.POST
    return render(request, 'user/cadastraDados.html', context)

def configsConta(request):
    if not isLogged(request):
        return redirect(reverse('home'))
    if request.method == 'POST':
        context = {'ret':request.POST, 'user':verifyUserSession(request)}
    context = {'ret':request.POST, 'user':verifyUserSession(request)}
    return render(request, 'user/configsConta.html', context)

def criarConta(request):
    if isLogged(request):
        return redirect(reverse('home'))
    if request.method == 'POST':
        login = request.POST["login"]
        password = request.POST["senha"]
        re_password = request.POST["re_senha"]
        mensagens = salvaUsuario(login, password, re_password)
        if mensagens != True:
            return render(request, 'user/criarConta.html', {'msgs':mensagens})
        token = enviarToken(request, login, 1)
        if token != '':
            return render(request, 'user/criarConta.html', {'msgs':token})
        return redirect(reverse('login'))
    return render(request, 'user/criarConta.html', {'msgs':'', 'user':verifyUserSession(request)})

def login(request):
    if isLogged(request):
        return redirect(reverse('home'))
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['senha']
        returnLogar = logar(login, password)
        if returnLogar == '':
            user = Usuario.objects.get(loginusuario=login)
            if user.tipousuario == 1:
                nome = Tatuador.objects.get(logintatuador=user.idusuario).nometatuador
            else:
                nome = ''
            request.session['user'] = {'login':login, 'nome':nome, 'tipo':user.tipousuario, 'confiavel':user.econfiavel, 'auth':True}
            return redirect(reverse('cadastraDados'))
        request.session['user']['auth'] = False
        return render(request, 'user/login.html', {'ret':'Usuarios disponiveis: %s Senhas: 12345678 0 = cliente / 1 = Tatuador' %(getUsuarios()), 'msg':returnLogar, 'user':verifyUserSession(request)})
    request.POST
    return render(request, 'user/login.html', {'ret':'Usuarios disponiveis: %s Senhas: 12345678 0 = cliente / 1 = Tatuador' %(getUsuarios()), 'user':verifyUserSession(request)})

def sair(request):
    killSession(request, 'user')
    verifyUserSession(request)
    return redirect(reverse('login'))

#############################################################################################################

############################################### Tatuador ####################################################

def main(request):
    if not isLogged(request):
        return redirect(reverse('home'))
    if request.session['user']['tipo'] != 1:
        return redirect(reverse('home'))
    return render(request, 'tatuador/main.html', {'user':verifyUserSession(request)})

def gestaoClientes(request):
    if not isLogged(request):
        return redirect(reverse('home'))
    if request.session['user']['tipo'] != 1:
        return redirect(reverse('home'))
    return render(request, 'tatuador/gestaoClientes.html', {'user':verifyUserSession(request)})

def gestaoCatalogo(request):
    if not isLogged(request):
        return redirect(reverse('home'))
    if request.session['user']['tipo'] != 1:
        return redirect(reverse('home'))

    context = {
        'data':selectFotos(),
        'estilos': getEstilos(),
        'user':verifyUserSession(request)
    }

    return render(request, 'tatuador/gestaoCatalogo.html', context)

def gestaoPortfolio(request):
    if not isLogged(request):
        return redirect(reverse('home'))
    if request.session['user']['tipo'] != 1:
        return redirect(reverse('home'))

    context = {
        "data": selectPins(),
        "boards": getBoards(),
        'user':verifyUserSession(request),
    }

    return render(request, 'tatuador/gestaoPortfolio.html', context)

def gestaoAgenda(request):
    if not isLogged(request):
        return redirect(reverse('home'))
    if request.session['user']['tipo'] != 1:
        return redirect(reverse('home'))
    return render(request, 'tatuador/gestaoAgenda.html', {'user':verifyUserSession(request)})

def gestaoPromos(request):
    if not isLogged(request):
        return redirect(reverse('home'))
    if request.session['user']['tipo'] != 1:
        return redirect(reverse('home'))
    return render(request, 'tatuador/gestaoPromos.html', {'user':verifyUserSession(request)})

def atualizarImagens(request):
    if not isLogged(request):
        return redirect(reverse('home'))
    if request.session['user']['tipo'] != 1:
        return redirect(reverse('home'))
    salvarFoto('Outros')
    salvarPins()
    #função para alimentar o json com as imagens do banco
    return redirect(reverse('home'))

def postarRedesSociais(request):
    if not isLogged(request):
        return redirect(reverse('home'))
    if request.session['user']['tipo'] != 1:
        return redirect(reverse('home'))
    #Interação com as redes sociais
    salvarFoto('Outros')
    salvarPins()
    #função para alimentar o json com as imagens do banco
    return render(request, 'tatuador/postarRedesSociais.html')


def saveGestaoCatalogo(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = request.body
            for item in data:
                alterarEstilo(item.imgId, item.estiloId)
            response = JsonResponse({"success":"Database Updated"})
            response.status_code = 200
            return response
        else:
            response = JsonResponse({"error":"Only POST method allowed"})
            response.status_code = 403
            return response
    else:
        response = JsonResponse({"error":"Request is not AJAX"})
        response.status_code = 500
        return response













#############################################################################################################