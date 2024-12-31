from django.urls import path 
from api.views import order


urlpatterns = [
    path("order/",  order.OrderAPIView.as_view(), name='order'),
    path("order/items/",  order.OrderItemsAPIView.as_view(), name='orderItems'),
    path("orer/items/<int:pk>", order.OrderItemAPIView.as_view(), name="orderItem")
]