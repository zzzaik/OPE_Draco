import json
from core.models import Imagem

images = Imagem.objects.all()

data = {
        'images':[images]
    }

def fillJson():
    pass
    #with open('core/data.json', 'w') as j:
    #    json.dump(data, j, ensure_ascii=False)