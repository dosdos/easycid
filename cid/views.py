from rest_framework import response, schemas, viewsets
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from .serializers import *


@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def api_docs(request):
    generator = schemas.SchemaGenerator(title='Bookings API')
    return response.Response(generator.get_schema(request=request))


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class AccidentViewSet(viewsets.ModelViewSet):
    queryset = Accident.objects.all()
    serializer_class = AccidentSerializer
