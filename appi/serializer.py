from rest_framework import serializers
from .models import Producto, Orden



class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


def productos(instance):
    array = []
    for producto in instance.productos.all():
        array.append({
            'nombre' : producto.nombre,
            'precio' : producto.precio,
            'img' : producto.img
        })
    print(array)
    return(array)

def total(instance):
    array = 0
    for producto in instance.productos.all():
        array += int(producto.precio)
    print(array)
    return(array)

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'

    # def products(self, instance):
    # array = []
    # product = Producto.objects.filter(post = instance.id)
    # for like in likes:
    #     slug = UserExtend.objects.get(user = like.author.id)
    #     array.append({'user_id' : like.author.id, 'username': like.author.username, 'user_slug' : slug.slug, 'user_img' : slug.profile_image})
    # return array

    
        
    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'productos' : productos(instance),
            'total' : total(instance)
            }
