from core.models import Usuario, Cliente

def verificarCliente(request, login):
    user = Usuario.objects.get(loginusuario=login)
    client = Cliente.objects.filter(logincliente=user)
    return not client
