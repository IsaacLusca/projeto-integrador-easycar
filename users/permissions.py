from rest_framework.permissions import BasePermission

class IsFuncionario(BasePermission):

# Permite que apenas usuários que pertençam ao grupo 'Funcionários' ou
# sejam superusuários acessem a view.
    

    def has_permission(self, request, view):
        # pega o usuário logado
        user = request.user
        
        # retorna True se o usuário existir E for superuser ou pertencer ao grupo Funcionários
        return user and (user.is_superuser or user.groups.filter(name='Funcionários').exists())
