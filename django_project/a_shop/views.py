from django.http import Http404
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from a_shop.serializers import *


class MayorViewSet(viewsets.ModelViewSet):
    queryset = Mayor.objects.all()
    serializer_class = MayorSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
