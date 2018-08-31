import bcrypt

def cript(password, nSalt):
    passwordHashed = bcrypt.hashpw(password, bcrypt.gensalt(nSalt))
    return passwordHashed

def compararSenha(password, passwordHashed):
    if bcrypt.hashpw(password, passwordHashed) == passwordHashed:
        return True
    return False