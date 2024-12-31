from django.urls import path 
from api.views import address


urlpatterns = [
    path("address/",  address.ShippingAddressAPIView.as_view(), name='address'),
]