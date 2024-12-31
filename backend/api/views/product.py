# return api view
from rest_framework import status, generics
from rest_framework.response import Response 
from rest_framework.views import APIView

#auth
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
#user
from django.db import IntegrityError
from django.contrib.auth.models import User

#my models 
from api.models import Product
from api.serializers import ProductSerializer, ReviewSerializer


class ProductAPIViews(APIView):
    
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    
class ProductsAPIView(generics.CreateAPIView):
    # Todo Accesso só para admin ou gerente  confirmar e Gerente ou admin acesso
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            self.perform_create(serializer)
            headers = self.get_success_headers(data=serializer.data)
            return Response({'Produto':'Criado succes'}, status=status.HTTP_201_CREATED, headers=headers)
        except IntegrityError:
            return Response({'Produto':'Criado succes'})
        

   
class ProdutcAPIView(generics.RetrieveUpdateDestroyAPIView):
    # Todo 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    
    
    
        