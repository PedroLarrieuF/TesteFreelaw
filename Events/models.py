from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.utils import timezone

def validate_participantes_limit(value):
    """
    Valida se o número de participantes não excede o limite de 100.

    Args:
        value (QuerySet): O conjunto de participantes do evento.

    Raises:
        ValidationError: Se o número de participantes exceder 100.
    """
    if value.count() > 100:
        raise ValidationError('O número máximo de participantes é 100.')


class Evento(models.Model):
    """
    Representa um evento.
    """
    REGIOES_BRASIL = [
        ('Norte', 'Norte'),
        ('Nordeste', 'Nordeste'),
        ('Centro-Oeste', 'Centro-Oeste'),
        ('Sudeste', 'Sudeste'),
        ('Sul', 'Sul'),
    ]

    nome = models.CharField(max_length=100, unique=True)
    local = models.CharField(max_length=100, choices=REGIOES_BRASIL)
    hora = models.TimeField()
    data = models.DateField(validators=[MinValueValidator(limit_value=timezone.now().date())])
    idealizador = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='eventos/', blank=True, null=True, help_text= "Adicione o logo de seu evento.")
    participantes = models.ManyToManyField(User, related_name='eventos_inscritos', blank=True, validators=[validate_participantes_limit])


    def __str__(self):
        return self.nome
