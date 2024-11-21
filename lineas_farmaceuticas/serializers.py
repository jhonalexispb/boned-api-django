from rest_framework import serializers
from .models import LineasFarmaceuticas

class LineaFarmaceuticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineasFarmaceuticas
        fields = '__all__'