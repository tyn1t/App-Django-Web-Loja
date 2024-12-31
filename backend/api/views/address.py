# return api view
from rest_framework import status, generics
from rest_framework.response import Response 

#auth
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
#user
from django.db import IntegrityError
from django.contrib.auth.models import User

#my models 
from api.models import Order, OrderItems, ShippingAddress 
from api.serializers import OrderSerializer, OrderItemsSerializer, ShippingAddressSerializer

    
class ShippingAddressAPIView(generics.ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer