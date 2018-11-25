from core.models import Usuario, Cliente

def cadastraCliente(request, login, dados):
    user = Usuario.objects.get(loginusuario=login)
    client = Cliente.objects.filter(logincliente=user)
    if client:
        return True
    else:
        if dados['menor18Anos']:
            cliMenor = Responsavel.objects.create(logincliente=user, nomeResponsavel=dados['responsavel'], )
        cli = Cliente.objects.create(logincliente=user, nomecliente=dados['nome'], dataNascCliente=dados['dataNasc'], rgCliente=dados['rg'], cpfCliente=dados['cpf'], naturalidade)
        cli.save()
