from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from users import permissions
from .models import Aluguel
from .serializers import AluguelSerializer
from rest_framework import viewsets
from users.permissions import IsFuncionarioOuSuperuser


class AlugarCarro(viewsets.ModelViewSet):
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer
    permission_classes = [IsFuncionarioOuSuperuser]




    
        
        


    

   


