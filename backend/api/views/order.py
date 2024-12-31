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
from api.models import Order, OrderItems, Product
from api.serializers import OrderSerializer, OrderItemsSerializer, ShippingAddressSerializer


class OrderAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        product = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(product, many=True)
        return Response(serializer.data)
    
      


    
class OrderItemsAPIView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
    
    def post(self, request, *args, **kwargs):
        product = Product.objects.get(_id=request.data['product'])
        if request.data['qty'] > product.countInStock:
            return Response({'ErroQty':"Compre uma quantidade meno"}, status=status.HTTP_204_NO_CONTENT)
        return super().post(request, *args, **kwargs)
    
 
class OrderItemAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer