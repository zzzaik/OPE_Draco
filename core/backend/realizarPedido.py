from core.models import Usuario, Cliente

def verificarCliente(request, login):
    user = Usuario.objects.get(loginusuario=login)
    client = Cliente.objects.filter(logincliente=user)
    if client:
        return True
    return False
