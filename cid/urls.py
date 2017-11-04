from rest_framework import routers

from cid.views import VehicleViewSet, ProfileViewSet, AccidentViewSet

urlpatterns = [
    # url(r'^test-url$', test_url, name='test_url'),
]

router = routers.DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'accidents', AccidentViewSet)
