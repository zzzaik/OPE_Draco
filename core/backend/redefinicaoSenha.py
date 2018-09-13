import random
import string
from django.core.mail import EmailMessage
from core.models import Token, Usuario
from core.backend.criptografia import cript, compararSenha

def randomTokenGenerator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def enviarToken(login):
    codigo = randomTokenGenerator()
    mensagem = 'Seu código é: %s' %(codigo)
    from_mail = 'testejira0@gmail.com'
    email = EmailMessage('Código para redefinição de senha', mensagem, from_mail, [login])
    email.send()
    token = '%s:%s' %(login, codigo)
    user = Usuario.objects.only('idusuario').get(loginusuario=login)
    if user:
        userToken = Token.objects.filter(idusuario=user)
        if not userToken:
            t = Token.objects.create(idusuario=user, token=token)
            t.save()
        else:
            userToken.update(token=token)
        return True
    return 'Usuário não encontrado!'

def verificarToken(login, token):
    user = Usuario.objects.only('idusuario').get(loginusuario=login)
    userToken = str(Token.objects.get(idusuario=user))
    t = userToken.split(':')
    if t[1] == token:
        return ''
    return 'Código incorreto! '

def alterarSenha(login, password, re_password, salt):
    user = Usuario.objects.get(loginusuario=login)
    if password == re_password and compararSenha(password, cript(re_password, salt)):
        user.senhausuario = cript(password, salt)
        return ''
    return 'As senhas não batem! '





