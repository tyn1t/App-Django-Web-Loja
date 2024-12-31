from django.contrib import admin
from django.forms import ModelForm
from django.http import HttpRequest

from .models import *
# Register your models here.
admin.site.register(Review)
admin.site.register(ShippingAddress)
admin.site.register(OrderItems)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
                     "user", "createdAt","totalPrice"
            ]
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
    
    list_display = [
        "user", "name", "image", "brand", "category", "description", 
        "ratimg", "numReviews", "price", "countInStock", "createdAt", "_id"
    ]
      
    def save_model(self, request, obj, form, change) -> None:
        if not obj.pk:
            self.user = obj.user
        return super().save_model(request, obj, form, change)
    
    def get_queryset(self, request: HttpRequest):
        return super(ProductAdmin, self).get_queryset(request).filter(user=request.user)
     