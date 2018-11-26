from core.models import Usuario, Cliente


def emailAgenda(request, login, dados):
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