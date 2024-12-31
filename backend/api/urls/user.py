from django.urls import path   
from api.views import user
from rest_framework_simplejwt.views import ( TokenRefreshView, TokenObtainPairView)

urlpatterns = [
    path('api/v1/register/', user.RegisterAPIView.as_view(), name='register'),
    path('api/v1/login/', user.LoginAPIView.as_view(), name="Login"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]