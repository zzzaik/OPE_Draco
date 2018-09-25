import random
import string
from django.core.mail import EmailMessage
from core.models import Token, Usuario
import re

def verifyEmail(email):
    return not re.match(r"^([a-zA-Z0-9._-])+@(([a-zA-Z.-])+.)+([a-zA-Z0-9]{2,4})+$", email)

def randomTokenGenerator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#Tipo: 0(False) = Alterar senha / 1(True) = Confirmar email

def enviarToken(request, login, tipo):
    if verifyEmail(login):
        return 'Digite um e-mail válido! '
    user = Usuario.objects.only('idu suario').filter(loginusuario=login)
    if not user:
        return 'E-mail não encontrado! '
    codigo = randomTokenGenerator()
    mensagem = "Seu código é: %s"  %(codigo)
    from_mail = 'testejira0@gmail.com'
    if tipo == 0:
        subject = 'Código para redefinição de senha'
    else:
        subject = 'Código para confirmação de email'
    email = EmailMessage(subject, mensagem, from_mail, [login])
    email.send()
    token = Token.objects.filter(idusuario=user[0])
    if tipo == 0:
        if user[0].econfiavel == 0:
            return 'Você não confirmou o e-mail, não pode alterar a senha!'
        if user:
            if token:
                token.update(token=codigo)
            else:
                t = Token.objects.create(idusuario=user[0], token=codigo, tipo=tipo)
                t.save()
            return ''
    if token:
        token.update(token=codigo)
    else:
        t = Token.objects.create(idusuario=user[0], token=codigo, tipo=tipo)
        t.save()
    return ''

def verificarToken(login, token):
    user = Usuario.objects.only('idusuario').get(loginusuario=login)
    userToken = Token.objects.filter(idusuario=user)
    if userToken[0].token == token:
        return ''
    return 'Código incorreto! '

def excluirToken(login):
    user = Usuario.objects.only('idusuario').get(loginusuario=login)
    Token.objects.filter(idusuario=user).delete()
