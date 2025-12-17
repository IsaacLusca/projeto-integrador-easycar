from .models import Aluguel
from .serializers import AluguelSerializer
from rest_framework import viewsets
from users.permissions import IsFuncionarioOuSuperuser
from .filters import AluguelFilter

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from decimal import Decimal


class AlugarViewSet(viewsets.ModelViewSet):
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer
    permission_classes = [IsFuncionarioOuSuperuser]
    filterset_class = AluguelFilter

    # Atualiza status atrasado (sem salvar em loop perigoso)
    def get_queryset(self):
        queryset = super().get_queryset()
        hoje = timezone.now().date()

        atrasados = queryset.filter(status='ativo', data_fim__lt=hoje)
        atrasados.update(status='atrasado')

        return queryset

    # Criação do aluguel
    def perform_create(self, serializer):
        aluguel = serializer.save(status='ativo')
        aluguel.carro.marcar_como_alugado()

    # Finalização / devolução do veículo
    @action(detail=True, methods=['post'], url_path='finalizar')
    def finalizar(self, request, pk=None):
        aluguel = self.get_object()

        if aluguel.status not in ['ativo', 'atrasado']:
            return Response(
                {'erro': 'Somente alugueis ativos ou atrasados podem ser finalizados.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        hoje = timezone.now().date()

        dias = (hoje - aluguel.data_inicio).days
        if dias <= 0:
            dias = 1

        valor_base = Decimal(dias) * aluguel.carro.valor_diaria
        multa = Decimal('0.00')

        if hoje > aluguel.data_fim:
            dias_atraso = (hoje - aluguel.data_fim).days
            multa = Decimal(dias_atraso) * aluguel.carro.valor_diaria

        aluguel.valor_total = valor_base + multa
        aluguel.status = 'finalizado'
        aluguel.save()

        aluguel.carro.marcar_como_disponivel()

        return Response(
            {
                'mensagem': 'Aluguel finalizado com sucesso.',
                'valor_base': valor_base,
                'multa': multa,
                'valor_total': aluguel.valor_total
            },
            status=status.HTTP_200_OK
        )

    # Cancelamento do aluguel
    @action(detail=True, methods=['post'], url_path='cancelar')
    def cancelar(self, request, pk=None):
        aluguel = self.get_object()

        if aluguel.status not in ['ativo', 'atrasado']:
            return Response(
                {'erro': 'Somente alugueis ativos ou atrasados podem ser cancelados.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        aluguel.status = 'cancelado'
        aluguel.save()

        aluguel.carro.marcar_como_disponivel()

        return Response(
            {'mensagem': 'Aluguel cancelado com sucesso.'},
            status=status.HTTP_200_OK
        )
