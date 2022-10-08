from rest_framework import serializers
from .models import Carrito, Producto
from .models import Agencia


class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = "__all__"


class AgenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agencia
        fields = "__all__"

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"