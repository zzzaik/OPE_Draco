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
from django.urls import path#, include
from core.views import index, agenda, promocao, portfolio, catalogo, login, criarConta, sair, cadastraDados, redefinirSenha, tokenRedefinirSenha, configsConta, confirmEmail

urlpatterns = [
    #path('admin/', admin.site.urls, name = 'admin'),
    path('', index, name = 'home'),
    path('agenda/', agenda, name = 'agenda'),
    path('promocao/', promocao, name = 'promocao'),
    path('portfolio/', portfolio, name = 'portfolio'),
    path('catalogo/', catalogo, name = 'catalogo'),
    ########## usuario ###########
    path('user/login/', login, name = 'login'),
    path('user/criar_conta/', criarConta, name = 'criarConta'),
    path('user/sair/', sair, name='sair'),
    path('user/redefinir_senha/', redefinirSenha, name = 'redefinirSenha'),
    path('user/token_redefinir_senha/', tokenRedefinirSenha, name = 'tokenRedefinirSenha'),
    path('user/configuracao_conta/', configsConta, name = 'configsConta'),
    path('user/cadastra_dados/', cadastraDados, name = 'cadastraDados'),
    path('user/comfirmar_email/', confirmEmail, name = 'confirmEmail'),
    ##############################
]