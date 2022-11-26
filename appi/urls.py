from django.urls import path
from .views import ProductosView, ContactoView

app_name='appi'

urlpatterns = [
    path('', ProductosView.as_view(), name='get'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
]