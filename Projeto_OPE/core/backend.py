import requests as req


############Criptografia##############
import bcrypt
def cript(password, nSalt):
    passwordHashed = bcrypt.hashpw(password, bcrypt.gensalt(nSalt))
    return passwordHashed

def compararSenha(password, passwordHashed):
    if bcrypt.hashpw(password, passwordHashed) == passwordHashed:
        return True
    return False

def compararLogin(login):
    logins = [login]#Lista de logins do banco
    if login in logins:
        return True
    return False
######################################
#############Instagram################
def getPhoto():
    url = "https://api.instagram.com/v1/users/self/media/recent/?access_token=3251373559.1556bce.467e8e9f0219425abf9915fa978bb275"
    ret = req.api.get(url).json()
    return ret

def alocarFotos():
    fotos = {}
    resp = getPhoto()
    cont = 0
    for elements in resp['data']:
        fotos[cont] = elements['images']['standard_resolution']['url']
        cont += 1
    return fotos
######################################
#############Instagram################
'''
def getPins():
    url = "https://api.instagram.com/v1/users/self/media/recent/?access_token=3251373559.1556bce.467e8e9f0219425abf9915fa978bb275"
    ret = req.api.get(url).json()
    return ret

def alocarFotos():
    fotos = {}
    resp = getPhoto()
    cont = 0
    for elements in resp['data']:
        fotos[cont] = elements['images']['standard_resolution']['url']
        cont += 1
    return fotos
'''
######################################