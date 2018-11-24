import requests as req
import random
from core.models import Imagem,


def getPromos(imgs=0):
    fotos = {}
    resp = getPhoto()
    cont = 0
    if imgs == 0:
        for elements in resp['data']:
            fotos[cont] = {'url':elements['images']['standard_resolution']['url'],'desconto':str(random.randint(15,50))+'%'}
            cont += 1
            return fotos
    else:
        elements = resp['data']
        while cont < imgs:
            fotos[cont] = {'url':elements['images']['standard_resolution']['url'],'desconto':str(random.randint(15,50))+'%'}
            cont += 1
            return fotos