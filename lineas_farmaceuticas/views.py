from rest_framework import generics
from .models import LineasFarmaceuticas
from .serializers import LineaFarmaceuticaSerializer
from rest_framework.permissions import (DjangoModelPermissions)

class LineaFarmaceuticaList(generics.ListAPIView):
    queryset = LineasFarmaceuticas.objects.all()
    serializer_class = LineaFarmaceuticaSerializer
    permission_classes = [DjangoModelPermissions]

class LineaFarmaceuticaCreate(generics.CreateAPIView):
    queryset = LineasFarmaceuticas.objects.all()
    serializer_class = LineaFarmaceuticaSerializer
    permission_classes = [DjangoModelPermissions]

class LineaFarmaceuticaDetail(generics.RetrieveAPIView):
    queryset = LineasFarmaceuticas.objects.all()
    serializer_class = LineaFarmaceuticaSerializer
    permission_classes = [DjangoModelPermissions]

class LineaFarmaceuticaUpdate(generics.UpdateAPIView):
    queryset = LineasFarmaceuticas.objects.all()
    serializer_class = LineaFarmaceuticaSerializer
    permission_classes = [DjangoModelPermissions]

class LineaFarmaceuticaDelete(generics.DestroyAPIView):
    queryset = LineasFarmaceuticas.objects.all()
    serializer_class = LineaFarmaceuticaSerializer
    permission_classes = [DjangoModelPermissions]
