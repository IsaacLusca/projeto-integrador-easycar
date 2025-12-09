from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import PerfilCliente
from .serializers import PerfilClienteSerializer, ClienteSerializer 
from .permissions import IsFuncionario
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# CRUD de usuários (somente funcionários ou superuser)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated, IsFuncionario | IsAdminUser]

# CRUD de perfis de clientes (somente funcionários ou superuser)
class PerfilClienteViewSet(viewsets.ModelViewSet):
    queryset = PerfilCliente.objects.all()
    serializer_class = PerfilClienteSerializer
    permission_classes = [IsAuthenticated, IsFuncionario | IsAdminUser]


# classe para visualizar os perfis dos clientes
class PerfilClienteReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    # usa o serializador de perfil de cliente
    serializer_class = PerfilClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # pega o usuário logado
        user = self.request.user

        # se for staf, retorna todos os perfis
        if user.is_staff:
            return PerfilCliente.objects.select_related('user').all()
        
        return PerfilCliente.objects.select_related('user').filter(user=user)