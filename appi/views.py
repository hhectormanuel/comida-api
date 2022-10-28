from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Producto, Orden
from .serializer import ProductoSerializer, OrdenSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class ProductosView(APIView):
    def get(self, request):
        producto = Producto.objects.all()
        producto_serializer = ProductoSerializer(producto, many=True)
        return Response(producto_serializer.data)

class OrdenViewSet(ModelViewSet):
    serializer_class = OrdenSerializer
    queryset = serializer_class.Meta.model.objects.all()