from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Aluguel
from .serializers import AluguelSerializer
from users.permissions import IsFuncionario  
from rest_framework.permissions import IsAdminUser

# Create your views here.

class AluguelViewSet(viewsets.ModelViewSet):
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer
    permission_classes = [IsAuthenticated,  IsFuncionario | IsAdminUser]


