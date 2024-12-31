from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# My Api + admin 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('api.urls.user')),
    path('loja/api/', include('api.urls.product')),
    path('address/api/', include('api.urls.address')),
    path('payment/api/', include('api.urls.order')),
]


# swagger
urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
