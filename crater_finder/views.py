import django_filters
from raven.utils import json
from rest_framework import authentication
from rest_framework import generics
from rest_framework import parsers
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from crater_finder.models import Vehicle, Employee, Crater, Fall
from crater_finder.serializers import VehicleSerializer, EmployeeSerializer, CraterSerializer, FallSerializer


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    @detail_route(methods=['post'])
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CraterViewSet(viewsets.ModelViewSet):
    serializer_class = CraterSerializer
    queryset = Crater.objects.all()


class FallViewSet(viewsets.ModelViewSet):
    serializer_class = FallSerializer
    queryset = Fall.objects.all()


class ListCraters(generics.ListAPIView):
    queryset = Crater.objects.all()
    serializer_class = CraterSerializer


class ReceiveReport(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    def post(self, request, format=None):
        pass