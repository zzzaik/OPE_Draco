from rest_framework import serializers
from core.models import Imagem

class ImagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ["idimagem","urlimagem","ratins","idestilo","fonteimagem"]