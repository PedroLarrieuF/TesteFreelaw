from django.test import TestCase
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Evento

from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Evento

class EventoViewSetTestCase(TestCase):
    """
    Testes para a classe EventoViewSet.
    """

    def setUp(self):
        """
        Configuração inicial para cada teste.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_list_eventos(self):
        """
        Testa se a listagem de eventos retorna status 200 (OK).
        """
        response = self.client.get('/eventos/list/')
        self.assertEqual(response.status_code, 200)

    def test_add_participant_event(self):
        """
        Testa se é possível adicionar um participante a um evento e retorna status 201 (Created).
        """
        evento = Evento.objects.create(nome='Evento Teste', local='Local Teste', hora='00:00:00', data='2024-05-13', idealizador=self.user, descricao='Descrição Teste', foto=None)
        response = self.client.post(f'/eventos/add_participant_event/{evento.id}/')
        self.assertEqual(response.status_code, 201)
