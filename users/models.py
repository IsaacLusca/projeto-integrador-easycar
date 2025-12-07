from django.db import models
from django.contrib.auth.models import User

class PerfilCliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cnh = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return f"Perfil de {self.user.username}"
    
    # função para retornar histórico
    def get_historico_alugueis(self):
        return
    
    # função para retornar alugueis ativos
    def get_alugueis_ativos(self):
        return
    