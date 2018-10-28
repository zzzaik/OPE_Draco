"""Projeto_OPE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.contrib.auth.models import User
#from django.conf.urls.static import static
from django.urls import path, re_path, include
from core.views import index, agenda, promocao, portfolio, catalogo, contato
from core.views import login, criarConta, sair, cadastraDados, redefinirSenha, tokenRedefinirSenha, configsConta, confirmEmail, reenviarConfirmarEmail, reenviarRedefinirSenha
from core.views import main, gestaoClientes, gestaoAgenda, gestaoCatalogo, gestaoPortfolio , gestaoPromos, atualizarImagens, postarRedesSociais
from core.views import reset, alimentarJson
from core.views import ListImagensView

urlpatterns = [
    #path('admin/', admin.site.urls, name = 'admin'),
    ######### Endpoint Routes ##########################
    path('dataImagens/', ListImagensView.as_view()),


    ######### comum ############## Páginas comuns para usuarios autenticados e não autenticados
    path('', index, name = 'home'),
    path('agenda/', agenda, name = 'agenda'),
    path('promocao/', promocao, name = 'promocao'),
    path('portfolio/', portfolio, name = 'portfolio'),
    path('catalogo/', catalogo, name = 'catalogo'),
    path('contato/', contato, name = 'contato'),
    ##############################

    ########## usuario ########### Páginas dos usuarios (Comum para cliente e tatuador)
    path('user/login/', login, name = 'login'),
    path('user/criar_conta/', criarConta, name = 'criarConta'),
    path('user/sair/', sair, name='sair'),
    path('user/redefinir_senha/', redefinirSenha, name = 'redefinirSenha'),
    path('user/token_redefinir_senha/', tokenRedefinirSenha, name = 'tokenRedefinirSenha'),
    path('user/configuracao_conta/', configsConta, name = 'configsConta'),
    path('user/cadastra_dados/', cadastraDados, name = 'cadastraDados'),
    path('user/confirmar_email/', confirmEmail, name = 'confirmEmail'),
    path('user/reenviar_confirmacao_email', reenviarConfirmarEmail, name = 'reenviarConfirmarEmail'),
    path('user/reenviar_redefinir_senha', reenviarRedefinirSenha, name = 'reenviarRedefinirSenha'),
    ##############################

    ########## clientes ########## Páginas exclusivas dos clientes


    ########## tatuador ########## Páginas exclusivas dos tatuadores
    path('tatuador/main', main, name = 'main'),
    path('tatuador/clientes', gestaoClientes, name = 'gestaoClientes'),
    path('tatuador/gestao_catalogo', gestaoCatalogo, name = 'gestaoCatalogo'),
    path('tatuador/gestao_portfolio', gestaoPortfolio, name = 'gestaoPortfolio'),
    path('tatuador/gestao_agenda', gestaoAgenda, name = 'gestaoAgenda'),
    path('tatuador/gestao_promos', gestaoPromos, name = 'gestaoPromos'),
    path('tatuador/atualiza_imagens', atualizarImagens, name = 'atualizarImagens'),
    path('tatuador/postar_redes_sociais', postarRedesSociais, name = 'postarRedesSociais'),
    ##############################

    ########## Admins ############ Páginas com o proposito de desenvolvimento
    path('adm/reset/', reset, name = 'reset'),
    path('adm/alimentarJson', alimentarJson, name = 'alimentarJson')
    ##############################
]
