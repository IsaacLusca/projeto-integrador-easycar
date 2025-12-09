from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import PerfilCliente
from rest_framework.exceptions import PermissionDenied

# serializer para criar/editar usuários (apenas funcionários)
# -----------------------------------------------------------
class ClienteSerializer(serializers.ModelSerializer):
    
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # campos que podem ser preenchidos
        # is_staff e is_superuser não são expostos para evitar que funcionários criem outros funcionários/admins
        fields = ['id', 'username', 'email', 'senha', 'is_active']

    def create(self, dados_validados):
        # verifica o usuario logado que esta fazendo a requisicao 
        usuario_logado = self.context['request'].user

        # verifica se o usuário logado é funcionário
        # se não for, retorna erro 403 Forbidden
        if not usuario_logado.groups.filter(name="Funcionários").exists():
            raise PermissionDenied("Apenas funcionários podem criar clientes.")

        # cria o usuário cliente no banco de dados
        # is_staff e is_superuser são sempre False para clientes
        cliente = User.objects.create_user(
            username=dados_validados['username'],         
            email=dados_validados['email'],               
            password=dados_validados['senha'],           
            is_staff=False,                               
            is_superuser=False,                           
            is_active=dados_validados.get('is_active', True)  # ativo por padrão
        )

        #adiciona o usuário criado por funcionario automaticamente ao grupo "Clientes"
        grupo_cliente = Group.objects.get(name="Clientes")
        cliente.groups.add(grupo_cliente)


        cliente.save()

        return cliente

# ------------------------------------------------------------------------------


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class PerfilClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = PerfilCliente
        fields = ['id', 'user', 'cnh', 'telefone', 'endereco']
