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
    for estilo in estilos:
        data.append(estilo)

    return data