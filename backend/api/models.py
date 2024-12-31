from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default="/images/placeholder.png", upload_to="images/")
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    ratimg = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return self.name + " | " + self.brand + " | " + str(self.price)
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comement = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return str(self.rating)
    
class Order(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   paymentMethod = models.CharField(max_length=200, null=True)
   taxPrice = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
   shippingPrice = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
   totalPrice = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
   isPaid = models.BooleanField(default=False)
   paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
   isDeliver = models.BooleanField(default=False)
   deliveredAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
   createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
   _id = models.AutoField(primary_key=True, editable=False)
   
   def __str__(self) -> str:
       return str(self.createdAt)

class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    
    def __str__(self) -> str:
        return self.name
    

class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200,null=True, blank=True)
    shippingPrice  = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return self.address