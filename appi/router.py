from rest_framework import routers
from .views import OrdenViewSet

router = routers.DefaultRouter()
router.register(r'orden', OrdenViewSet, basename='orden')

urlpatterns = router.urls