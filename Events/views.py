import csv
import base64
from io import StringIO
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.models import Count, F
from .models import Evento
from .serializers import EventoSerializer
from .sendemail import enviar_email

class EventoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manipulação de eventos.
    """

    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def list(self, request):
        """
        Endpoint para listar todos os eventos com contagem de participantes.
        """
        eventos = Evento.objects.all()
        data = []
        for evento in eventos:
            participantes_count = evento.participantes.count()
            data.append({'evento': evento.nome, 'participantes_count': participantes_count})
        return Response(data)
    
    @action(detail=False, methods=['post'])
    def add_participant_event(self, request, id):
        """
        Adiciona um usuário como participante de um evento.
        """
        try:    
            evento = Evento.objects.get(id=id)
        except Evento.DoesNotExist:
            return Response({"error": "Evento não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        if request.user.is_authenticated:
            evento.participantes.add(request.user)
            return Response({"message": "Você foi cadastrado no evento com sucesso"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Você precisa estar logado para se cadastrar em um evento"}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['get'])
    def count_total_events_csv(self, request):
        """
        Conta quantos eventos existem no total e gera um CSV em base64.
        """
        total_eventos = Evento.objects.count()
        eventos = Evento.objects.all()
        eventos_data = EventoSerializer(eventos, many=True).data
        
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=['id', 'nome', 'local', 'hora', 'data', 'idealizador', 'descricao', 'foto'])
        writer.writeheader()
        for evento in eventos_data:
            writer.writerow(evento)
        csv_content = output.getvalue()
        output.close()

        csv_base64 = base64.b64encode(csv_content.encode()).decode()

        return Response({'total_eventos': total_eventos, 'csv_base64': csv_base64})

    @action(detail=False, methods=['get'])
    def count_events_by_region(self, request):
        """
        Conta quantos eventos existem por região.
        """
        eventos_por_regiao = Evento.objects.values('local').annotate(total=Count('id'))
        return Response({'eventos_por_regiao': eventos_por_regiao})

    @action(detail=False, methods=['get'])
    def count_events_by_region_and_day(self, request):
        """
        Conta quantos eventos existem por região e por dia.
        """
        eventos_por_regiao_e_dia = Evento.objects.annotate(dia=F('data')).values('local', 'dia').annotate(total=Count('id'))
        return Response({'eventos_por_regiao_e_dia': eventos_por_regiao_e_dia})

    @action(detail=False, methods=['get'])
    def count_events_in_month(self, request, month):
        """
        Conta quantos eventos existem naquele mês.
        """
        eventos_no_mes = Evento.objects.filter(data__month=month).count()
        return Response({'eventos_no_mes': eventos_no_mes})

    @action(detail=False, methods=['get'])
    def user_with_most_created_events(self, request):
        """
        Informa qual usuário criou mais eventos.
        """
        usuario_mais_eventos = User.objects.annotate(num_eventos_criados=Count('evento')).order_by('-num_eventos_criados').first()
        return Response({'usuario_mais_eventos': usuario_mais_eventos.username})

    @action(detail=False, methods=['get'])
    def create(self, request, *args, **kwargs):
        """
        Sobrescreve o método create para notificar o usuário se a região do evento for a mesma do usuário.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        evento = serializer.instance
        usuarios = User.objects.filter(usuario__regiao_brasil=evento.local)
        for usuario in usuarios:
            destinatario = usuario.email
            assunto = 'Novo Evento Disponível!'
            mensagem = f'Olá {usuario.nome},\n\nUm novo evento está disponível! Verifique agora mesmo em nosso aplicativo.\n\nAtenciosamente,\nSua Equipe'
            enviar_email(destinatario, assunto, mensagem)


        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['put'])
    def update(self, request, *args, **kwargs):
        """
        Sobrescreve o método update para notificar o usuário se a região do evento for a mesma do usuário.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        lookup_field = id
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        evento = serializer.instance
        usuarios = User.objects.filter(usuario__regiao_brasil=evento.local)
        for usuario in usuarios:
            destinatario = usuario.email
            assunto = 'Novo Evento Disponível!'
            mensagem = f'Olá {usuario.nome},\n\nUm novo evento está disponível! Verifique agora mesmo em nosso aplicativo.\n\nAtenciosamente,\nSua Equipe'
            enviar_email(destinatario, assunto, mensagem)


        return Response(serializer.data)
