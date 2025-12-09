from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.views import PerfilClienteViewSet

from rest_framework.authtoken import views as drf_views
from users.views import PerfilClienteViewSet
from users.views import UserViewSet, PerfilClienteViewSet
from cars.views import CarroViewSet
from rentals.views import AluguelViewSet

router = routers.DefaultRouter()
router.register(r'clientes', PerfilClienteViewSet, basename='cliente')
router.register(r'users', UserViewSet, basename='user')
router.register(r'carros', CarroViewSet, basename='carro')
router.register(r'alugueis', AluguelViewSet, basename='aluguel')

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/token/', drf_views.obtain_auth_token),  # rota para pegar token
]
