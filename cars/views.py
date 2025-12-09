from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Carro
from .serializers import CarroSerializer
from users.permissions import IsFuncionario  
from rest_framework.permissions import IsAdminUser

# Create your views here.

class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    permission_classes = [IsAuthenticated,  IsFuncionario | IsAdminUser]

