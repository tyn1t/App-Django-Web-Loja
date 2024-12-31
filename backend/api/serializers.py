from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField()
    # name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','_id','username', 'email', 'password','isAdmin']
        
        extra_kwargs  = {'password': {'write_only':True}}
     
    def get__id(self, obj):
        return obj.id 
     
    def get_isAdmin(self, obj):
        return obj.is_staff
     
    # def get_name(self, obj):
    #     name = obj.first_name 
    #     if name == "":
    #          name = obj.email 
    #     return name  
     
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create_user(
                username=  validated_data.get('email'),
                email=validated_data.get('email'),
                password=password,
                first_name=validated_data.get('username')
        )
        return user
        
        
        
    
class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField() # Ou username, se for o caso
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email') # Ou username, se for o caso
        password = data.get('password')

        if email and password:
           pass
        else:
            raise serializers.ValidationError('Informe o nome de usuário e a senha.')
        return data
  
            
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = "__all__"
        
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review 
        fields = "__all__"
        
class OrderSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Order
        fields = ["_id", "paymentMethod", "taxPrice", "shippingPrice", "totalPrice",
    "isPaid","paidAt", "isDeliver", "deliveredAt", "createdAt", "user"]
   
class  OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems 
        fields = "__all__"
    
class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress 
        fields = "__all__"
        