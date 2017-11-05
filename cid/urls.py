from rest_framework import routers

from cid.views import VehicleViewSet, ProfileViewSet, AccidentViewSet, AniaMockViewSet, AciMockViewSet, AroundMeMockViewSet

urlpatterns = []

router = routers.DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'accidents', AccidentViewSet)
router.register(r'ania_api/(?P<targa>\d+)', AniaMockViewSet, 'ania_api')
router.register(r'aci_api/(?P<patente>\d+)', AciMockViewSet, 'aci_api')
router.register(r'trova_carroattrezzi/', AroundMeMockViewSet, 'trova_carroattrezzi')
