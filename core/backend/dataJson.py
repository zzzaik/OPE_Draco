import json
from django.http import HttpResponse
from core.models import Imagem, Estilo, Cor, Regiao, Tamanho

images = Imagem.objects.all()

data = {
        'images':[images]
    }

def getClassificacoes(request):
    data = {
        'estilos':['1','2','3'],
        'cores':['a','b','c'],
        'regiao':['um','dois','tres'],
        'tamanho':['s','m','l']
    }
    if request.method == 'GET':
        return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponse("This is not a GET request", content_type="text/plain")

def fillJson():
    pass
    #with open('core/data.json', 'w') as j:
    #    json.dump(data, j, ensure_ascii=False)

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