from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import Agencia, Carrito, Producto
from .serializers import AgenciaSerializer, CarritoSerializer, ProductoSerializer

#import logging

# Create your views here.
class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer


class AgenciaViewSet(viewsets.ModelViewSet):
    queryset = Agencia.objects.all()
    serializer_class = AgenciaSerializer

class ProductoListarViewSet(generics.CreateAPIView , generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


@api_view(["GET"])
def carritos_compras(request, agenciaId):
    """
    Cantidad de items en el modelo categoria
    """
    #logger.info("Cantidad categoria mostada correctamente")
    try:
        carritos = Carrito.objects.filter(agencia = agenciaId)
        #productos = Producto.objects.filter(unidades='u')
        return JsonResponse(
            CarritoSerializer(carritos, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)