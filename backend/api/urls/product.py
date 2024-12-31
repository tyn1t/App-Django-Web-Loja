from django.urls import path   
from api.views import product

urlpatterns = [
    path('v1/produtos/', product.ProductsAPIView.as_view(), name='products'),
    path('v1/product/', product.ProductAPIViews.as_view(), name='products'),
    path('v1/produtos/<str:str>',product.ProdutcAPIView.as_view(), name='product')
]