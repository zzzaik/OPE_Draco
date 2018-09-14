import random
import string
from django.core.mail import EmailMessage
from core.models import Token, Usuario

def randomTokenGenerator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def enviarToken(login, tipo):
    codigo = randomTokenGenerator()
    mensagem = 'Seu código é: %s' %(codigo)
    from_mail = 'testejira0@gmail.com'
    email = EmailMessage('Código para redefinição de senha', mensagem, from_mail, [login])
    email.send()
    token = '%s:%s' %(login, codigo)
    user = Usuario.objects.only('idusuario').get(loginusuario=login)
    if tipo == 0:
        if user.econfiavel == 0:
            return 'Você não confirmou o e-mail, não pode alterar a senha!'
        if user:
            userToken = Token.objects.filter(idusuario=user)
            if not userToken:
                t = Token.objects.create(idusuario=user, token=token, ativo=1, tipo=tipo)
                t.save()
            else:
                userToken.update(token=token, ativo=1, tipo=tipo)
            return True
        return 'Usuário não encontrado!'
    userToken = Token.objects.filter(idusuario=user)
    if not userToken:
        t = Token.objects.create(idusuario=user, token=token, ativo=1, tipo=tipo)
        t.save()
    else:
        userToken.update(token=token, ativo=1, tipo=tipo)
    return ''

def verificarToken(login, token):
    user = Usuario.objects.only('idusuario').get(loginusuario=login)
    userToken = Token.objects.filter(idusuario=user)
    t = str(userToken[0].token).split(':')
    if userToken[0].ativo == 0:
        return 'O código informado não está ativo! '
    if t[1] == token:
        return ''
    return 'Código incorreto! '