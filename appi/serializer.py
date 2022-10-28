from rest_framework import serializers
from .models import Producto, Orden



class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'
        
    def to_representation(self, instance):
        
        return {
            'id' : instance.id,
            'nombre' : instance.nombre,
            'precio' : instance.precio,
            'img' : instance.img
            }
