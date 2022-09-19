from rest_framework.viewsets import ModelViewSet

from core.models import Carro, Categoria, Marca
from core.serializers import (
    CarroSerializer,
    CarroDetailSerializer,
    CategoriaSerializer,
    MarcaSerializer,
)


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CarroDetailSerializer
        return CarroSerializer
