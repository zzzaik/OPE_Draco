import json
from django.http import HttpResponse
from core.models import Imagem, Estilo, PromoImagem

def getEstilos():
    estilos = Estilo.objects.all()
    data = []
    for item in estilos:
        data.append({'estiloId':str(item.idestilo), 'estiloName':str(item.estilo)})

    return data

def alterarEstilo(imgId,estiloId):
    imgDB = Imagem.objects.get(pk=imgId)
    newEstilo = Estilo.objects.get(idestilo=estiloId).estilo
    if Imagem.objects.filter(pk=imgId).values('idestilo') == 'NULL':
        if imgDB.idestilo != newEstilo:
            Imagem.objects.filter(pk=imgId).update(idestilo=estiloId)
    else:
        Imagem.objects.filter(pk=imgId).update(idestilo=estiloId)

def getAllImages():
    fotos = []
    imagens = Imagem.objects.all().exclude(idestilo=False)
    for item in imagens:
        idImg = item.idimagem
        urlImg = item.urlimagem
        fotos.append({'id': idImg, 'url': urlImg})
    return fotos