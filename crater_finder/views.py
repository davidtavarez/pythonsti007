import django_filters
import rest_framework
from django.http import Http404
from raven.utils import json
from rest_framework import authentication
from rest_framework import generics
from rest_framework import parsers
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

from crater_finder.models import Vehicle, Employee, Crater, Fall
from crater_finder.serializers import VehicleSerializer, EmployeeSerializer, CraterSerializer, FallSerializer, \
    CraterListSerializer


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


class CraterDetails(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        crater = self.get_object(pk)
        serializer = CraterSerializer(crater)
        return Response(serializer.data)


class ListCraters(generics.ListAPIView):
    queryset = Crater.objects.all()
    serializer_class = CraterListSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (OrderingFilter,)
    ordering_fields = '__all__'
    ordering = ('-discovered_at')


class EmployeeDetails(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReceiveReport(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def post(self, request, format=None):
        pass


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CraterViewSet(viewsets.ModelViewSet):
    serializer_class = CraterSerializer
    queryset = Crater.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FallViewSet(viewsets.ModelViewSet):
    serializer_class = FallSerializer
    queryset = Fall.objects.all()
