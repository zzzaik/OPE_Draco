import json
from django.http import HttpResponse
from core.models import Imagem, Estilo, Cor, Regiao, Tamanho

images = Imagem.objects.all()

data = {
        'images':[images]
    }

def getClassificacoes():
    data = {
        'estilos':[],
        'cores':[],
        'regiao':[],
        'tamanho':[]
    }

    for item in Estilo.objects.all():
        data['estilos'].append({'id':item.idEstilo,'desc':item.estilo})
    for item in Cor.objects.all():
        data['cores'].append({'id':item.idCor,'desc':item.colorido})
    for item in Regiao.objects.all():
        data['regiao'].append({'id':item.idRegiao,'desc':item.regiaodocorpo})
    for item in Tamanho.objects.all():
        data['regiao'].append({'id':item.idRegiao,'desc':item.regiaodocorpo})
    
    return HttpResponse(json.dumps(data), content_type="application/json")

def fillJson():
    pass
    #with open('core/data.json', 'w') as j:
    #    json.dump(data, j, ensure_ascii=False)