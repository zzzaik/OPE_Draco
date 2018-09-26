import requests as req
from core.models import Imagem, Tag, Imagemtag

def getPhoto():
    url = "https://api.instagram.com/v1/users/self/media/recent/?access_token=3251373559.1556bce.467e8e9f0219425abf9915fa978bb275"
    ret = req.api.get(url).json()
    return ret
'''
def savePhoto()
    fotos = getPhoto()
    for foto in fotos['data']:
        img = Imagens.objects.create(urlimagem=foto['images']['standard_resolution']['url'], )
'''

def alocarFotos(imgs=0):
    fotos = {}
    resp = getPhoto()
    cont = 0
    if imgs == 0:
        for elements in resp['data']:
            fotos[cont] = elements['images']['standard_resolution']['url']
            cont += 1
        return fotos
    else:
        elements = resp['data']
        while cont < imgs:
            fotos[cont] = elements[cont]['images']['standard_resolution']['url']
            cont += 1
        return fotos