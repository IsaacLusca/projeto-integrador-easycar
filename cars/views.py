from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Carro
from .serializers import CarroSerializer
from .permissions import IsFuncionario



class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

    # 🔹 Rota pública: lista só disponíveis
    def get_queryset(self):
        if self.action == 'disponiveis':
            return Carro.objects.filter(status='disponivel')
        return Carro.objects.all()

    # 🔹 Apenas funcionário pode usar essas actions
    @action(detail=True, methods=['post'], permission_classes=[IsFuncionario])
    def alugar(self, request, pk=None):
        carro = self.get_object()
        carro.marcar_como_alugado()
        return Response({'mensagem': 'Carro alugado com sucesso'})

    @action(detail=True, methods=['post'], permission_classes=[IsFuncionario])
    def devolver(self, request, pk=None):
        carro = self.get_object()
        carro.marcar_como_disponivel()
        return Response({'mensagem': 'Carro devolvido com sucesso'})

    # 🔹 Rota pública para ver só disponíveis
    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def disponiveis(self, request):
        carros = Carro.objects.filter(status='disponivel')
        serializer = self.get_serializer(carros, many=True)
        return Response(serializer.data)
