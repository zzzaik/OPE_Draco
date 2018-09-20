import bcrypt

def cript(password, nSalt=8):
    passwordHashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(nSalt))
    return passwordHashed.decode('utf-8')

def compararSenha(password, passwordHashed):
    if bcrypt.hashpw(password.encode('utf-8'), passwordHashed.encode('utf-8')) == passwordHashed.encode('utf-8'):
        return True
    return False