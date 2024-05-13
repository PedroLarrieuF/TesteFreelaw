from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
import csv

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manipulação de usuários.
    """

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Cria um novo usuário.
        """
        self.permission_classes = []
        return super().create(request, *args, **kwargs)
    
    @action(detail=False, methods=['get'])
    def count_users(self, request):
        """
        Endpoint para contar quantos usuários existem.
        """
        total_usuarios = Usuario.objects.count()
        return Response({'total_usuarios': total_usuarios})

    @action(detail=False, methods=['get'])
    def export_users_csv(self, request):
        """
        Método para exportar todos os usuários para CSV.
        """
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="usuarios.csv"'

        # Obtem todos os usuários
        usuarios = Usuario.objects.all()

        # Define os cabeçalhos do CSV
        fieldnames = ['id', 'nome', 'email']  # Adicione mais campos conforme necessário

        # Crie o escritor CSV
        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()

        # Escreve os usuários no CSV
        for usuario in usuarios:
            writer.writerow({'id': usuario.id, 'nome': usuario.nome, 'email': usuario.email})  # Adicione mais campos conforme necessário

        return response
    
    @action(detail=True, methods=['put'])
    def update_user(self, request, pk=None):
        """
        Método para atualizar um usuário específico.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
