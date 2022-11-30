from rest_framework import routers
from .views import JefeViewSet

router = routers.DefaultRouter()
router.register(r'eljefe', JefeViewSet, basename='jefe')

urlpatterns = router.urls
