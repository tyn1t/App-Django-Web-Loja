from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

# Authenticação user 
from django.db import IntegrityError
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# models e serializers
from django.contrib.auth.models import User
from api.serializers import UserSerializer, UserLoginSerializer

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
          self.perform_create(serializer)
          headers = self.get_success_headers(serializer.data) 
          return Response({'detail': 'Usuario Criado com succes.'},status=status.HTTP_201_CREATED, headers=headers)
        except IntegrityError: 
            return Response({'detail': 'Usuário com este e-mail já existe.'}, status=status.HTTP_400_BAD_REQUEST)
 


class LoginAPIView(APIView):
    serializer_class = UserLoginSerializer 

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']  
        password = serializer.validated_data['password']

        user = authenticate(username=email, password=password) # Autentique com o email (ou username se aplicável)
        
        if user:

            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Credenciais inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)
          
      
    
# class OlaAPIView(generics.ListCreateAPIView):
#       authentication_classes = [JWTAuthentication]
#       permission_classes = [IsAuthenticated]
      
#       def get(self, request):
#         return Response({"Ola":"mundo"})