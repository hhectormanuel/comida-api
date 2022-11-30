from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Producto, Orden, Contacto
from .serializer import ProductoSerializer, OrdenSerializer, ContactoSerializer, JefeSerializer
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


class ContactoView(APIView):
    def get(self, request):
        contacto = Contacto.objects.all()
        contacto_serializer = ContactoSerializer(contacto, many=True)
        return Response(contacto_serializer.data)


class ContactoViewSet(ModelViewSet):
    serializer_class = ContactoSerializer
    queryset = serializer_class.Meta.model.objects.all()
    
class JefeViewSet(ModelViewSet):
    serializer_class = JefeSerializer
    queryset = serializer_class.Meta.model.objects.all()
