from django.urls import path
from .views import ProductosView

app_name='appi'

urlpatterns = [
    path('', ProductosView.as_view(), name='get'),
]