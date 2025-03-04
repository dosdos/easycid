import json

import requests
from rest_framework import response, schemas, viewsets
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from cid.carta_si import primo_pagamento_ssl
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


class AniaMockViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        targa = self.kwargs.get('targa', '')
        return Response({'data': targa}, status=status.HTTP_200_OK)


class AciMockViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        patente = self.kwargs.get('patente', '')
        return Response({'data': patente}, status=status.HTTP_200_OK)


class AroundMeMockViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        url = "https://pp.api.helab.nuvolaitaliana.it/si/contacts/v2/locations?companyAteco=52.21.6&lat=45.45111&lon=9.178333"
        headers = {'Keyid': '4d019814-f574-4d72-9e58-5510c60afc5b'}
        companyAteco = self.request.query_params.get('ateco', '52.21.6')
        lat = self.request.query_params.get('lat', '45.45111')
        lon = self.request.query_params.get('lon', '9.178333')
        distance = self.request.query_params.get('distance', '10000')
        params = {
            'companyAteco': companyAteco,
            'lat': lat,
            'lon': lon,
            'distance': distance,
        }
        res = requests.get(url, params=params, headers=headers)
        if res.status_code == 200:
            return Response(json.loads(res.content), status=status.HTTP_200_OK)
        else:
            return Response({'error': 'error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)


class CartaSiMockViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        status_code, resp = primo_pagamento_ssl()
        return Response(resp, status=status.HTTP_200_OK)
